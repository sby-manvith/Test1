"""
Web-based calculator utilities.
WARNING: This file contains intentional security vulnerabilities for code scanning demo purposes.
"""

import os
import sqlite3
import subprocess


# Hardcoded credentials (security vulnerability)
DB_USER = "admin"
DB_PASSWORD = "supersecret123"
SECRET_KEY = "hardcoded-secret-key-do-not-use"


def evaluate_expression(expression):
    """Evaluate a math expression from user input.

    VULNERABILITY: Uses eval() with unsanitized user input — code injection risk.
    """
    result = eval(expression)  # noqa: S307
    return result


def run_system_command(user_input):
    """Run a system command based on user input.

    VULNERABILITY: Shell injection — user input passed directly to shell.
    """
    output = subprocess.check_output("echo " + user_input, shell=True)
    return output.decode()


def get_user_by_name(username):
    """Fetch a user record from the database by name.

    VULNERABILITY: SQL injection — username is interpolated directly into query.
    """
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows


def read_user_file(filename):
    """Read a file specified by the user.

    VULNERABILITY: Path traversal — no validation of filename.
    """
    with open(filename, "r") as f:
        return f.read()


def log_calculation(user_input, result):
    """Log a calculation result to a file specified by the user.

    VULNERABILITY: Uncontrolled write path — user controls the file name.
    """
    log_path = "/var/log/" + user_input + ".log"
    with open(log_path, "w") as f:
        f.write(str(result))


if __name__ == "__main__":
    print(evaluate_expression("1 + 2"))
    print(run_system_command("Hello"))
    print(get_user_by_name("alice"))

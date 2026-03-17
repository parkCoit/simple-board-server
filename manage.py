#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import json
import os
import sys

import django
import pymysql
from django.core.management import call_command

scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'admin/secrets.json')
with open(filename, "r") as f:
    secrets = json.load(f)


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def create_db_if_not_exists():
    connection = pymysql.connect(
        host=secrets["DATABASE"]["default"]["HOST"],
        user=secrets["DATABASE"]["default"]["USER"],
        password=secrets["DATABASE"]["default"]["PASSWORD"]
    )
    try:
        with connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS simple_board CHARACTER SET utf8mb4;")

        django.setup()
        call_command('migrate', interactive=False)

    except Exception as e:
        print(f"⚠️ Error during DB setup: {e}")
    finally:
        connection.close()


if __name__ == '__main__':
    create_db_if_not_exists()
    main()

# coding=utf-8

DB = {
    "password": "db_password",
    "login": "db_login",
    "name": "db_name",
    "host": "db_host"
}

try:
    # Try to load local values
    from local_conf import *

except ModuleNotFoundError:
    # No local config found
    print("Local config not found")

    raise ModuleNotFoundError(str("Local config not found"))

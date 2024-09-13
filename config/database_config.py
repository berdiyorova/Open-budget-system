import os

from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

DB_CONFIG = {
    "database": DB_NAME,
    "user": DB_USER,
    "host": DB_HOST,
    "port": DB_PORT,
    "password": DB_PASS
}

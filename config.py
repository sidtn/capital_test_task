import os

from dotenv import load_dotenv

load_dotenv()


DB_USER = os.getenv("DB_USER", default="capital_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="password")
DB_NAME = os.getenv("DB_NAME", default="capital_db")
DB_HOST = os.getenv("DB_HOST", default="localhost")
DB_PORT = os.getenv("DB_PORT", default="5432")

DB_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

TEST_DB_USER = os.getenv("TEST_DB_USER", default="capital_user_test")
TEST_DB_PASSWORD = os.getenv("TEST_DB_PASSWORD", default="password_test")
TEST_DB_NAME = os.getenv("TEST_DB_NAME", default="capital_db_test")
TEST_DB_HOST = os.getenv("TEST_DB_HOST", default="localhost")
TEST_DB_PORT = os.getenv("TEST_DB_PORT", default="5433")

TEST_DB_URI = f"postgresql://{TEST_DB_USER}:{TEST_DB_PASSWORD}@{TEST_DB_HOST}:{TEST_DB_PORT}/{TEST_DB_NAME}"

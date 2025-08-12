import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    BASE_URL = os.getenv('BASE_URL')

    TEST_USER_USERNAME = os.getenv('TEST_USER_USERNAME')
    TEST_USER_EMAIL = os.getenv('TEST_USER_EMAIL')
    TEST_USER_PASSWORD = os.getenv('TEST_USER_PASSWORD')


settings = Settings()

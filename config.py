import os

os.environ['APP_BASE_URL'] = os.getenv("APP_BASE_URL", "http://localhost:2019")

LOGIN = os.getenv("LOGIN", "test")
PASSWORD = os.getenv("PASSWORD", "test")
import os

DB_NAME = os.environ.get('DATABASE_NAME', 'thing_type')
USERNAME = os.environ.get('DB_USER', 'admin')
PASSWORD = os.environ.get('PASSWORD', 'pass123')
URL = os.environ.get('DB_URL', '127.0.0.1')

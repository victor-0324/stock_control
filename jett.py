import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DATABASE_CONNECTION = os.environ.get('DATABASE_CONNECTION')
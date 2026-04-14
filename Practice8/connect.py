import psycopg2
from config import DaBa_CONFIG

def connect():
    return psycopg2.connect(**DaBa_CONFIG)
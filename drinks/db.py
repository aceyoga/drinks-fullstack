import psycopg2
import os

# Database connection parameters
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres.kktlpydtltwixpxpmrat:Skibidi1234@aws-0-us-east-1.pooler.supabase.com:5432/postgres')

class DatabaseConnection:
    _instance = None
    _connection = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DatabaseConnection, cls).__new__(cls, *args, **kwargs)
            cls._connection = psycopg2.connect(DATABASE_URL)
        return cls._instance

    @property
    def connection(self):
        return self._connection

# Function to get the singleton database connection
def get_db_connection():
    db_instance = DatabaseConnection()
    return db_instance.connection
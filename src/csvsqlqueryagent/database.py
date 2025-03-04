import os
import pandas as pd
from sqlalchemy import create_engine
from config import DATABASE_PATH, CSV_PATH

# Ensure the database directory exists
os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)

# Create database connection
engine = create_engine(f"sqlite:///{DATABASE_PATH}")

def initialize_database():
    """Load CSV into the database (only run if the database is empty)."""
    df = pd.read_csv(CSV_PATH).fillna(0)
    df.to_sql("salaries_2023", con=engine, if_exists="replace", index=False)
    print("Database initialized successfully!")

def get_engine():
    """Return database engine."""
    return engine

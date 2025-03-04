import os
import sqlite3
import pandas as pd

# Define paths relative to the project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Moves up three levels

DB_PATH = os.path.join(BASE_DIR, "db", "salary.db")
CSV_PATH = os.path.join(BASE_DIR, "data", "salaries_2023.csv")

# Access SQLite database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Load CSV file into Pandas
df = pd.read_csv(CSV_PATH)

print("Database Path:", DB_PATH)
print("CSV Data Preview:", df.head())

# Close DB connection
conn.close()

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# LLM Model
LLM_NAME = "gpt-3.5-turbo"

# Base Directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Database Path
DATABASE_PATH = os.path.join(BASE_DIR, "db", "salary.db")

# CSV File Path
CSV_PATH = os.path.join(BASE_DIR, "data", "salaries_2023.csv")

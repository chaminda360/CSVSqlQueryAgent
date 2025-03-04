# CSV SQL Query Agent  

## 📌 Overview  
**CSV SQL Query Agent** is a Python-based application that allows users to query a database created from a CSV file using natural language. It leverages **OpenAI's LLM (GPT-3.5/4)** to generate SQL queries and execute them against an **SQLite database**. The project features a **Streamlit UI**, enabling users to input queries and receive results dynamically.  

## ⚙️ How It Works  
1. **CSV to Database** – A CSV file (`salaries_2023.csv`) is converted into an SQLite database (`salary.db`).  
2. **AI-Powered Query Generation** – User queries in natural language are converted into SQL using **LangChain's SQL Agent**.  
3. **Streamlit Interface** – Users interact with the system through a web UI, inputting queries and viewing results.  

## 🛠️ Tech Stack  
- **Python** (Core logic)  
- **SQLite** (Database storage)  
- **LangChain + OpenAI** (AI-powered SQL query generation)  
- **Streamlit** (User interface)  
- **SQLAlchemy + Pandas** (Database and data processing)  

## 🚀 How to Run the Program  

### 1️⃣ **Clone the Repository**  
```bash
git clone https://github.com/your-repo/csv-sql-query-agent.git
cd csv-sql-query-agent
```
### 2️⃣ Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate      # On Windows
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Set Up Environment Variables
Create a .env file in the project root and add:
```bash
OPENAI_API_KEY=your_openai_api_key
```
### 5️⃣ Run the Application
```bash
streamlit run src/csvsqlqueryagent/app.py
```
### 6️⃣ Interact with the UI
    Open the URL displayed in the terminal (usually http://localhost:8501).

    Enter a natural language query and get AI-generated SQL responses.
## 📌Example Query
"What is the highest average salary by department?"
The AI generates an SQL query, retrieves results from the database, and displays them in the UI.

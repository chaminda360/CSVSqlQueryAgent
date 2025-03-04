import streamlit as st
from llm_agent import get_sql_agent
from database import initialize_database

# Initialize database (if needed)
initialize_database()

# Streamlit UI
st.title("SQL Query AI Agent")

question = st.text_input("Enter your query:")

if st.button("Run Query"):
    if question:
        sql_agent = get_sql_agent()
        res = sql_agent.invoke(question)
        st.markdown(res["output"])
    else:
        st.error("Please enter a query.")

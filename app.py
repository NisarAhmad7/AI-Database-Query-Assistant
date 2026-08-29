from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import sqlite3
from groq import Groq


# Configure Groq
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


# Function to load Groq model and generate SQL
def get_groq_response(question, prompt):
    

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": prompt[0]
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "student.db")
# Function to retrieve query from database
def read_sql_query(sql, DB_PATH):

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute(sql)

    rows = cur.fetchall()

    conn.close()

    return rows


# Define your prompt
prompt = [
    """
    You are an expert in converting English questions to SQL queries.

    The SQL database is called STUDENT.

    The STUDENT table has these columns:

    NAME
    CLASS
    SECTION
    MARKS

    Examples:

    Example 1:
    Question: How many students are there?

    SQL:
    SELECT COUNT(*) FROM STUDENT;

    Example 2:
    Question: Tell me all the students studying in Data Science class.

    SQL:
    SELECT * FROM STUDENT WHERE CLASS="Data Science";

    Important instructions:

    1. Return ONLY the SQL query.
    2. Do not include ``` at the beginning or end.
    3. Do not include the word SQL.
    4. Use the STUDENT table.
    5. Use only the columns NAME, CLASS, SECTION, and MARKS.
    """
]


# Streamlit App
st.set_page_config(
    page_title="I can Retrieve Any SQL Query"
)

st.header("SQL Retrieve APP ")


question = st.text_input(
    "Input:",
    key="input"
)


submit = st.button("Ask the question")


# If submit is clicked
if submit:

    response = get_groq_response(question, prompt)

    st.write("Generated SQL:")
    st.code(response, language="sql")

    try:

        result = read_sql_query(
            response,
            "student.db"
        )

        st.subheader("The Response is:")

        for row in result:
            st.write(row)

    except Exception as e:

        st.error(f"SQL Error: {e}")
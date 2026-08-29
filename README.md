# AI SQL Query Assistant

An AI-powered SQL assistant that lets users query a SQLite database using natural language.

Instead of writing SQL manually, users can simply ask questions like:

- How many students are there?
- Who scored more than 80 marks?
- Show all students in Machine Learning class.
- Who has the highest marks?

The application uses Groq to convert the user's question into a SQL query, executes that query on a SQLite database, and displays the result through a Streamlit interface.

## How It Works

The application follows a simple flow:

User Question → Streamlit → Groq LLM → SQL Query → SQLite Database → Result

For example, when the user asks:

"Who scored more than 80 marks?"

The AI generates:

```sql
SELECT * FROM STUDENT WHERE MARKS > 80;

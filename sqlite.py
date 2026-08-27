import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

# Create the table
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
"""

cursor.execute(table_info)

# Check if the table already has data
cursor.execute("SELECT COUNT(*) FROM STUDENT")
count = cursor.fetchone()[0]

if count == 0:

    cursor.execute("""
    INSERT INTO STUDENT VALUES
    ('Nisar', 'Machine Learning', 'A', 90)
    """)

    cursor.execute("""
    INSERT INTO STUDENT VALUES
    ('Ahmad', 'Data Science', 'B', 100)
    """)

    cursor.execute("""
    INSERT INTO STUDENT VALUES
    ('Ali', 'Machine Learning', 'A', 86)
    """)

    cursor.execute("""
    INSERT INTO STUDENT VALUES
    ('karim', 'DEVOPS', 'A', 50)
    """)

    cursor.execute("""
    INSERT INTO STUDENT VALUES
    ('Hakim', 'DEVOPS', 'A', 35)
    """)



print("The inserted records are:")

data = cursor.execute("SELECT * FROM STUDENT")

for row in data:
    print(row)

connection.commit()
connection.close()
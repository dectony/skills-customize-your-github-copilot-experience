import sqlite3

# The database file is provided — run this script from the assignment folder.
DB_FILE = "school.db"

# ── Setup: create and seed the database (do not modify this section) ──────────
def setup_database():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            name  TEXT NOT NULL,
            grade TEXT NOT NULL
        )
    """)
    conn.execute("DELETE FROM students")  # reset on each run
    conn.executemany("INSERT INTO students (name, grade) VALUES (?, ?)", [
        ("Alice",   "A"),
        ("Bob",     "B"),
        ("Carlos",  "A"),
        ("Diana",   "C"),
        ("Ethan",   "B"),
    ])
    conn.commit()
    conn.close()

setup_database()

# ── Task 1: Connect and explore the schema ────────────────────────────────────
# TODO: Connect to DB_FILE and query sqlite_master to print all table names.
# Expected output example:
#   Tables in database: ['students']


# ── Task 2: Query and filter student records ──────────────────────────────────
# TODO: Fetch and print ALL students from the students table.
# TODO: Fetch and print only students with grade = 'A'.
# Expected output example:
#   Alice — Grade: A
#   Carlos — Grade: A


# ── Task 3: Insert and verify a new student ───────────────────────────────────
# TODO: Insert a new student with a name and grade of your choice.
# TODO: Commit the change, then re-query and print all rows to confirm.

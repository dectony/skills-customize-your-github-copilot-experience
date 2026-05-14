# 📘 Assignment: Intro to SQL with SQLite

## 🎯 Objective

Learn the fundamentals of relational databases by querying and manipulating a SQLite database using Python's built-in `sqlite3` module. You will practice connecting to a database, reading data with SQL queries, and inserting new records.

## 📝 Tasks

### 🛠️ Connect to a Database and Explore the Schema

#### Description
Use Python's `sqlite3` module to open a database file and inspect the tables it contains.

#### Requirements
Completed program should:

- Import the `sqlite3` module and connect to `school.db`
- Query `sqlite_master` to retrieve and print the names of all tables in the database
- Close the connection cleanly after use

### 🛠️ Query and Filter Student Records

#### Description
Write SQL `SELECT` queries to retrieve student data from the `students` table, with and without filters.

#### Requirements
Completed program should:

- Fetch and print all rows from the `students` table
- Fetch and print only students whose `grade` is `'A'` using a `WHERE` clause
- Display each result as a readable line, e.g. `Alice — Grade: A`

### 🛠️ Insert and Verify a New Student

#### Description
Add a new student to the database using an `INSERT` statement and confirm the record was saved.

#### Requirements
Completed program should:

- Insert a new row into the `students` table with a name and grade of your choice
- Commit the transaction so the change is persisted
- Re-query the table and print all rows to confirm the new student appears

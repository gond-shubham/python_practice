# Python DB-API

This folder contains Python practice programs focused on database connectivity and database operations using Python's `sqlite3` module.

The purpose is to understand how Python applications communicate with databases, execute SQL queries, manage transactions and handle database-related exceptions.

## Topics Covered

### 1. Database Connection
- Connecting to a SQLite database using `sqlite3.connect()`
- Creating database connection objects
- Creating cursor objects
- Understanding the role of connection and cursor objects

### 2. Table Creation and Data Insertion
- Creating database tables using SQL queries
- Defining columns and data types
- Setting primary keys
- Inserting single and multiple records
- Using parameterized SQL queries

### 3. Retrieving Data
- Executing SELECT queries
- Retrieving all records using `fetchall()`
- Retrieving a single record using `fetchone()`
- Retrieving multiple records using `fetchmany()`
- Filtering records using WHERE conditions

### 4. Updating and Deleting Records
- Updating existing records using UPDATE
- Deleting records using DELETE
- Filtering records based on conditions
- Verifying database modifications

### 5. Transaction Management
- Understanding database transactions
- Saving changes using `commit()`
- Reverting changes using `rollback()`
- Understanding transaction behaviour

### 6. Resource Management
- Closing cursor objects
- Closing database connections
- Using context managers with database connections
- Understanding automatic resource management

### 7. Exception Handling
- Handling database-related exceptions
- Understanding `sqlite3.OperationalError`
- Understanding `sqlite3.IntegrityError`
- Handling duplicate primary keys
- Rolling back transactions when errors occur
- Using `try`, `except` and `finally` with database operations

### 8. Mini Project – Employee Management System

A small database-driven application implementing basic employee management operations:

- Add employees
- View employee records
- Update employee salaries
- Delete employee records
- Handle invalid operations and database errors

## Practice Approach

The programs progress from basic database connectivity to CRUD operations, transaction management and exception handling.

The focus is on understanding Python DB-API concepts through practical SQLite database operations.

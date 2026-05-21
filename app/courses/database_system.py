database_system_quiz = {
    "course_code": "BCP 105",
    "course_name": "Data Communication",
    "total_questions": 50,
    "questions": [
        
  
  
  
  
    {
        "id": 1,
        "type": "multiple_choice",
        "question": "What does INT represent in MySQL?",
        "options": [
            "Text",
            "Decimal number",
            "Whole number",
            "Date"
        ],
        "correct_answer": 2,
        "explanation": "INT stores whole numbers (integers) without decimal places."
    },
    {
        "id": 2,
        "type": "multiple_choice",
        "question": "Which data type stores text?",
        "options": [
            "DATE",
            "VARCHAR",
            "INT",
            "FLOAT"
        ],
        "correct_answer": 1,
        "explanation": "VARCHAR (Variable Character) stores text/string values."
    },
    {
        "id": 3,
        "type": "multiple_choice",
        "question": "AUTO_INCREMENT is used to:",
        "options": [
            "Delete data",
            "Automatically increase numbers",
            "Encrypt data",
            "Store text"
        ],
        "correct_answer": 1,
        "explanation": "AUTO_INCREMENT automatically generates a unique sequential number for each new row."
    },
    {
        "id": 4,
        "type": "multiple_choice",
        "question": "PRIMARY KEY must be:",
        "options": [
            "Duplicate",
            "Empty",
            "Unique",
            "Text only"
        ],
        "correct_answer": 2,
        "explanation": "A primary key uniquely identifies each row, so duplicate values are not allowed."
    },
    {
        "id": 5,
        "type": "multiple_choice",
        "question": "Which data type stores dates?",
        "options": [
            "DATE",
            "TEXT",
            "INT",
            "CHAR"
        ],
        "correct_answer": 0,
        "explanation": "The DATE data type stores calendar dates in YYYY-MM-DD format."
    },
    {
        "id": 6,
        "type": "multiple_choice",
        "question": "VARCHAR(50) means:",
        "options": [
            "50 numbers only",
            "50 characters max",
            "50 tables",
            "50 rows"
        ],
        "correct_answer": 1,
        "explanation": "The number in VARCHAR(50) is the maximum character length allowed."
    },
    {
        "id": 7,
        "type": "multiple_choice",
        "question": "NOT NULL means:",
        "options": [
            "Can be empty",
            "Must have value",
            "Must be number",
            "Must be duplicate"
        ],
        "correct_answer": 1,
        "explanation": "NOT NULL enforces that a column cannot contain NULL (empty/unknown) values."
    },
    {
        "id": 8,
        "type": "multiple_choice",
        "question": "Which command is used to view data?",
        "options": [
            "INSERT",
            "UPDATE",
            "SELECT",
            "DELETE"
        ],
        "correct_answer": 2,
        "explanation": "SELECT is the query command used to retrieve data from tables."
    },
    {
        "id": 9,
        "type": "multiple_choice",
        "question": "Which command adds new data?",
        "options": [
            "SELECT",
            "INSERT",
            "UPDATE",
            "DROP"
        ],
        "correct_answer": 1,
        "explanation": "INSERT adds new rows/records to a table."
    },
    {
        "id": 10,
        "type": "multiple_choice",
        "question": "Which command modifies existing data?",
        "options": [
            "INSERT",
            "SELECT",
            "UPDATE",
            "CREATE"
        ],
        "correct_answer": 2,
        "explanation": "UPDATE changes existing values in one or more rows."
    },
    {
        "id": 11,
        "type": "multiple_choice",
        "question": "Which command removes data?",
        "options": [
            "DELETE",
            "INSERT",
            "SELECT",
            "ALTER"
        ],
        "correct_answer": 0,
        "explanation": "DELETE removes rows from a table, but keeps the table structure."
    },
    {
        "id": 12,
        "type": "multiple_choice",
        "question": "FLOAT is used for:",
        "options": [
            "Text",
            "Whole numbers",
            "Decimal numbers",
            "Dates"
        ],
        "correct_answer": 2,
        "explanation": "FLOAT stores approximate numeric values with decimal points."
    },
    {
        "id": 13,
        "type": "multiple_choice",
        "question": "ENUM is used to:",
        "options": [
            "Store only fixed values",
            "Store images",
            "Store tables",
            "Store numbers only"
        ],
        "correct_answer": 0,
        "explanation": "ENUM restricts a column to a predefined list of allowed values."
    },
    {
        "id": 14,
        "type": "multiple_choice",
        "question": "DEFAULT CURRENT_DATE means:",
        "options": [
            "Random date",
            "Today's date automatically",
            "Future date",
            "Empty value"
        ],
        "correct_answer": 1,
        "explanation": "DEFAULT CURRENT_DATE automatically inserts the current date if no value is provided."
    },
    {
        "id": 15,
        "type": "multiple_choice",
        "question": "PRIMARY KEY allows:",
        "options": [
            "Duplicate values",
            "Null values",
            "Unique values only",
            "Text only"
        ],
        "correct_answer": 2,
        "explanation": "Primary keys enforce uniqueness and also cannot be NULL."
    },
    {
        "id": 16,
        "type": "multiple_choice",
        "question": "Which is NOT a SQL command?",
        "options": [
            "SELECT",
            "INSERT",
            "LOOP",
            "UPDATE"
        ],
        "correct_answer": 2,
        "explanation": "LOOP is a procedural programming concept, not a standard SQL command."
    },
    {
        "id": 17,
        "type": "multiple_choice",
        "question": "DECIMAL(5,2) means:",
        "options": [
            "5 total digits, 2 decimals",
            "2 total digits",
            "5 rows",
            "2 tables"
        ],
        "correct_answer": 0,
        "explanation": "DECIMAL(5,2) = 5 digits total, with 2 digits after the decimal point (e.g., 123.45)."
    },
    {
        "id": 18,
        "type": "multiple_choice",
        "question": "FOREIGN KEY is used to:",
        "options": [
            "Encrypt data",
            "Connect tables",
            "Delete tables",
            "Sort data"
        ],
        "correct_answer": 1,
        "explanation": "A foreign key links two tables by referencing the primary key of another table."
    },
    {
        "id": 19,
        "type": "multiple_choice",
        "question": "Which stores single character?",
        "options": [
            "CHAR",
            "TEXT",
            "INT",
            "DATE"
        ],
        "correct_answer": 0,
        "explanation": "CHAR(1) stores exactly one fixed-length character."
    },
    {
        "id": 20,
        "type": "multiple_choice",
        "question": "SQL stands for:",
        "options": [
            "Simple Query Language",
            "Structured Query Language",
            "Strong Question Language",
            "System Query Logic"
        ],
        "correct_answer": 1,
        "explanation": "SQL stands for Structured Query Language, used for managing relational databases."
    },
    {
        "id": 21,
        "type": "multiple_choice",
        "question": "SELECT * means:",
        "options": [
            "Select one column",
            "Select all columns",
            "Delete all data",
            "Insert all data"
        ],
        "correct_answer": 1,
        "explanation": "The asterisk (*) is shorthand for 'all columns' in the table."
    },
    {
        "id": 22,
        "type": "multiple_choice",
        "question": "WHERE is used to:",
        "options": [
            "Insert data",
            "Filter data",
            "Create table",
            "Drop table"
        ],
        "correct_answer": 1,
        "explanation": "WHERE filters rows based on specified conditions."
    },
    {
        "id": 23,
        "type": "multiple_choice",
        "question": "ORDER BY is used to:",
        "options": [
            "Delete data",
            "Sort data",
            "Insert data",
            "Connect tables"
        ],
        "correct_answer": 1,
        "explanation": "ORDER BY sorts query results in ascending or descending order."
    },
    {
        "id": 24,
        "type": "multiple_choice",
        "question": "LIMIT is used to:",
        "options": [
            "Increase rows",
            "Limit number of rows",
            "Delete rows",
            "Update rows"
        ],
        "correct_answer": 1,
        "explanation": "LIMIT restricts how many rows a query returns."
    },
    {
        "id": 25,
        "type": "multiple_choice",
        "question": "PRIMARY KEY cannot be:",
        "options": [
            "Unique",
            "Null",
            "Indexed",
            "Integer"
        ],
        "correct_answer": 1,
        "explanation": "Primary keys cannot contain NULL values — each row must have a value."
    },
    {
        "id": 26,
        "type": "multiple_choice",
        "question": "VARCHAR is better than CHAR when:",
        "options": [
            "Fixed length text",
            "Variable length text",
            "Numbers only",
            "Dates"
        ],
        "correct_answer": 1,
        "explanation": "VARCHAR saves space by using only the needed storage for variable-length strings."
    },
    {
        "id": 27,
        "type": "multiple_choice",
        "question": "INT stores:",
        "options": [
            "Decimal numbers",
            "Whole numbers",
            "Text",
            "Boolean only"
        ],
        "correct_answer": 1,
        "explanation": "INT stores whole numbers (no fractional part)."
    },
    {
        "id": 28,
        "type": "multiple_choice",
        "question": "A table is made up of:",
        "options": [
            "Columns only",
            "Rows and columns",
            "Files",
            "Folders"
        ],
        "correct_answer": 1,
        "explanation": "Tables are structured in rows (records) and columns (fields)."
    },
    {
        "id": 29,
        "type": "multiple_choice",
        "question": "A row in a table is also called:",
        "options": [
            "Column",
            "Record",
            "Database",
            "Field"
        ],
        "correct_answer": 1,
        "explanation": "In database terms, a row is often called a record or tuple."
    },
    {
        "id": 30,
        "type": "multiple_choice",
        "question": "A column is also called:",
        "options": [
            "Field",
            "Row",
            "Table",
            "Record"
        ],
        "correct_answer": 0,
        "explanation": "A column represents a field or attribute of an entity."
    },
    {
        "id": 31,
        "type": "multiple_choice",
        "question": "FOREIGN KEY connects:",
        "options": [
            "Same table only",
            "Two tables",
            "Three databases",
            "Two rows"
        ],
        "correct_answer": 1,
        "explanation": "Foreign keys create relationships between two tables (child and parent)."
    },
    {
        "id": 32,
        "type": "multiple_choice",
        "question": "UPDATE needs:",
        "options": [
            "WHERE clause",
            "SELECT clause",
            "DROP clause",
            "CREATE clause"
        ],
        "correct_answer": 0,
        "explanation": "Without WHERE, UPDATE changes all rows — WHERE limits which rows are updated."
    },
    {
        "id": 33,
        "type": "multiple_choice",
        "question": "If you forget WHERE in UPDATE:",
        "options": [
            "Only one row changes",
            "All rows may change",
            "Nothing happens",
            "Table is deleted"
        ],
        "correct_answer": 1,
        "explanation": "Omitting WHERE causes the update to apply to every row in the table."
    },
    {
        "id": 34,
        "type": "multiple_choice",
        "question": "DECIMAL is used for:",
        "options": [
            "Text",
            "Exact numbers",
            "Dates",
            "Tables"
        ],
        "correct_answer": 1,
        "explanation": "DECIMAL stores exact numeric values (e.g., money, precise decimals)."
    },
    {
        "id": 35,
        "type": "multiple_choice",
        "question": "AUTO_INCREMENT starts from:",
        "options": [
            "Random number",
            "1 by default",
            "1000 always",
            "0 only"
        ],
        "correct_answer": 1,
        "explanation": "By default, AUTO_INCREMENT starts at 1 and increments by 1 each time."
    },
    {
        "id": 36,
        "type": "multiple_choice",
        "question": "Which is NOT a data type?",
        "options": [
            "INT",
            "VARCHAR",
            "SELECT",
            "DATE"
        ],
        "correct_answer": 2,
        "explanation": "SELECT is a command/statement, not a data type."
    },
    {
        "id": 37,
        "type": "multiple_choice",
        "question": "Database is:",
        "options": [
            "A file",
            "A collection of tables",
            "A row",
            "A column"
        ],
        "correct_answer": 1,
        "explanation": "A database contains tables, views, indexes, etc., organized for data management."
    },
    {
        "id": 38,
        "type": "multiple_choice",
        "question": "SQL is mainly used for:",
        "options": [
            "Designing UI",
            "Managing databases",
            "Editing videos",
            "Programming games"
        ],
        "correct_answer": 1,
        "explanation": "SQL is the standard language for relational database management systems."
    },
    {
        "id": 39,
        "type": "multiple_choice",
        "question": "A NULL value means:",
        "options": [
            "Zero",
            "Empty/unknown",
            "False",
            "True"
        ],
        "correct_answer": 1,
        "explanation": "NULL represents missing or unknown data — not the same as 0 or empty string."
    },
    {
        "id": 40,
        "type": "multiple_choice",
        "question": "PRIMARY KEY is used to:",
        "options": [
            "Duplicate rows",
            "Identify rows uniquely",
            "Delete rows",
            "Sort rows"
        ],
        "correct_answer": 1,
        "explanation": "The primary key uniquely identifies each row in a table."
    },
    {
        "id": 41,
        "type": "multiple_choice",
        "question": "INSERT INTO is followed by:",
        "options": [
            "Columns and values",
            "Only values",
            "Only tables",
            "Only WHERE"
        ],
        "correct_answer": 0,
        "explanation": "Full syntax: INSERT INTO table (columns) VALUES (values). Columns optional if inserting all columns in order."
    },
    {
        "id": 42,
        "type": "multiple_choice",
        "question": "DELETE removes:",
        "options": [
            "Table structure",
            "Data rows",
            "Database",
            "Columns"
        ],
        "correct_answer": 1,
        "explanation": "DELETE removes rows; table structure remains. Use DROP to remove structure."
    },
    {
        "id": 43,
        "type": "multiple_choice",
        "question": "ALTER is used to:",
        "options": [
            "Change table structure",
            "Insert data",
            "Delete data",
            "Query data"
        ],
        "correct_answer": 0,
        "explanation": "ALTER modifies table definition (add/remove columns, change data types, etc.)."
    },
    {
        "id": 44,
        "type": "multiple_choice",
        "question": "A database table looks like:",
        "options": [
            "Excel sheet",
            "Video file",
            "Image",
            "Folder"
        ],
        "correct_answer": 0,
        "explanation": "Tables are structured in rows and columns, similar to an Excel spreadsheet."
    },
    {
        "id": 45,
        "type": "multiple_choice",
        "question": "ENUM allows:",
        "options": [
            "Any value",
            "Fixed set of values",
            "Random numbers",
            "Only text"
        ],
        "correct_answer": 1,
        "explanation": "ENUM defines a list of permissible values for a column."
    },
    {
        "id": 46,
        "type": "multiple_choice",
        "question": "SQL is:",
        "options": [
            "Programming language for databases",
            "Game engine",
            "Operating system",
            "Browser"
        ],
        "correct_answer": 0,
        "explanation": "SQL is a domain-specific language for managing relational databases."
    },
    {
        "id": 47,
        "type": "multiple_choice",
        "question": "CHAR differs from VARCHAR because:",
        "options": [
            "CHAR is fixed length",
            "VARCHAR is fixed",
            "Both are same",
            "CHAR is only numbers"
        ],
        "correct_answer": 0,
        "explanation": "CHAR allocates fixed storage; VARCHAR allocates only needed storage + 1 byte."
    },
    {
        "id": 48,
        "type": "multiple_choice",
        "question": "FOREIGN KEY must match:",
        "options": [
            "Any column",
            "Primary key in another table",
            "Random value",
            "NULL only"
        ],
        "correct_answer": 1,
        "explanation": "Foreign key references the primary key (or unique key) of another table."
    },
    {
        "id": 49,
        "type": "multiple_choice",
        "question": "SELECT * FROM students returns:",
        "options": [
            "Only names",
            "All columns and rows",
            "Only emails",
            "Only IDs"
        ],
        "correct_answer": 1,
        "explanation": "* means all columns; without WHERE, all rows are returned."
    },
    {
        "id": 50,
        "type": "multiple_choice",
        "question": "DROP TABLE means:",
        "options": [
            "Delete rows only",
            "Delete entire table",
            "Update table",
            "Insert table"
        ],
        "correct_answer": 1,
        "explanation": "DROP TABLE removes the table structure and all data permanently."
    },
    {
        "id": 51,
        "type": "multiple_choice",
        "question": "Which is used for sorting?",
        "options": [
            "ORDER BY",
            "WHERE",
            "INSERT",
            "CREATE"
        ],
        "correct_answer": 0,
        "explanation": "ORDER BY sorts results — ASC (default) or DESC."
    },
    {
        "id": 52,
        "type": "multiple_choice",
        "question": "Which keyword filters data?",
        "options": [
            "WHERE",
            "SELECT",
            "INSERT",
            "DROP"
        ],
        "correct_answer": 0,
        "explanation": "WHERE sets conditions that rows must meet to be included."
    },
    {
        "id": 53,
        "type": "multiple_choice",
        "question": "Database primary goal:",
        "options": [
            "Store structured data",
            "Show images",
            "Edit videos",
            "Run games"
        ],
        "correct_answer": 0,
        "explanation": "Databases store and retrieve structured data efficiently."
    },
    {
        "id": 54,
        "type": "multiple_choice",
        "question": "TEXT is used for:",
        "options": [
            "Long text",
            "Numbers",
            "Dates",
            "Boolean"
        ],
        "correct_answer": 0,
        "explanation": "TEXT is for long strings (e.g., paragraphs, articles) beyond VARCHAR limits."
    },
    {
        "id": 55,
        "type": "multiple_choice",
        "question": "A relationship between tables uses:",
        "options": [
            "PRIMARY KEY only",
            "FOREIGN KEY",
            "VARCHAR",
            "SELECT"
        ],
        "correct_answer": 1,
        "explanation": "Foreign keys define and enforce relationships between tables."
    },
    {
        "id": 56,
        "type": "multiple_choice",
        "question": "DEFAULT means:",
        "options": [
            "Required value",
            "Automatic value if not given",
            "Random value",
            "Empty only"
        ],
        "correct_answer": 1,
        "explanation": "DEFAULT supplies a value when no explicit value is provided in INSERT."
    },
    {
        "id": 57,
        "type": "multiple_choice",
        "question": "Which is faster for fixed size text?",
        "options": [
            "VARCHAR",
            "CHAR",
            "TEXT",
            "DATE"
        ],
        "correct_answer": 1,
        "explanation": "CHAR is faster for fixed-length data because storage is predictable."
    },
    {
        "id": 58,
        "type": "multiple_choice",
        "question": "SQL queries end with:",
        "options": [
            ";",
            ":",
            ".",
            ","
        ],
        "correct_answer": 0,
        "explanation": "The semicolon (;) is the standard statement terminator in SQL."
    },
    {
        "id": 59,
        "type": "multiple_choice",
        "question": "A database schema is:",
        "options": [
            "Table structure design",
            "Data values",
            "Output screen",
            "Query result"
        ],
        "correct_answer": 0,
        "explanation": "Schema defines tables, columns, data types, constraints, and relationships."
    },
    {
        "id": 60,
        "type": "multiple_choice",
        "question": "A good primary key should be:",
        "options": [
            "Duplicate",
            "Unique and stable",
            "Empty",
            "Text only"
        ],
        "correct_answer": 1,
        "explanation": "Primary keys should be unique, non-NULL, and rarely change (e.g., auto-increment ID)."
    },
    
    {
        "id": 61,
        "type": "multiple_choice",
        "question": "What happens if you run this? SELECT * FROM students WHERE 1 = 1;",
        "options": [
            "Returns no rows",
            "Returns all rows",
            "Deletes all data",
            "Causes error"
        ],
        "correct_answer": 1,
        "explanation": "1=1 is always true, so all rows are returned. This is sometimes used to bypass dynamic WHERE conditions."
    },
    {
        "id": 62,
        "type": "multiple_choice",
        "question": "What is the output of this? SELECT COUNT(*) FROM students;",
        "options": [
            "Total columns",
            "Total rows",
            "Student names",
            "Error"
        ],
        "correct_answer": 1,
        "explanation": "COUNT(*) returns the number of rows in the table (including rows with NULLs in any column)."
    },
    {
        "id": 63,
        "type": "multiple_choice",
        "question": "What happens if PRIMARY KEY is NOT defined?",
        "options": [
            "Table cannot be created",
            "Table works but no uniqueness rule",
            "Data is encrypted",
            "Only one row allowed"
        ],
        "correct_answer": 1,
        "explanation": "A table can exist without a primary key, but you lose the uniqueness constraint and faster lookups."
    },
    {
        "id": 64,
        "type": "multiple_choice",
        "question": "Which is TRUE about AUTO_INCREMENT?",
        "options": [
            "It resets every insert",
            "It generates duplicate values",
            "It generates unique numbers automatically",
            "It works only on VARCHAR"
        ],
        "correct_answer": 2,
        "explanation": "AUTO_INCREMENT generates a unique sequential number for each new row, typically starting from 1."
    },
    {
        "id": 65,
        "type": "multiple_choice",
        "question": "What happens if you forget WHERE in UPDATE? UPDATE students SET gender = 'Male';",
        "options": [
            "Only first row updates",
            "All rows update",
            "Error occurs",
            "Nothing happens"
        ],
        "correct_answer": 1,
        "explanation": "Without WHERE, every row in the table gets updated — this is a common and dangerous mistake."
    },
    {
        "id": 66,
        "type": "multiple_choice",
        "question": "Which query is correct?",
        "options": [
            "SELECT name FROM students WHERE;",
            "SELECT * students;",
            "SELECT * FROM students;",
            "GET * FROM students;"
        ],
        "correct_answer": 2,
        "explanation": "The correct syntax is SELECT column(s) FROM table_name; Options 1, 2, and 4 have syntax errors."
    },
    {
        "id": 67,
        "type": "multiple_choice",
        "question": "What is wrong here? INSERT INTO students VALUES ('John', 'Smith');",
        "options": [
            "Missing SELECT",
            "Missing column list",
            "Nothing wrong",
            "Missing WHERE"
        ],
        "correct_answer": 1,
        "explanation": "Technically this works if the table has exactly 2 columns and order matches. But best practice is to specify column names for clarity and safety."
    },
    {
        "id": 68,
        "type": "multiple_choice",
        "question": "What does this return? SELECT * FROM students LIMIT 1,3;",
        "options": [
            "First row only",
            "3 rows starting from second row",
            "1 row only",
            "All rows"
        ],
        "correct_answer": 1,
        "explanation": "LIMIT 1,3 means offset=1 (skip first row), then return up to 3 rows — so rows 2, 3, and 4."
    },
    {
        "id": 69,
        "type": "multiple_choice",
        "question": "FOREIGN KEY mainly ensures:",
        "options": [
            "Speed",
            "Data integrity",
            "Encryption",
            "Sorting"
        ],
        "correct_answer": 1,
        "explanation": "Foreign keys enforce referential integrity — you cannot insert a value that doesn't exist in the parent table."
    },
    {
        "id": 70,
        "type": "multiple_choice",
        "question": "If a foreign key value does not exist in parent table:",
        "options": [
            "It is accepted",
            "Error occurs",
            "Auto-created",
            "Ignored silently"
        ],
        "correct_answer": 1,
        "explanation": "The database will reject the insert/update with a foreign key constraint violation error."
    },
    {
        "id": 71,
        "type": "multiple_choice",
        "question": "Which is NOT a valid data type?",
        "options": [
            "INT",
            "VARCHAR",
            "SELECT",
            "DATE"
        ],
        "correct_answer": 2,
        "explanation": "SELECT is a SQL command/keyword, not a data type. The others are valid data types."
    },
    {
        "id": 72,
        "type": "multiple_choice",
        "question": "What does NULL mean?",
        "options": [
            "Zero",
            "Empty/unknown",
            "False",
            "Deleted"
        ],
        "correct_answer": 1,
        "explanation": "NULL means 'no value' or 'unknown' — it is not the same as 0, empty string, or false."
    },
    {
        "id": 73,
        "type": "multiple_choice",
        "question": "What happens if you insert NULL into NOT NULL column?",
        "options": [
            "Accepted",
            "Ignored",
            "Error",
            "Converted to zero"
        ],
        "correct_answer": 2,
        "explanation": "The NOT NULL constraint rejects any INSERT or UPDATE that attempts to set the column to NULL."
    },
    {
        "id": 74,
        "type": "multiple_choice",
        "question": "Which is correct primary key rule?",
        "options": [
            "Can repeat",
            "Must be unique",
            "Can be NULL",
            "Can be text only"
        ],
        "correct_answer": 1,
        "explanation": "Primary keys must contain unique values and cannot be NULL. They can be text, numbers, or other types."
    },
    {
        "id": 75,
        "type": "multiple_choice",
        "question": "What does this do? SELECT * FROM students ORDER BY first_name DESC;",
        "options": [
            "Ascending order",
            "Random order",
            "Descending order",
            "Deletes rows"
        ],
        "correct_answer": 2,
        "explanation": "ORDER BY ... DESC sorts results from highest to lowest (Z to A for text, largest to smallest for numbers)."
    },
    {
        "id": 76,
        "type": "multiple_choice",
        "question": "Which keyword filters records?",
        "options": [
            "WHERE",
            "SELECT",
            "ORDER BY",
            "INSERT"
        ],
        "correct_answer": 0,
        "explanation": "WHERE applies conditions to filter which rows are returned or affected."
    },
    {
        "id": 77,
        "type": "multiple_choice",
        "question": "What is output of COUNT(*) when table is empty?",
        "options": [
            "NULL",
            "1",
            "0",
            "Error"
        ],
        "correct_answer": 2,
        "explanation": "COUNT(*) returns 0 for an empty table — it never returns NULL."
    },
    {
        "id": 78,
        "type": "multiple_choice",
        "question": "Which is correct?",
        "options": [
            "SELECT * FROM students WHERE age = NULL;",
            "SELECT * FROM students WHERE age IS NULL;",
            "SELECT * FROM students WHERE age = 0;",
            "SELECT NULL FROM students;"
        ],
        "correct_answer": 1,
        "explanation": "NULL cannot be compared with = or !=. You must use IS NULL or IS NOT NULL."
    },
    {
        "id": 79,
        "type": "multiple_choice",
        "question": "VARCHAR differs from CHAR because:",
        "options": [
            "CHAR is variable",
            "VARCHAR is fixed",
            "VARCHAR is variable length",
            "Both same"
        ],
        "correct_answer": 2,
        "explanation": "VARCHAR uses only the space needed (plus 1-2 bytes overhead); CHAR uses fixed space regardless of actual content."
    },
    {
        "id": 80,
        "type": "multiple_choice",
        "question": "What happens if you run DROP TABLE students?",
        "options": [
            "Deletes rows only",
            "Deletes structure and data",
            "Clears columns only",
            "Updates table"
        ],
        "correct_answer": 1,
        "explanation": "DROP TABLE permanently removes both the table structure and all its data. Cannot be rolled back in most databases."
    },
    {
        "id": 81,
        "type": "multiple_choice",
        "question": "Which is DDL?",
        "options": [
            "SELECT",
            "INSERT",
            "CREATE",
            "UPDATE"
        ],
        "correct_answer": 2,
        "explanation": "DDL (Data Definition Language) includes CREATE, ALTER, DROP, TRUNCATE. SELECT/INSERT/UPDATE are DML."
    },
    {
        "id": 82,
        "type": "multiple_choice",
        "question": "Which is DML?",
        "options": [
            "CREATE",
            "ALTER",
            "SELECT",
            "DROP"
        ],
        "correct_answer": 2,
        "explanation": "DML (Data Manipulation Language) includes SELECT, INSERT, UPDATE, DELETE. CREATE/ALTER/DROP are DDL."
    },
    {
        "id": 83,
        "type": "multiple_choice",
        "question": "What does this return? SELECT 2 + 3;",
        "options": [
            "Error",
            "23",
            "5",
            "NULL"
        ],
        "correct_answer": 2,
        "explanation": "Many SQL dialects allow expressions without a FROM clause, returning the computed result (5)."
    },
    {
        "id": 84,
        "type": "multiple_choice",
        "question": "What is wrong here? SELECT * FROM students WHERE email = gmail.com;",
        "options": [
            "Missing quotes",
            "Wrong column",
            "Nothing wrong",
            "Missing SELECT"
        ],
        "correct_answer": 0,
        "explanation": "String values must be enclosed in quotes. gmail.com is interpreted as a column or variable name, not a string."
    },
    {
        "id": 85,
        "type": "multiple_choice",
        "question": "Correct version of question 84:",
        "options": [
            "email = \"gmail.com\"",
            "email = gmail.com",
            "email = 'gmail.com'",
            "email == gmail.com"
        ],
        "correct_answer": 2,
        "explanation": "Single quotes are standard SQL for string literals. Double quotes work in some databases but single is safest."
    },
    {
        "id": 86,
        "type": "multiple_choice",
        "question": "What does BETWEEN do?",
        "options": [
            "Deletes range",
            "Filters range",
            "Sorts data",
            "Joins tables"
        ],
        "correct_answer": 1,
        "explanation": "BETWEEN filters rows where a column's value falls within a specified inclusive range (e.g., WHERE age BETWEEN 18 AND 25)."
    },
    {
        "id": 87,
        "type": "multiple_choice",
        "question": "What happens if PRIMARY KEY is duplicated?",
        "options": [
            "Allowed",
            "Ignored",
            "Error",
            "Converted"
        ],
        "correct_answer": 2,
        "explanation": "A duplicate primary key violates the uniqueness constraint and causes an error."
    },
    {
        "id": 88,
        "type": "multiple_choice",
        "question": "Which is correct JOIN purpose?",
        "options": [
            "Delete tables",
            "Combine tables",
            "Encrypt tables",
            "Rename tables"
        ],
        "correct_answer": 1,
        "explanation": "JOINs combine rows from two or more tables based on a related column (often foreign key to primary key)."
    },
    {
        "id": 89,
        "type": "multiple_choice",
        "question": "What does this return? SELECT * FROM students WHERE 1=0;",
        "options": [
            "All rows",
            "No rows",
            "Error",
            "First row"
        ],
        "correct_answer": 1,
        "explanation": "1=0 is always false, so no rows are returned. This is sometimes used to create an empty result set with column structure."
    },
    {
        "id": 90,
        "type": "multiple_choice",
        "question": "Which one is correct syntax?",
        "options": [
            "SELECT FROM students *;",
            "SELECT * FROM students;",
            "GET * FROM students;",
            "SHOW students *;"
        ],
        "correct_answer": 1,
        "explanation": "The standard SELECT syntax is SELECT column_list FROM table_name;"
    },
    {
        "id": 91,
        "type": "multiple_choice",
        "question": "What does DISTINCT do?",
        "options": [
            "Duplicates data",
            "Removes duplicates",
            "Deletes table",
            "Sorts data"
        ],
        "correct_answer": 1,
        "explanation": "SELECT DISTINCT returns only unique rows, eliminating duplicate values from the result set."
    },
    {
        "id": 92,
        "type": "multiple_choice",
        "question": "Which is true about PRIMARY KEY?",
        "options": [
            "Can be multiple columns",
            "Always NULL",
            "Can duplicate",
            "Only text"
        ],
        "correct_answer": 0,
        "explanation": "A composite primary key uses two or more columns together to uniquely identify a row."
    },
    {
        "id": 93,
        "type": "multiple_choice",
        "question": "What happens if you INSERT wrong data type?",
        "options": [
            "Auto convert",
            "Error",
            "Ignore",
            "Delete row"
        ],
        "correct_answer": 1,
        "explanation": "Most databases will throw an error if you try to insert a value that doesn't match the column's data type."
    },
    {
        "id": 94,
        "type": "multiple_choice",
        "question": "What does LIKE do?",
        "options": [
            "Exact match only",
            "Pattern matching",
            "Deletes data",
            "Joins tables"
        ],
        "correct_answer": 1,
        "explanation": "LIKE allows wildcard pattern matching: % (any characters) and _ (single character)."
    },
    {
        "id": 95,
        "type": "multiple_choice",
        "question": "What does % mean in LIKE?",
        "options": [
            "Single character",
            "Any number of characters",
            "NULL",
            "One digit only"
        ],
        "correct_answer": 1,
        "explanation": "% matches zero or more characters. '_' matches exactly one character."
    },
    {
        "id": 96,
        "type": "multiple_choice",
        "question": "Which is correct?",
        "options": [
            "SELECT * FROM students WHERE name LIKE 'A%';",
            "SELECT * FROM students WHERE name = A%;",
            "SELECT * FROM students LIKE A%;",
            "SELECT LIKE name FROM students;"
        ],
        "correct_answer": 0,
        "explanation": "LIKE is used in the WHERE clause with quoted pattern strings. 'A%' means names starting with 'A'."
    },
    {
        "id": 97,
        "type": "multiple_choice",
        "question": "What is result of: SELECT 10/2;",
        "options": [
            "5",
            "2",
            "20",
            "Error"
        ],
        "correct_answer": 0,
        "explanation": "Basic arithmetic works in SQL SELECT statements. 10/2 equals 5."
    },
    {
        "id": 98,
        "type": "multiple_choice",
        "question": "What does ALTER TABLE do?",
        "options": [
            "Deletes table",
            "Changes structure",
            "Inserts data",
            "Selects data"
        ],
        "correct_answer": 1,
        "explanation": "ALTER TABLE modifies the table structure: add/drop columns, change data types, add constraints, etc."
    },
    {
        "id": 99,
        "type": "multiple_choice",
        "question": "Which is safest key to use?",
        "options": [
            "Name",
            "Email",
            "Auto-increment ID",
            "Gender"
        ],
        "correct_answer": 2,
        "explanation": "Auto-increment ID is safest because it never changes, is always unique, and has no business meaning that could become invalid."
    },
    {
        "id": 100,
        "type": "multiple_choice",
        "question": "What happens if you run: SELECT * FROM students;",
        "options": [
            "Deletes data",
            "Shows all data",
            "Updates table",
            "Creates table"
        ],
        "correct_answer": 1,
        "explanation": "SELECT * FROM students displays all rows and columns from the students table — a read-only operation."
    }







]
}
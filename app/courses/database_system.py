database_system_quiz = {
    "course_code": "BCP 105",
    "course_name": "Data Communication",
    "total_questions": 50,
    "questions": [
        
  
  
  
  
   
   
  
  {
    "id": 1,
    "type": "multiple_choice",
    "question": "A __________ is a software system that facilitates the definition, creation, maintenance, and control of access to databases.",
    "options": [
      "Operating System",
      "Database Management System (DBMS)",
      "Compiler",
      "Data Dictionary"
    ],
    "correct_answer": 1,
    "explanation": "A Database Management System (DBMS) is software that manages databases. An operating system manages hardware, a compiler translates code, and a data dictionary stores metadata."
  },
  {
    "id": 2,
    "type": "multiple_choice",
    "question": "The __________ level in the three-schema architecture describes how data is physically stored.",
    "options": [
      "External Level",
      "Conceptual Level",
      "Internal Level",
      "Logical Level"
    ],
    "correct_answer": 2,
    "explanation": "The Internal Level describes physical storage. External Level is user views, Conceptual Level is the community view, and Logical Level is another name for Conceptual."
  },
  {
    "id": 3,
    "type": "multiple_choice",
    "question": "The process of ensuring changes to the internal schema do not affect the conceptual schema is called __________.",
    "options": [
      "Logical Data Independence",
      "Data Consistency",
      "Physical Data Independence",
      "Data Redundancy"
    ],
    "correct_answer": 2,
    "explanation": "Physical Data Independence protects conceptual schema from internal schema changes. Logical Data Independence protects external views from conceptual changes."
  },
  {
    "id": 4,
    "type": "multiple_choice",
    "question": "The file-based system suffers from __________, where the same piece of data is stored in multiple files.",
    "options": [
      "Data Sharing",
      "Data Redundancy",
      "Data Security",
      "Data Recovery"
    ],
    "correct_answer": 1,
    "explanation": "Data Redundancy is the duplication of data in multiple files. Data Sharing is the opposite, Security protects data, and Recovery restores lost data."
  },
  {
    "id": 5,
    "type": "multiple_choice",
    "question": "The component responsible for ensuring data accuracy and consistency in a DBMS is known as __________.",
    "options": [
      "Data Integrity Constraints",
      "Query Processor",
      "Data Dictionary",
      "Transaction Manager"
    ],
    "correct_answer": 0,
    "explanation": "Data Integrity Constraints enforce accuracy and consistency. Query Processor handles queries, Data Dictionary stores metadata, and Transaction Manager manages transactions."
  },
  {
    "id": 6,
    "type": "multiple_choice",
    "question": "The component that describes the structure of the database, including entities, attributes, and relationships, is the __________.",
    "options": [
      "External Schema",
      "Internal Schema",
      "Conceptual Schema",
      "Data Model"
    ],
    "correct_answer": 2,
    "explanation": "Conceptual Schema describes the overall database structure. External Schema is user views, Internal Schema is physical storage, and Data Model is the theoretical framework."
  },
  {
    "id": 7,
    "type": "multiple_choice",
    "question": "In the DBMS environment, the people who implement the physical structure of the database and ensure performance are known as __________.",
    "options": [
      "System Analysts",
      "Programmers",
      "Database Administrators (DBA)",
      "Operators"
    ],
    "correct_answer": 2,
    "explanation": "Database Administrators (DBA) handle physical implementation and performance. System Analysts design systems, Programmers write code, and Operators manage hardware."
  },
  {
    "id": 8,
    "type": "multiple_choice",
    "question": "The __________ data model uses entities, attributes, and relationships to model the real world.",
    "options": [
      "Hierarchical",
      "Relational",
      "Network",
      "Entity-Relationship (ER)"
    ],
    "correct_answer": 3,
    "explanation": "ER Model uses entities, attributes, and relationships. Hierarchical uses tree structures, Relational uses tables, and Network uses graph structures."
  },
  {
    "id": 9,
    "type": "multiple_choice",
    "question": "The logical level in the ANSI-SPARC architecture is also known as the __________ view.",
    "options": [
      "Internal",
      "External",
      "Conceptual",
      "Physical"
    ],
    "correct_answer": 2,
    "explanation": "The Conceptual view is the logical level in ANSI-SPARC. Internal is physical, External is user view, and Physical is storage details."
  },
  {
    "id": 10,
    "type": "multiple_choice",
    "question": "Procedural DMLs specify both what data is needed and __________.",
    "options": [
      "Why it is needed",
      "When it is needed",
      "How to get it",
      "Where it is stored"
    ],
    "correct_answer": 2,
    "explanation": "Procedural DMLs specify what data is needed and how to get it. Nonprocedural DMLs only specify what data is needed."
  },
  {
    "id": 11,
    "type": "multiple_choice",
    "question": "In a two-tier client-server architecture, the client handles the __________ while the server manages the database.",
    "options": [
      "Storage Devices",
      "User Interface (Presentation)",
      "Data Files",
      "Network Cables"
    ],
    "correct_answer": 1,
    "explanation": "The client handles the user interface/presentation layer. The server handles database management. Storage, data files, and network are managed elsewhere."
  },
  {
    "id": 12,
    "type": "multiple_choice",
    "question": "A __________ in the relational model is a unique identifier that uniquely identifies each row in a table.",
    "options": [
      "Foreign Key",
      "Candidate Key",
      "Composite Key",
      "Primary Key"
    ],
    "correct_answer": 3,
    "explanation": "Primary Key uniquely identifies each row. Foreign Key references another table, Candidate Key is a potential primary key, and Composite Key uses multiple columns."
  },
  {
    "id": 13,
    "type": "multiple_choice",
    "question": "The architecture that separates business logic from database services and user interface is the __________ architecture.",
    "options": [
      "Two-Tier",
      "Client-Server",
      "Three-Tier",
      "Distributed"
    ],
    "correct_answer": 2,
    "explanation": "Three-Tier architecture separates presentation, business logic, and data services. Two-Tier combines presentation and business logic."
  },
  {
    "id": 14,
    "type": "multiple_choice",
    "question": "The __________ model represents data as tables composed of rows and columns.",
    "options": [
      "Network",
      "Relational",
      "Hierarchical",
      "Object-Oriented"
    ],
    "correct_answer": 1,
    "explanation": "The Relational model uses tables. Network uses graphs, Hierarchical uses trees, and Object-Oriented uses objects."
  },
  {
    "id": 15,
    "type": "multiple_choice",
    "question": "The concept in which no primary key attribute can be null is referred to as __________ integrity.",
    "options": [
      "Referential",
      "Domain",
      "Entity",
      "Functional"
    ],
    "correct_answer": 2,
    "explanation": "Entity Integrity ensures primary keys are non-null and unique. Referential Integrity ensures foreign keys match primary keys. Domain Integrity ensures valid values."
  },
  {
    "id": 16,
    "type": "multiple_choice",
    "question": "A foreign key must either match a candidate key in another table or be __________.",
    "options": [
      "Unique",
      "Indexed",
      "Valid",
      "Null"
    ],
    "correct_answer": 3,
    "explanation": "A foreign key can be NULL or match a candidate key. Unique and Indexed are not requirements, and Valid is vague."
  },
  {
    "id": 17,
    "type": "multiple_choice",
    "question": "Web services interact using a programmatic interface and do not require a __________.",
    "options": [
      "Browser",
      "Server",
      "GUI",
      "Database"
    ],
    "correct_answer": 2,
    "explanation": "Web services do not require a GUI (Graphical User Interface) as they use programmatic interfaces. They still require servers and may use databases."
  },
  {
    "id": 18,
    "type": "multiple_choice",
    "question": "In the relational model, a __________ is a set of allowable values for an attribute.",
    "options": [
      "Domain",
      "Tuple",
      "Relation",
      "Entity"
    ],
    "correct_answer": 0,
    "explanation": "Domain defines the set of allowable values for an attribute. Tuple is a row, Relation is a table, and Entity is a real-world object."
  },
  {
    "id": 19,
    "type": "multiple_choice",
    "question": "SOA is designed around services that are __________ and loosely coupled.",
    "options": [
      "Dependent",
      "Autonomous",
      "Temporary",
      "Sequential"
    ],
    "correct_answer": 1,
    "explanation": "SOA services are autonomous (independent) and loosely coupled. Dependent and sequential are incorrect, temporary is not a characteristic."
  },
  {
    "id": 20,
    "type": "multiple_choice",
    "question": "In the relational model, the set of all tuples in a relation at a given point in time is called its __________.",
    "options": [
      "Schema",
      "Degree",
      "Domain",
      "Instance"
    ],
    "correct_answer": 3,
    "explanation": "Instance is the set of tuples in a relation at a given time. Schema is the structure, Degree is number of columns, Domain is value sets."
  },
  {
    "id": 21,
    "type": "multiple_choice",
    "question": "The clause in an SQL SELECT statement used to sort query results is the __________ clause.",
    "options": [
      "GROUP BY",
      "HAVING",
      "ORDER BY",
      "FROM"
    ],
    "correct_answer": 2,
    "explanation": "ORDER BY sorts results. GROUP BY groups for aggregation, HAVING filters groups, and FROM specifies tables."
  },
  {
    "id": 22,
    "type": "multiple_choice",
    "question": "The SQL command used to remove records from a table is the __________ statement.",
    "options": [
      "DROP",
      "REMOVE",
      "ERASE",
      "DELETE"
    ],
    "correct_answer": 3,
    "explanation": "DELETE removes records (rows). DROP removes the entire table structure. REMOVE and ERASE are not standard SQL commands."
  },
  {
    "id": 23,
    "type": "multiple_choice",
    "question": "The keyword in a SELECT statement that removes duplicate records from the result set is __________.",
    "options": [
      "UNIQUE",
      "DISTINCT",
      "DIFFERENT",
      "FILTER"
    ],
    "correct_answer": 1,
    "explanation": "DISTINCT removes duplicates. UNIQUE is a constraint, DIFFERENT and FILTER are not SQL keywords for this purpose."
  },
  {
    "id": 24,
    "type": "multiple_choice",
    "question": "The aggregate function that returns the number of rows in a query is __________.",
    "options": [
      "SUM",
      "TOTAL",
      "COUNT",
      "NUMBER"
    ],
    "correct_answer": 2,
    "explanation": "COUNT returns the number of rows. SUM adds values, TOTAL is not standard SQL, NUMBER is not an aggregate function."
  },
  {
    "id": 25,
    "type": "multiple_choice",
    "question": "The GROUP BY clause is typically used in conjunction with __________ functions.",
    "options": [
      "String",
      "Aggregate",
      "Date",
      "Logical"
    ],
    "correct_answer": 1,
    "explanation": "GROUP BY is used with aggregate functions (COUNT, SUM, AVG, etc.). String, Date, and Logical functions are not grouping functions."
  },
  {
    "id": 26,
    "type": "multiple_choice",
    "question": "In SQL, the WHERE clause filters individual __________ before grouping.",
    "options": [
      "Columns",
      "Tables",
      "Rows",
      "Databases"
    ],
    "correct_answer": 2,
    "explanation": "WHERE filters individual rows before grouping. Columns are selected, tables are specified in FROM, databases are container objects."
  },
  {
    "id": 27,
    "type": "multiple_choice",
    "question": "The SQL clause used to filter grouped data is the __________ clause.",
    "options": [
      "WHERE",
      "ORDER BY",
      "HAVING",
      "GROUP BY"
    ],
    "correct_answer": 2,
    "explanation": "HAVING filters grouped data. WHERE filters individual rows, ORDER BY sorts, GROUP BY groups data."
  },
  {
    "id": 28,
    "type": "multiple_choice",
    "question": "To change data already in a table, the __________ statement is used in SQL.",
    "options": [
      "MODIFY",
      "CHANGE",
      "ALTER",
      "UPDATE"
    ],
    "correct_answer": 3,
    "explanation": "UPDATE modifies existing data. ALTER changes table structure, MODIFY and CHANGE are not standard SQL commands for data modification."
  },
  {
    "id": 29,
    "type": "multiple_choice",
    "question": "The __________ clause is used to specify the tables to be used in an SQL SELECT query.",
    "options": [
      "WHERE",
      "SELECT",
      "FROM",
      "HAVING"
    ],
    "correct_answer": 2,
    "explanation": "FROM specifies the tables. WHERE filters, SELECT specifies columns, HAVING filters groups."
  },
  {
    "id": 30,
    "type": "multiple_choice",
    "question": "In SQL, inserting new data into a table is done using the __________ statement.",
    "options": [
      "ADD",
      "APPEND",
      "CREATE",
      "INSERT"
    ],
    "correct_answer": 3,
    "explanation": "INSERT adds new data. CREATE makes new objects, ADD and APPEND are not standard SQL commands."
  },
  {
    "id": 31,
    "type": "multiple_choice",
    "question": "The process of organizing data to reduce redundancy and improve integrity is called __________.",
    "options": [
      "Validation",
      "Normalization",
      "Encryption",
      "Aggregation"
    ],
    "correct_answer": 1,
    "explanation": "Normalization organizes data to reduce redundancy. Validation checks data, Encryption protects data, Aggregation summarizes data."
  },
  {
    "id": 32,
    "type": "multiple_choice",
    "question": "A table is in Second Normal Form (2NF) if it is in 1NF and there are no __________ dependencies.",
    "options": [
      "Functional",
      "Transitive",
      "Partial",
      "Referential"
    ],
    "correct_answer": 2,
    "explanation": "2NF eliminates partial dependencies. 3NF eliminates transitive dependencies. Functional is the general type, Referential is for foreign keys."
  },
  {
    "id": 33,
    "type": "multiple_choice",
    "question": "A table is in Third Normal Form (3NF) if it is in 2NF and contains no __________ dependencies.",
    "options": [
      "Partial",
      "Composite",
      "Candidate",
      "Transitive"
    ],
    "correct_answer": 3,
    "explanation": "3NF eliminates transitive dependencies. Partial dependencies are eliminated in 2NF. Composite and Candidate are key types."
  },
  {
    "id": 34,
    "type": "multiple_choice",
    "question": "The type of dependency where a non-key attribute depends on another non-key attribute is known as a __________ dependency.",
    "options": [
      "Functional",
      "Partial",
      "Transitive",
      "Multivalued"
    ],
    "correct_answer": 2,
    "explanation": "Transitive dependency occurs when a non-key attribute depends on another non-key attribute. Partial is on part of a key, Functional is general."
  },
  {
    "id": 35,
    "type": "multiple_choice",
    "question": "A __________ constraint ensures that an attribute's value is not NULL.",
    "options": [
      "UNIQUE",
      "CHECK",
      "DEFAULT",
      "NOT NULL"
    ],
    "correct_answer": 3,
    "explanation": "NOT NULL prevents NULL values. UNIQUE ensures distinct values, CHECK validates conditions, DEFAULT provides default values."
  },
  {
    "id": 36,
    "type": "multiple_choice",
    "question": "The constraint that enforces unique values in a column or set of columns is the __________ constraint.",
    "options": [
      "PRIMARY KEY",
      "UNIQUE",
      "CHECK",
      "FOREIGN KEY"
    ],
    "correct_answer": 1,
    "explanation": "UNIQUE enforces unique values. PRIMARY KEY also enforces uniqueness but with NOT NULL. CHECK validates conditions, FOREIGN KEY enforces referential integrity."
  },
  {
    "id": 37,
    "type": "multiple_choice",
    "question": "A __________ is a column or combination of columns that uniquely identifies rows in a table.",
    "options": [
      "Foreign Key",
      "Candidate Key",
      "Primary Key",
      "Secondary Key"
    ],
    "correct_answer": 2,
    "explanation": "Primary Key uniquely identifies rows. Foreign Key references another table, Candidate Key is a potential primary key, Secondary Key is an index."
  },
  {
    "id": 38,
    "type": "multiple_choice",
    "question": "A __________ key in one table references a primary key in another table.",
    "options": [
      "Composite",
      "Candidate",
      "Alternate",
      "Foreign"
    ],
    "correct_answer": 3,
    "explanation": "Foreign Key references a primary key in another table. Composite uses multiple columns, Candidate is a potential key, Alternate is a non-primary candidate."
  },
  {
    "id": 39,
    "type": "multiple_choice",
    "question": "The SQL command CREATE TABLE is part of the __________ language.",
    "options": [
      "DML",
      "DQL",
      "DDL",
      "TCL"
    ],
    "correct_answer": 2,
    "explanation": "DDL (Data Definition Language) includes CREATE TABLE. DML manipulates data, DQL queries data, TCL manages transactions."
  },
  {
    "id": 40,
    "type": "multiple_choice",
    "question": "The concept of removing repeating groups in a table to reach First Normal Form (1NF) involves ensuring all attributes have __________ values.",
    "options": [
      "Duplicate",
      "Atomic",
      "Composite",
      "Derived"
    ],
    "correct_answer": 1,
    "explanation": "1NF requires atomic values (no repeating groups). Duplicate is opposite, Composite is combined, Derived is calculated."
  },
  {
    "id": 41,
    "type": "multiple_choice",
    "question": "The __________ clause is used to specify the tables to be used in an SQL SELECT query.",
    "options": [
      "WHERE",
      "HAVING",
      "ORDER BY",
      "FROM"
    ],
    "correct_answer": 3,
    "explanation": "FROM specifies the tables. WHERE filters rows, HAVING filters groups, ORDER BY sorts results."
  },
  {
    "id": 42,
    "type": "multiple_choice",
    "question": "A __________ dependency occurs when one attribute's value determines another's value.",
    "options": [
      "Partial",
      "Functional",
      "Transitive",
      "Referential"
    ],
    "correct_answer": 1,
    "explanation": "Functional dependency occurs when one attribute determines another. Partial is on part of a key, Transitive is through another attribute, Referential is between tables."
  },
  {
    "id": 43,
    "type": "multiple_choice",
    "question": "If every non-key attribute is fully functionally dependent on the primary key, the relation is in __________.",
    "options": [
      "1NF",
      "2NF",
      "3NF",
      "BCNF"
    ],
    "correct_answer": 1,
    "explanation": "2NF requires full functional dependency on the primary key. 1NF is atomic values, 3NF eliminates transitive dependencies, BCNF is stricter than 3NF."
  }




]
}
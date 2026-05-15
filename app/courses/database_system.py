database_system_quiz = {
    "course_code": "BCP 105",
    "course_name": "Data Communication",
    "total_questions": 50,
    "questions": [
        
  
  
  
  {
    "id": 1,
    "type": "multiple_choice",
    "question": "Raw facts such as numbers, characters, or symbols without context are called:",
    "options": [
      "Information",
      "Metadata",
      "Data",
      "Queries"
    ],
    "correct_answer": 2,
    "explanation": "Data is defined as raw, unprocessed facts without intrinsic meaning. Information is processed data, metadata is data about data, and queries are requests for data."
  },
  {
    "id": 2,
    "type": "multiple_choice",
    "question": "When data is organized, contextualized, and made meaningful, it becomes:",
    "options": [
      "A file",
      "Information",
      "A primary key",
      "Redundancy"
    ],
    "correct_answer": 1,
    "explanation": "Information is processed data that is organized, contextualized, and presented in a meaningful way, such as 'Student ID 45020 belongs to James Owusu'."
  },
  {
    "id": 3,
    "type": "multiple_choice",
    "question": "Which of the following best describes the transformation process from data to information?",
    "options": [
      "Deleting duplicate entries",
      "Processing and adding context",
      "Storing in multiple files",
      "Encrypting the data"
    ],
    "correct_answer": 1,
    "explanation": "Data becomes information when it is processed, organized, and given context, making it meaningful and useful for decision-making."
  },
  {
    "id": 4,
    "type": "multiple_choice",
    "question": "A student ID number alone is considered data, but 'Student ID 45020 belongs to James Owusu' is an example of:",
    "options": [
      "A database constraint",
      "Information",
      "A flat file",
      "A secondary key"
    ],
    "correct_answer": 1,
    "explanation": "The statement provides context and meaning to the raw number, transforming it from data into information."
  },
  {
    "id": 5,
    "type": "multiple_choice",
    "question": "File-based systems stored data primarily in:",
    "options": [
      "Relational tables",
      "Flat files like .txt, .csv, or .dat",
      "XML documents only",
      "Object-oriented databases"
    ],
    "correct_answer": 1,
    "explanation": "File-based systems stored data in flat files, typically in formats such as .txt, .csv, or .dat, not in relational or object-oriented structures."
  },
  {
    "id": 6,
    "type": "multiple_choice",
    "question": "In a file-based system, if the same customer address appears in both a billing file and a shipping file, this is an example of:",
    "options": [
      "Data independence",
      "Data redundancy",
      "Referential integrity",
      "Concurrency"
    ],
    "correct_answer": 1,
    "explanation": "Data redundancy means duplicate data entries are stored in multiple files, which was common in file-based systems."
  },
  {
    "id": 7,
    "type": "multiple_choice",
    "question": "Data inconsistency in file-based systems often results directly from:",
    "options": [
      "Too many indexes",
      "Lack of encryption",
      "Redundant data that is updated in one file but not others",
      "Excessive use of SQL"
    ],
    "correct_answer": 2,
    "explanation": "When the same data is stored redundantly across multiple files and an update occurs in only one file, inconsistency arises because other files still contain the old value."
  },
  {
    "id": 8,
    "type": "multiple_choice",
    "question": "Which of the following is a limitation of file-based systems mentioned in the slides?",
    "options": [
      "High scalability",
      "Excellent data sharing",
      "Limited security",
      "Built-in concurrency control"
    ],
    "correct_answer": 2,
    "explanation": "Limited security is explicitly listed as a critical limitation of file-based systems, which offered minimal access control mechanisms."
  },
  {
    "id": 9,
    "type": "multiple_choice",
    "question": "In file-based systems, accessing data from multiple files is difficult because:",
    "options": [
      "Files are always encrypted",
      "The application developer must manually synchronize processing",
      "SQL is not available",
      "There is no storage space"
    ],
    "correct_answer": 1,
    "explanation": "The application developer must synchronize processing of multiple files manually, and this difficulty compounds when more than two files are involved."
  },
  {
    "id": 10,
    "type": "multiple_choice",
    "question": "File-based systems were an early attempt to computerize:",
    "options": [
      "Network databases",
      "Manual filing systems",
      "Object-oriented storage",
      "Cloud storage"
    ],
    "correct_answer": 1,
    "explanation": "File-based systems were an early attempt to computerize the manual filing systems that organizations traditionally used to store correspondence and records."
  },
  {
    "id": 11,
    "type": "multiple_choice",
    "question": "A major problem with file-based systems is that updates in one file are not automatically reflected in other files, leading to:",
    "options": [
      "Faster access",
      "Data inconsistency",
      "Better security",
      "Less redundancy"
    ],
    "correct_answer": 1,
    "explanation": "When an update occurs in only one file but the same data exists elsewhere, the files become inconsistent with each other."
  },
  {
    "id": 12,
    "type": "multiple_choice",
    "question": "Which of the following is NOT a characteristic of a database according to the slides?",
    "options": [
      "Multiple departments may access it concurrently",
      "Data items are combined with little duplication",
      "It belongs to a single department only",
      "It includes operational data and its description"
    ],
    "correct_answer": 2,
    "explanation": "The slides state that the database is a common company resource rather than belonging to a single department."
  },
  {
    "id": 13,
    "type": "multiple_choice",
    "question": "A database is defined as a collection of interconnected records that:",
    "options": [
      "Require no maintenance",
      "Describe themselves",
      "Cannot be shared",
      "Are stored in flat files"
    ],
    "correct_answer": 1,
    "explanation": "The slides define a database as a collection of interconnected records that describe themselves, separating data definitions from application code."
  },
  {
    "id": 14,
    "type": "multiple_choice",
    "question": "The separation of data definitions from application code in a database is comparable to:",
    "options": [
      "File-based system indexing",
      "Current software development providing internal and external definitions for objects",
      "Manual filing cabinets",
      "Hard-coded data in programs"
    ],
    "correct_answer": 1,
    "explanation": "Database systems separate data definitions from application code, similar to how modern software development provides both internal and external definitions for objects."
  },
  {
    "id": 15,
    "type": "multiple_choice",
    "question": "Which language allows users to specify data types, structures, and constraints on data?",
    "options": [
      "DML",
      "DDL",
      "SQL (only for queries)",
      "Python"
    ],
    "correct_answer": 1,
    "explanation": "Data Definition Language (DDL) allows users to specify data types, structures, and constraints on the data to be stored in the database."
  },
  {
    "id": 16,
    "type": "multiple_choice",
    "question": "The DML (Data Manipulation Language) is primarily used for:",
    "options": [
      "Defining tables",
      "Inserting, updating, deleting, and retrieving data",
      "Setting hardware requirements",
      "Managing user logins"
    ],
    "correct_answer": 1,
    "explanation": "DML allows users to insert, update, delete, and retrieve data from the database."
  },
  {
    "id": 17,
    "type": "multiple_choice",
    "question": "The general inquiry facility provided by DML is called a:",
    "options": [
      "Data dictionary",
      "Query language",
      "Compiler",
      "Transaction manager"
    ],
    "correct_answer": 1,
    "explanation": "Having a central repository allows the DML to provide a general inquiry facility called a query language, with SQL being the most common example."
  },
  {
    "id": 18,
    "type": "multiple_choice",
    "question": "Which language is both the formal and de facto standard for relational DBMSs?",
    "options": [
      "Java",
      "C++",
      "SQL",
      "HTML"
    ],
    "correct_answer": 2,
    "explanation": "SQL (Structured Query Language) is both the formal and de facto standard language for relational DBMSs."
  },
  {
    "id": 19,
    "type": "multiple_choice",
    "question": "The DBMS advantage that ensures accuracy and consistency across the system is:",
    "options": [
      "Scalability",
      "Concurrency",
      "Data integrity",
      "Data redundancy"
    ],
    "correct_answer": 2,
    "explanation": "Data integrity ensures accuracy and consistency of data across the entire database system."
  },
  {
    "id": 20,
    "type": "multiple_choice",
    "question": "Role-based access control and authentication are features of which DBMS advantage?",
    "options": [
      "Scalability",
      "Security",
      "Data independence",
      "Concurrency"
    ],
    "correct_answer": 1,
    "explanation": "Security in DBMS includes role-based access control and authentication mechanisms."
  },
  {
    "id": 21,
    "type": "multiple_choice",
    "question": "The ability of a DBMS to allow simultaneous access without conflict is called:",
    "options": [
      "Data integrity",
      "Concurrency",
      "Security",
      "Scalability"
    ],
    "correct_answer": 1,
    "explanation": "Concurrency allows multiple users to access the database simultaneously without interfering with each other."
  },
  {
    "id": 22,
    "type": "multiple_choice",
    "question": "The DBMS advantage that supports large volumes of data and many users is:",
    "options": [
      "Data independence",
      "Concurrency",
      "Scalability",
      "Integrity"
    ],
    "correct_answer": 2,
    "explanation": "Scalability refers to the DBMS's ability to handle growing amounts of data and increasing numbers of users."
  },
  {
    "id": 23,
    "type": "multiple_choice",
    "question": "Insulation between application programs and data is known as:",
    "options": [
      "Data redundancy",
      "Data independence",
      "Concurrency",
      "Security"
    ],
    "correct_answer": 1,
    "explanation": "Data independence provides insulation between application programs and the data, allowing changes to data storage without affecting applications."
  },
  {
    "id": 24,
    "type": "multiple_choice",
    "question": "Which of the following is NOT one of the five major components in a DBMS environment?",
    "options": [
      "Hardware",
      "Software",
      "Compiler",
      "Procedures"
    ],
    "correct_answer": 2,
    "explanation": "The five major components are hardware, software, data, procedures, and people. Compiler is not listed as a separate component."
  },
  {
    "id": 25,
    "type": "multiple_choice",
    "question": "In the DBMS environment, hardware can range from:",
    "options": [
      "Only mainframes",
      "Personal computers to mainframes or networks",
      "Only personal computers",
      "Only mobile devices"
    ],
    "correct_answer": 1,
    "explanation": "Hardware requirements depend on the organization and DBMS used, ranging from personal computers to mainframes or networks."
  },
  {
    "id": 26,
    "type": "multiple_choice",
    "question": "Which component of the DBMS environment includes instructions on how to log on, start/stop the DBMS, and make backups?",
    "options": [
      "Hardware",
      "Software",
      "Data",
      "Procedures"
    ],
    "correct_answer": 3,
    "explanation": "Procedures refer to the instructions and rules governing database design and use, including login, startup/shutdown, and backup procedures."
  },
  {
    "id": 27,
    "type": "multiple_choice",
    "question": "Who is responsible for database planning, standards, policies, and conceptual/logical database design?",
    "options": [
      "Database Administrator (DBA)",
      "Data Administrator (DA)",
      "Application Developer",
      "End User"
    ],
    "correct_answer": 1,
    "explanation": "The Data Administrator (DA) is responsible for management of the data resource, including database planning, standards, policies, and conceptual/logical design."
  },
  {
    "id": 28,
    "type": "multiple_choice",
    "question": "The Database Administrator (DBA) is primarily responsible for:",
    "options": [
      "Writing application programs",
      "Physical database design, security, and performance",
      "Only logical design",
      "Using the database via menus"
    ],
    "correct_answer": 1,
    "explanation": "The DBA is responsible for physical database design and implementation, security, integrity control, maintenance, and ensuring satisfactory performance."
  },
  {
    "id": 29,
    "type": "multiple_choice",
    "question": "Which role is concerned with identifying entities, attributes, relationships, and business rules?",
    "options": [
      "Physical database designer",
      "Logical database designer",
      "Systems analyst",
      "Naive user"
    ],
    "correct_answer": 1,
    "explanation": "The logical database designer identifies entities, attributes, relationships, and constraints (business rules) on the data to be stored."
  },
  {
    "id": 30,
    "type": "multiple_choice",
    "question": "Constraints on data in logical database design are sometimes called:",
    "options": [
      "Storage rules",
      "Access paths",
      "Business rules",
      "Index definitions"
    ],
    "correct_answer": 2,
    "explanation": "Constraints on data in logical database design are sometimes called business rules."
  },
  {
    "id": 31,
    "type": "multiple_choice",
    "question": "Conceptual database design is:",
    "options": [
      "Dependent on the target DBMS",
      "Independent of implementation details",
      "Concerned with storage structures only",
      "The same as physical design"
    ],
    "correct_answer": 1,
    "explanation": "Conceptual database design is independent of implementation details such as the target DBMS, application programs, or programming languages."
  },
  {
    "id": 32,
    "type": "multiple_choice",
    "question": "Logical database design targets a specific data model such as:",
    "options": [
      "Only relational",
      "Relational, network, hierarchical, or object-oriented",
      "Only object-oriented",
      "Only flat files"
    ],
    "correct_answer": 1,
    "explanation": "Logical database design targets a specific data model, including relational, network, hierarchical, or object-oriented."
  },
  {
    "id": 33,
    "type": "multiple_choice",
    "question": "The physical database designer maps the logical design into:",
    "options": [
      "User interfaces",
      "A set of tables and integrity constraints",
      "Application source code",
      "Backup scripts"
    ],
    "correct_answer": 1,
    "explanation": "Physical database design involves mapping the logical database design into a set of tables and integrity constraints."
  },
  {
    "id": 34,
    "type": "multiple_choice",
    "question": "Selecting specific storage structures and access methods to achieve good performance is the job of:",
    "options": [
      "Logical database designer",
      "Physical database designer",
      "End user",
      "Data Administrator"
    ],
    "correct_answer": 1,
    "explanation": "The physical database designer selects specific storage structures and access methods for the data to achieve good performance."
  },
  {
    "id": 35,
    "type": "multiple_choice",
    "question": "Application developers typically work from a specification produced by:",
    "options": [
      "End users",
      "Systems analysts",
      "Database Administrator",
      "Hardware engineers"
    ],
    "correct_answer": 1,
    "explanation": "Application developers typically work from a specification produced by systems analysts."
  },
  {
    "id": 36,
    "type": "multiple_choice",
    "question": "Application programs contain statements that request the DBMS to perform operations including:",
    "options": [
      "Only data retrieval",
      "Only data insertion",
      "Retrieval, insertion, updating, and deletion",
      "Only data deletion"
    ],
    "correct_answer": 2,
    "explanation": "Each program contains statements requesting the DBMS to retrieve, insert, update, and delete data."
  },
  {
    "id": 37,
    "type": "multiple_choice",
    "question": "End users who are unaware of the DBMS and use simple commands or menus are called:",
    "options": [
      "Sophisticated users",
      "Naive users",
      "Database designers",
      "Systems analysts"
    ],
    "correct_answer": 1,
    "explanation": "Naive users are typically unaware of the DBMS and access the database through specially written application programs with simple commands or menus."
  },
  {
    "id": 38,
    "type": "multiple_choice",
    "question": "Which type of end user is familiar with the database structure and may write SQL queries?",
    "options": [
      "Naive user",
      "Sophisticated user",
      "Application developer",
      "Data Administrator"
    ],
    "correct_answer": 1,
    "explanation": "Sophisticated end users are familiar with the database structure and DBMS facilities, and may use high-level query languages like SQL."
  },
  {
    "id": 39,
    "type": "multiple_choice",
    "question": "Sophisticated end users may even write:",
    "options": [
      "Operating systems",
      "Application programs for their own use",
      "Database backup software",
      "Hardware drivers"
    ],
    "correct_answer": 1,
    "explanation": "Some sophisticated end users may write application programs for their own use."
  },
  {
    "id": 40,
    "type": "multiple_choice",
    "question": "Naive users invoke database operations by:",
    "options": [
      "Writing complex joins",
      "Entering simple commands or choosing menu options",
      "Designing table schemas",
      "Managing transactions"
    ],
    "correct_answer": 1,
    "explanation": "Naive users invoke database operations by entering simple commands or choosing options from a menu, without needing knowledge of the database or DBMS."
  },
  {
    "id": 41,
    "type": "multiple_choice",
    "question": "The central repository for all data and data descriptions allows the DML to provide a:",
    "options": [
      "Compiler",
      "Query language",
      "File system",
      "Hardware interface"
    ],
    "correct_answer": 1,
    "explanation": "Having a central repository allows the DML to provide a general inquiry facility called a query language."
  },
  {
    "id": 42,
    "type": "multiple_choice",
    "question": "Data redundancy in file-based systems commonly leads to:",
    "options": [
      "Improved performance",
      "Data inconsistency",
      "Better security",
      "Easier backups"
    ],
    "correct_answer": 1,
    "explanation": "Data redundancy leads to data inconsistency because updates in one file are not reflected in others."
  },
  {
    "id": 43,
    "type": "multiple_choice",
    "question": "Poor data sharing in file-based systems means accessing files often requires:",
    "options": [
      "Automatic synchronization",
      "Manual coordination",
      "SQL knowledge",
      "Network upgrades"
    ],
    "correct_answer": 1,
    "explanation": "Files were often isolated, and accessing them required manual coordination."
  },
  {
    "id": 44,
    "type": "multiple_choice",
    "question": "In a file-based system, if you need data from more than two files, the difficulty is:",
    "options": [
      "Reduced",
      "Compounded",
      "Eliminated",
      "Handled automatically by the OS"
    ],
    "correct_answer": 1,
    "explanation": "The difficulty is compounded if data is required from more than two files."
  },
  {
    "id": 45,
    "type": "multiple_choice",
    "question": "Which of the following is true about file-based systems?",
    "options": [
      "They offered excellent security controls",
      "They were an early attempt to computerize manual filing",
      "They automatically avoid data duplication",
      "They are still the standard for large organizations"
    ],
    "correct_answer": 1,
    "explanation": "File-based systems were an early attempt to computerize manual filing systems, though they suffered from limitations like data redundancy and poor security."
  },
  {
    "id": 46,
    "type": "multiple_choice",
    "question": "The database includes both operational data and its:",
    "options": [
      "Backup copy",
      "Description",
      "Encryption key",
      "File path"
    ],
    "correct_answer": 1,
    "explanation": "The database includes both operational data and its description (metadata)."
  },
  {
    "id": 47,
    "type": "multiple_choice",
    "question": "Which person is responsible for the physical realization of the database, including maintenance and performance?",
    "options": [
      "Data Administrator",
      "Database Administrator",
      "Logical designer",
      "End user"
    ],
    "correct_answer": 1,
    "explanation": "The Database Administrator (DBA) is responsible for physical database design, implementation, maintenance, and ensuring satisfactory performance."
  },
  {
    "id": 48,
    "type": "multiple_choice",
    "question": "Which person is responsible for the management of the data resource rather than the physical database?",
    "options": [
      "Database Administrator",
      "Data Administrator",
      "Application Developer",
      "Physical designer"
    ],
    "correct_answer": 1,
    "explanation": "The Data Administrator (DA) is responsible for management of the data resource, while the DBA handles physical implementation."
  },
  {
    "id": 49,
    "type": "multiple_choice",
    "question": "Procedures in the DBMS environment may include instructions on how to:",
    "options": [
      "Only write SQL",
      "Only design hardware",
      "Log on, use facilities, start/stop, and make backups",
      "Only compile programs"
    ],
    "correct_answer": 2,
    "explanation": "Procedures include instructions on logging on, using DBMS facilities, starting/stopping the DBMS, and making backup copies."
  },
  {
    "id": 50,
    "type": "multiple_choice",
    "question": "Which of the following is a role in the DBMS environment according to the slides?",
    "options": [
      "Network engineer",
      "Database designer",
      "Power supply manager",
      "Web designer"
    ],
    "correct_answer": 1,
    "explanation": "Database designer is explicitly listed as a role, along with data/database administrators, application developers, and end users."
  },
  {
    "id": 51,
    "type": "multiple_choice",
    "question": "The physical database designer also designs:",
    "options": [
      "Business rules",
      "Security measures on the data",
      "Conceptual models",
      "End-user training manuals"
    ],
    "correct_answer": 1,
    "explanation": "Physical database design includes designing any security measures required on the data."
  },
  {
    "id": 52,
    "type": "multiple_choice",
    "question": "A logical database designer must have a thorough understanding of:",
    "options": [
      "Storage hardware",
      "The organization's data and constraints",
      "Network protocols",
      "Compiler design"
    ],
    "correct_answer": 1,
    "explanation": "The logical database designer must have a thorough and complete understanding of the organization's data and any constraints (business rules)."
  },
  {
    "id": 53,
    "type": "multiple_choice",
    "question": "The quote 'A DBMS provides abstraction that hides complex storage details…' is attributed to:",
    "options": [
      "The slide author only",
      "Ullman & Widom (2022)",
      "The Database Administrator",
      "Microsoft"
    ],
    "correct_answer": 1,
    "explanation": "The quote is explicitly attributed to Ullman & Widom (2022) in the slides."
  },
  {
    "id": 54,
    "type": "multiple_choice",
    "question": "A DBMS requires a minimum amount of main memory and disk space, but this may not provide:",
    "options": [
      "Any functionality",
      "Acceptable performance",
      "Data storage capability",
      "User access"
    ],
    "correct_answer": 1,
    "explanation": "A DBMS requires minimum memory and disk space, but meeting only the minimum may not provide acceptable performance."
  },
  {
    "id": 55,
    "type": "multiple_choice",
    "question": "Which of the following is a responsibility of application developers?",
    "options": [
      "Physical database design",
      "Implementing application programs for end users",
      "Defining business rules",
      "Managing hardware"
    ],
    "correct_answer": 1,
    "explanation": "Application developers implement the application programs that provide required functionality for end users."
  },
  {
    "id": 56,
    "type": "multiple_choice",
    "question": "Application programs may be written in a third-generation or fourth-generation programming language. This suggests they are NOT typically written in:",
    "options": [
      "Java",
      "C++",
      "Machine code only",
      "Python"
    ],
    "correct_answer": 2,
    "explanation": "Third-generation (e.g., C, Java) and fourth-generation languages are used, not low-level machine code."
  },
  {
    "id": 57,
    "type": "multiple_choice",
    "question": "Which type of user does NOT need to know anything about the database or DBMS?",
    "options": [
      "Database Administrator",
      "Logical designer",
      "Naive user",
      "Sophisticated user"
    ],
    "correct_answer": 2,
    "explanation": "Naive users do not need to know anything about the database or DBMS; they access it through simple commands or menus."
  },
  {
    "id": 58,
    "type": "multiple_choice",
    "question": "The slides state that the database is a common company resource rather than belonging to:",
    "options": [
      "The IT department",
      "A single department",
      "External auditors",
      "The government"
    ],
    "correct_answer": 1,
    "explanation": "The database is a common company resource rather than belonging to a single department."
  },
  {
    "id": 59,
    "type": "multiple_choice",
    "question": "Which of the following is true about the DBMS environment?",
    "options": [
      "Hardware is irrelevant",
      "Data is the least important component",
      "Procedures include rules for database design and use",
      "People are optional"
    ],
    "correct_answer": 2,
    "explanation": "Procedures refer to the instructions and rules that govern the design and use of the database."
  },
  {
    "id": 60,
    "type": "multiple_choice",
    "question": "Which of these is NOT a type of end user classified in the slides?",
    "options": [
      "Naive users",
      "Sophisticated users",
      "Power users",
      "Both a and b are the only types mentioned"
    ],
    "correct_answer": 2,
    "explanation": "The slides classify end users into only two categories: naive users and sophisticated users. 'Power users' is not mentioned."
  }






]
}
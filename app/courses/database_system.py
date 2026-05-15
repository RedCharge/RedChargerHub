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
  },
  
  
    {
        "id": 61,
        "type": "multiple_choice",
        "question": "The three-schema architecture separates the database system into which three schemas?",
        "options": [
            "Physical, logical, view",
            "External, conceptual, internal",
            "Primary, secondary, tertiary",
            "User, program, system"
        ],
        "correct_answer": 1,
        "explanation": "The three-schema architecture consists of the external level (user views), conceptual level (logical structure), and internal level (physical storage)."
    },
    {
        "id": 62,
        "type": "multiple_choice",
        "question": "According to the slides, which level shows only the data relevant to each user and hides the rest?",
        "options": [
            "Internal level",
            "Conceptual level",
            "Physical level",
            "External level"
        ],
        "correct_answer": 3,
        "explanation": "The external level provides user-specific views of the database, showing only the data relevant to each user and hiding the rest."
    },
    {
        "id": 63,
        "type": "multiple_choice",
        "question": "The way the DBMS and the operating system perceive the data is called:",
        "options": [
            "External level",
            "User level",
            "Conceptual level",
            "Internal level"
        ],
        "correct_answer": 3,
        "explanation": "The internal level is how the DBMS and operating system perceive the data, dealing with physical storage structures."
    },
    {
        "id": 64,
        "type": "multiple_choice",
        "question": "The conceptual level provides both mapping and the desired independence between which two levels?",
        "options": [
            "Logical and physical",
            "User and system",
            "External and internal",
            "Program and data"
        ],
        "correct_answer": 2,
        "explanation": "The conceptual level provides mapping and independence between the external level (user views) and the internal level (physical storage)."
    },
    {
        "id": 65,
        "type": "multiple_choice",
        "question": "At the external level, some views may include calculated data that isn't stored in the database. This is created:",
        "options": [
            "During backup",
            "When needed",
            "Only at system startup",
            "By the operating system"
        ],
        "correct_answer": 1,
        "explanation": "Calculated data not stored in the database (like a student seeing their grades) is created when needed, not permanently stored."
    },
    {
        "id": 66,
        "type": "multiple_choice",
        "question": "The conceptual level is also known as the:",
        "options": [
            "Physical storage view",
            "User view",
            "Community view of the database",
            "Operating system view"
        ],
        "correct_answer": 2,
        "explanation": "The conceptual level is described as the 'community view' of the database, showing the entire logical structure as seen by DBAs and designers."
    },
    {
        "id": 67,
        "type": "multiple_choice",
        "question": "Which level defines all entities, attributes, relationships, constraints, and security rules?",
        "options": [
            "External level",
            "File level",
            "Internal level",
            "Conceptual level"
        ],
        "correct_answer": 3,
        "explanation": "The conceptual level defines all entities, attributes, relationships, constraints, and security rules, independent of storage details."
    },
    {
        "id": 68,
        "type": "multiple_choice",
        "question": "The internal level deals with all of the following EXCEPT:",
        "options": [
            "Indexing",
            "File structures",
            "User login credentials",
            "Space optimization for performance"
        ],
        "correct_answer": 2,
        "explanation": "User login credentials are related to security and authentication, not physical storage structures like file structures, indexing, or space optimization."
    },
    {
        "id": 69,
        "type": "multiple_choice",
        "question": "Below the internal level, the physical level is often handled by:",
        "options": [
            "The DBMS",
            "The operating system",
            "The application program",
            "The end user"
        ],
        "correct_answer": 1,
        "explanation": "Below the internal level, the physical level is often handled by the operating system, though the boundary between DBMS and OS varies across systems."
    },
    {
        "id": 70,
        "type": "multiple_choice",
        "question": "The overall description of the database divided into three levels is called the:",
        "options": [
            "Database instance",
            "Data dictionary",
            "Database schema",
            "Data model"
        ],
        "correct_answer": 2,
        "explanation": "The database schema is the overall description of the database, divided into external, conceptual, and internal schemas."
    },
    {
        "id": 71,
        "type": "multiple_choice",
        "question": "Which mapping connects the logical view with physical storage, allowing differences in names, order, or data types?",
        "options": [
            "External/internal mapping",
            "External/conceptual mapping",
            "Conceptual/internal mapping",
            "Logical/physical mapping"
        ],
        "correct_answer": 2,
        "explanation": "The conceptual/internal mapping connects the logical view with physical storage, allowing differences in names, order, or data types."
    },
    {
        "id": 72,
        "type": "multiple_choice",
        "question": "The data in the database at any particular point in time is called a:",
        "options": [
            "Database schema",
            "Data model",
            "Database instance",
            "Data dictionary"
        ],
        "correct_answer": 2,
        "explanation": "The data in the database at any particular point in time is called a database instance. Many instances can correspond to the same schema."
    },
    {
        "id": 73,
        "type": "multiple_choice",
        "question": "The schema is sometimes called the intension of the database, while an instance is called the:",
        "options": [
            "Snapshot",
            "Backup",
            "Extension or state",
            "Transaction log"
        ],
        "correct_answer": 2,
        "explanation": "The schema is called the intension; an instance is called the extension (or state) of the database."
    },
    {
        "id": 74,
        "type": "multiple_choice",
        "question": "Which type of data independence allows changes to the internal schema without affecting the conceptual schema?",
        "options": [
            "Logical data independence",
            "External data independence",
            "Structural data independence",
            "Physical data independence"
        ],
        "correct_answer": 3,
        "explanation": "Physical data independence is the ability to change the internal schema (e.g., file structures, indexing) without affecting the conceptual schema."
    },
    {
        "id": 75,
        "type": "multiple_choice",
        "question": "Physical data independence changes are usually made to:",
        "options": [
            "Add new users",
            "Change business rules",
            "Improve performance or efficiency",
            "Modify external views"
        ],
        "correct_answer": 2,
        "explanation": "Changes under physical data independence (e.g., new file structures, indexing methods) are usually made to improve performance or efficiency."
    },
    {
        "id": 76,
        "type": "multiple_choice",
        "question": "Which of the following is an example of a change possible under physical data independence?",
        "options": [
            "Adding a new entity",
            "Using a new indexing method",
            "Changing a user's view",
            "Modifying a relationship"
        ],
        "correct_answer": 1,
        "explanation": "Using a new indexing method is a physical change that does not affect the conceptual schema, demonstrating physical data independence."
    },
    {
        "id": 77,
        "type": "multiple_choice",
        "question": "A data sublanguage includes DDL and DML. Why are they called sublanguages?",
        "options": [
            "They are spoken languages",
            "They lack full programming features like loops or conditionals",
            "They can only be used by administrators",
            "They are not stored in the database"
        ],
        "correct_answer": 1,
        "explanation": "DDL and DML are called sublanguages because they lack full programming features like loops or conditionals."
    },
    {
        "id": 78,
        "type": "multiple_choice",
        "question": "When DDL statements are compiled, they generate metadata stored in the:",
        "options": [
            "User directory",
            "Transaction log",
            "System catalog (data dictionary)",
            "Buffer pool"
        ],
        "correct_answer": 2,
        "explanation": "DDL compilation generates metadata stored in the system catalog (also called data dictionary or data director), which describes all database objects."
    },
    {
        "id": 79,
        "type": "multiple_choice",
        "question": "Which language can create or modify the database schema but cannot manipulate data?",
        "options": [
            "DML",
            "4GL",
            "DDL",
            "SQL (all forms)"
        ],
        "correct_answer": 2,
        "explanation": "DDL (Data Definition Language) is used to define and modify the database schema but cannot manipulate data. DML handles data manipulation."
    },
    {
        "id": 80,
        "type": "multiple_choice",
        "question": "Procedural DML tells the system:",
        "options": [
            "What data is needed",
            "How to get the data step by step",
            "Only to insert data",
            "Only to delete data"
        ],
        "correct_answer": 1,
        "explanation": "Procedural DML tells the system how to get the data step by step, often embedded in host languages like C or Java."
    },
    {
        "id": 81,
        "type": "multiple_choice",
        "question": "Nonprocedural DML tells the system:",
        "options": [
            "How to get the data step by step",
            "What data is needed, not how to get it",
            "To ignore performance",
            "To use only indexes"
        ],
        "correct_answer": 1,
        "explanation": "Nonprocedural DML tells the system what data is needed, not how to get it. SQL and QBE are examples."
    },
    {
        "id": 82,
        "type": "multiple_choice",
        "question": "Which type of DML offers better data independence and is easier to learn?",
        "options": [
            "Procedural DML",
            "Embedded DML",
            "Nonprocedural DML",
            "Host language DML"
        ],
        "correct_answer": 2,
        "explanation": "Nonprocedural DMLs are easier to learn and offer better data independence compared to procedural DML."
    },
    {
        "id": 83,
        "type": "multiple_choice",
        "question": "Fourth-Generation Languages (4GLs) are:",
        "options": [
            "Procedural languages like C",
            "Machine languages",
            "Nonprocedural languages designed for quick application development",
            "Assembly languages"
        ],
        "correct_answer": 2,
        "explanation": "4GLs are high-level, nonprocedural languages designed to help users develop applications more quickly and easily than 3GLs like C or COBOL."
    },
    {
        "id": 84,
        "type": "multiple_choice",
        "question": "4GLs aim to boost productivity especially for:",
        "options": [
            "Operating system development",
            "Compiler design",
            "Database and business applications",
            "Device drivers"
        ],
        "correct_answer": 2,
        "explanation": "4GLs aim to boost productivity especially for database and business applications, not low-level systems programming."
    },
    {
        "id": 85,
        "type": "multiple_choice",
        "question": "Which of the following is listed as a type of 4GL tool?",
        "options": [
            "Debugger",
            "Query & Report Generators",
            "Assembler",
            "Linker"
        ],
        "correct_answer": 1,
        "explanation": "Query and Report Generators are listed as a type of 4GL tool, allowing users to ask questions and format output from data."
    },
    {
        "id": 86,
        "type": "multiple_choice",
        "question": "According to the slides, which of these is NOT listed as a 4GL tool?",
        "options": [
            "Forms Generators",
            "Graphics Generators",
            "Compiler Generators",
            "Application Generators"
        ],
        "correct_answer": 2,
        "explanation": "Forms Generators, Graphics Generators, and Application Generators are listed. Compiler Generators are not mentioned as a 4GL tool."
    },
    {
        "id": 87,
        "type": "multiple_choice",
        "question": "A data model is described as a high-level abstract description that acts like a:",
        "options": [
            "Compiler",
            "Blueprint",
            "Operating system",
            "File system"
        ],
        "correct_answer": 1,
        "explanation": "A data model is like a blueprint that helps people understand and communicate the structure and rules of the data."
    },
    {
        "id": 88,
        "type": "multiple_choice",
        "question": "Which of the following is a main component of a data model according to the slides?",
        "options": [
            "Compilation rules",
            "Integrity constraints",
            "Memory allocation",
            "Network protocols"
        ],
        "correct_answer": 1,
        "explanation": "The main components of a data model are Structure, Manipulation, and Integrity Constraints."
    },
    {
        "id": 89,
        "type": "multiple_choice",
        "question": "The three broad categories of data models mentioned are:",
        "options": [
            "Physical, logical, abstract",
            "Object-based, record-based, and physical",
            "Hierarchical, network, relational",
            "Conceptual, logical, internal"
        ],
        "correct_answer": 1,
        "explanation": "The three broad categories of data models are object-based, record-based, and physical data models."
    },
    {
        "id": 90,
        "type": "multiple_choice",
        "question": "In object-based data models, a real-world object like a person or product is called an:",
        "options": [
            "Attribute",
            "Relationship",
            "Entity",
            "Record"
        ],
        "correct_answer": 2,
        "explanation": "An entity is a real-world object (e.g., a person, product, or place) that you want to store data about."
    },
    {
        "id": 91,
        "type": "multiple_choice",
        "question": "A property of an entity, such as a person's name or age, is called an:",
        "options": [
            "Entity",
            "Relationship",
            "Instance",
            "Attribute"
        ],
        "correct_answer": 3,
        "explanation": "An attribute is a property of an entity, such as a person's name, age, or ID."
    },
    {
        "id": 92,
        "type": "multiple_choice",
        "question": "Which of the following is a type of object-based data model listed in the slides?",
        "options": [
            "Relational",
            "Network",
            "Entity-Relationship (ER)",
            "Hierarchical"
        ],
        "correct_answer": 2,
        "explanation": "Entity-Relationship (ER) is listed as a type of object-based data model, along with Semantic, Functional, and Object-oriented."
    },
    {
        "id": 93,
        "type": "multiple_choice",
        "question": "Record-based data models organize data as:",
        "options": [
            "Objects with methods",
            "Fixed-format structures with fields",
            "Free text",
            "Unstructured files"
        ],
        "correct_answer": 1,
        "explanation": "Record-based data models organize data as records — fixed-format structures with fields. Each record type defines what fields exist and their format."
    },
    {
        "id": 94,
        "type": "multiple_choice",
        "question": "Which of the following is a type of record-based data model?",
        "options": [
            "Object-oriented",
            "Functional",
            "Relational",
            "Semantic"
        ],
        "correct_answer": 2,
        "explanation": "The Relational data model is a type of record-based model, along with Network and Hierarchical models."
    },
    {
        "id": 95,
        "type": "multiple_choice",
        "question": "Physical data models focus on:",
        "options": [
            "What data looks like",
            "Business rules",
            "How data is stored and accessed for performance",
            "User views only"
        ],
        "correct_answer": 2,
        "explanation": "Physical data models describe how data is actually stored, structured, organized, and accessed for performance and storage efficiency."
    },
    {
        "id": 96,
        "type": "multiple_choice",
        "question": "Which of the following is a key aspect of physical data models?",
        "options": [
            "Entity definitions",
            "Access paths like indexes and pointers",
            "User permissions",
            "Forms and reports"
        ],
        "correct_answer": 1,
        "explanation": "Access paths such as indexes, pointers, and links are key aspects of physical data models used to find and retrieve data quickly."
    },
    {
        "id": 97,
        "type": "multiple_choice",
        "question": "Conceptual modeling is the process of creating a model:",
        "options": [
            "Dependent on a specific DBMS",
            "Without worrying about how data is stored or processed by a specific system",
            "Focused only on indexes",
            "That includes all programming details"
        ],
        "correct_answer": 1,
        "explanation": "Conceptual modeling creates a high-level abstract model without worrying about storage or processing by a specific system."
    },
    {
        "id": 98,
        "type": "multiple_choice",
        "question": "The conceptual schema connects:",
        "options": [
            "Two external schemas",
            "User views (external schemas) to physical storage (internal schema)",
            "Two internal schemas",
            "Only the DDL and DML"
        ],
        "correct_answer": 1,
        "explanation": "The conceptual schema is the core that connects user views (external schemas) to physical storage (internal schema)."
    },
    {
        "id": 99,
        "type": "multiple_choice",
        "question": "According to the conceptual vs. logical model table, the conceptual model focuses on:",
        "options": [
            "Tables and keys",
            "Normalization rules",
            "Business data requirements",
            "DBMS-specific features"
        ],
        "correct_answer": 2,
        "explanation": "The conceptual model focuses on business data requirements, while the logical model focuses on data structure in a specific DBMS."
    },
    {
        "id": 100,
        "type": "multiple_choice",
        "question": "In the conceptual vs. logical model table, which model depends on a specific DBMS (e.g., relational model)?",
        "options": [
            "Conceptual model",
            "Physical model",
            "Logical model",
            "External model"
        ],
        "correct_answer": 2,
        "explanation": "The logical model depends on a specific DBMS (e.g., relational model), while the conceptual model is independent of any system."
    },
    {
        "id": 101,
        "type": "multiple_choice",
        "question": "The logical model is described as having a level of abstraction that is:",
        "options": [
            "Highest-level",
            "Independent of any system",
            "Intermediate (between conceptual and physical)",
            "Lowest-level"
        ],
        "correct_answer": 2,
        "explanation": "The logical model has an intermediate level of abstraction, sitting between the conceptual and physical models."
    },
    {
        "id": 102,
        "type": "multiple_choice",
        "question": "Which of the following is included in a conceptual model but NOT typically in a logical model according to the table?",
        "options": [
            "Tables",
            "Entities and relationships",
            "Normalization rules",
            "Keys"
        ],
        "correct_answer": 1,
        "explanation": "Entities and relationships are included in the conceptual model. Tables, keys, and normalization rules are features of the logical model."
    },
    {
        "id": 103,
        "type": "multiple_choice",
        "question": "A good conceptual model ensures:",
        "options": [
            "Fast query performance",
            "Nothing is left out or wrongly defined",
            "Storage is minimized",
            "Indexes are created"
        ],
        "correct_answer": 1,
        "explanation": "A good conceptual model ensures nothing is left out or wrongly defined, accurately representing the enterprise's data requirements."
    },
    {
        "id": 104,
        "type": "multiple_choice",
        "question": "The internal schema details include all of the following EXCEPT:",
        "options": [
            "Record structures",
            "Indexes",
            "User passwords",
            "Storage methods"
        ],
        "correct_answer": 2,
        "explanation": "User passwords are security-related and belong to external or conceptual level concerns, not physical storage details like record structures, indexes, or storage methods."
    },
    {
        "id": 105,
        "type": "multiple_choice",
        "question": "The slide titled 'Three-level architecture Diagram' appears between which two topics?",
        "options": [
            "Introduction and External Level",
            "Conceptual Level and Internal Level",
            "External Level and Conceptual Level",
            "Schemas and Data Independence"
        ],
        "correct_answer": 0,
        "explanation": "The three-level architecture diagram appears between the introduction of the three-schema architecture and the detailed explanation of the External Level."
    },
    {
        "id": 106,
        "type": "multiple_choice",
        "question": "According to the slides, many database instances can correspond to:",
        "options": [
            "Many different schemas",
            "Only one external schema",
            "The same database schema",
            "No schema"
        ],
        "correct_answer": 2,
        "explanation": "Many database instances can correspond to the same database schema. The schema is the intension; instances are extensions."
    },
    {
        "id": 107,
        "type": "multiple_choice",
        "question": "The boundary between DBMS and OS responsibilities at the physical level can:",
        "options": [
            "Never change",
            "Only be set by the user",
            "Vary across systems",
            "Be ignored"
        ],
        "correct_answer": 2,
        "explanation": "The boundary between DBMS and OS responsibilities at the physical level can vary across different systems."
    },
    {
        "id": 108,
        "type": "multiple_choice",
        "question": "DML operates at all schema levels but focuses on ease of use at:",
        "options": [
            "Internal level",
            "Lower levels",
            "Higher levels",
            "Physical level"
        ],
        "correct_answer": 2,
        "explanation": "DML operates at all schema levels but focuses on ease of use at higher levels (external and conceptual)."
    },
    {
        "id": 109,
        "type": "multiple_choice",
        "question": "The query language is the part of DML used for:",
        "options": [
            "Defining tables",
            "Inserting data",
            "Retrieving data",
            "Deleting data"
        ],
        "correct_answer": 2,
        "explanation": "The query language is the part of DML used specifically for retrieving data from the database."
    },
    {
        "id": 110,
        "type": "multiple_choice",
        "question": "Which of the following is an example of a nonprocedural DML mentioned in the slides?",
        "options": [
            "C with embedded SQL",
            "COBOL",
            "QBE (Query by Example)",
            "Assembly"
        ],
        "correct_answer": 2,
        "explanation": "QBE (Query by Example) is explicitly mentioned as an example of a nonprocedural DML alongside SQL."
    },
    {
        "id": 111,
        "type": "multiple_choice",
        "question": "4GLs are much shorter and faster to use than:",
        "options": [
            "SQL",
            "3GLs like COBOL",
            "Query generators",
            "Spreadsheets"
        ],
        "correct_answer": 1,
        "explanation": "4GLs are much shorter and faster to use than 3GLs like COBOL, aiming to boost productivity for database and business applications."
    },
    {
        "id": 112,
        "type": "multiple_choice",
        "question": "Which of the following is listed as a 'Very High-Level Language' under 4GL tools?",
        "options": [
            "C++",
            "Java",
            "Abstract tools for generating applications",
            "Assembly"
        ],
        "correct_answer": 2,
        "explanation": "Under 4GL tools, 'Very High-Level Languages' are described as abstract tools for generating applications with minimal input."
    },
    {
        "id": 113,
        "type": "multiple_choice",
        "question": "According to the slides, which data model category includes the Relational, Network, and Hierarchical models?",
        "options": [
            "Object-based",
            "Physical",
            "Record-based",
            "Conceptual"
        ],
        "correct_answer": 2,
        "explanation": "The Relational, Network, and Hierarchical models are all types of record-based data models."
    },
    {
        "id": 114,
        "type": "multiple_choice",
        "question": "In the three-schema architecture, which level avoids storage details like memory size or file format?",
        "options": [
            "Internal level",
            "External level",
            "Conceptual level",
            "Physical level"
        ],
        "correct_answer": 2,
        "explanation": "The conceptual level avoids any storage details like memory size or file format, focusing only on logical structure."
    },
    {
        "id": 115,
        "type": "multiple_choice",
        "question": "The slide 'Differences between the three levels' appears immediately before which topic?",
        "options": [
            "Schemas, Mappings, and Instances",
            "Data Independence",
            "Physical data independence",
            "Conceptual Modeling"
        ],
        "correct_answer": 1,
        "explanation": "The slide 'Differences between the three levels' appears immediately before the topic 'Data Independence'."
    },
    {
        "id": 116,
        "type": "multiple_choice",
        "question": "Which mapping connects user views to the conceptual schema?",
        "options": [
            "Conceptual/internal mapping",
            "External/internal mapping",
            "External/conceptual mapping",
            "Logical/physical mapping"
        ],
        "correct_answer": 2,
        "explanation": "The external/conceptual mapping connects user views (external schemas) to the conceptual schema."
    },
    {
        "id": 117,
        "type": "multiple_choice",
        "question": "When DDL statements are compiled, the resulting metadata is sometimes called a:",
        "options": [
            "Transaction log",
            "Data dictionary or data director",
            "Query plan",
            "Buffer manager"
        ],
        "correct_answer": 1,
        "explanation": "The metadata generated by DDL compilation is stored in the system catalog, sometimes called a data dictionary or data director."
    },
    {
        "id": 118,
        "type": "multiple_choice",
        "question": "Procedural DML is often embedded in which types of languages?",
        "options": [
            "4GLs only",
            "SQL only",
            "High-level host languages like C or Java",
            "HTML"
        ],
        "correct_answer": 2,
        "explanation": "Procedural DML is often embedded in high-level programming languages (like C, C++, Java, or Python) which act as host languages."
    },
    {
        "id": 119,
        "type": "multiple_choice",
        "question": "The conceptual model is independent of:",
        "options": [
            "Business rules",
            "Entities and relationships",
            "DBMS and physical storage details",
            "Integrity constraints"
        ],
        "correct_answer": 2,
        "explanation": "The conceptual model is independent of DBMS, programming languages, and any physical storage details."
    },
    {
        "id": 120,
        "type": "multiple_choice",
        "question": "The slide 'Data independence Diagram' comes after the explanation of:",
        "options": [
            "Logical data independence",
            "Both logical and physical data independence",
            "Physical data independence",
            "Schemas and mappings"
        ],
        "correct_answer": 1,
        "explanation": "The 'Data independence Diagram' appears after the explanation of both logical and physical data independence."
    }







]
}
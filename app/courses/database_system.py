database_system_quiz = {
    "course_code": "BCP 105",
    "course_name": "Data Communication",
    "total_questions": 50,
    "questions": [
        
  
  
  
  
   
  {
    "id": 1,
    "type": "multiple_choice",
    "question": "A database is:",
    "options": [
      "Software designed to define, create, maintain, and control access to databases.",
      "A collection of interconnected records that describe themselves.",
      "Raw, unprocessed facts such as numbers and symbols.",
      "A collection of application programs that perform services for end-users."
    ],
    "correct_answer": 1,
    "explanation": "A database is a shared collection of related data. The first option describes a DBMS, the third describes data, and the fourth describes a file-based system."
  },
  {
    "id": 2,
    "type": "multiple_choice",
    "question": "Data refers to:",
    "options": [
      "Processed data organized into meaningful information.",
      "A collection of related records.",
      "Raw, unprocessed facts that have no intrinsic meaning.",
      "Information used for decision-making."
    ],
    "correct_answer": 2,
    "explanation": "Data means raw, unprocessed facts. The first and last options describe information, and the second describes a file or record collection."
  },
  {
    "id": 3,
    "type": "multiple_choice",
    "question": "Information is:",
    "options": [
      "Processed data that is organized and meaningful.",
      "A collection of application programs.",
      "A language used to query databases.",
      "Duplicate copies of data."
    ],
    "correct_answer": 0,
    "explanation": "Information is data that has been processed to become meaningful. The second option describes a file-based system, the third is SQL, and the fourth is data redundancy."
  },
  {
    "id": 4,
    "type": "multiple_choice",
    "question": "A Database Management System (DBMS) is:",
    "options": [
      "A collection of interconnected records.",
      "Software designed to define, create, maintain, and control access to databases.",
      "Raw data stored in files.",
      "A procedure used to log into a system."
    ],
    "correct_answer": 1,
    "explanation": "A DBMS is the software that manages databases. The first option describes a database itself, the third describes file-based data, and the fourth is a login procedure."
  },
  {
    "id": 5,
    "type": "multiple_choice",
    "question": "Which of the following is a major limitation of file-based systems?",
    "options": [
      "Data Integrity",
      "Data Independence",
      "Data Redundancy",
      "Concurrency"
    ],
    "correct_answer": 2,
    "explanation": "File-based systems suffer from uncontrolled duplicate data. The other three are actually advantages of DBMS, not limitations of file systems."
  },
  {
    "id": 6,
    "type": "multiple_choice",
    "question": "Data redundancy means:",
    "options": [
      "Duplicate data entries exist in multiple locations.",
      "Data is protected from unauthorized access.",
      "Data is processed into information.",
      "Users can access data simultaneously."
    ],
    "correct_answer": 0,
    "explanation": "Redundancy means the same data is stored in multiple places. The second is security, the third is data processing, and the fourth is concurrency."
  },
  {
    "id": 7,
    "type": "multiple_choice",
    "question": "Data inconsistency occurs when:",
    "options": [
      "Data is stored in tables.",
      "Updates in one file are not reflected in others.",
      "Security controls are applied.",
      "Data is backed up regularly."
    ],
    "correct_answer": 1,
    "explanation": "Inconsistency happens when you update one file but not another copy. Storing in tables is good, security and backup prevent problems, not cause them."
  },
  {
    "id": 8,
    "type": "multiple_choice",
    "question": "Which language is used to define data structures and constraints?",
    "options": ["SQL", "DML", "DDL", "DBMS"],
    "correct_answer": 2,
    "explanation": "DDL (Data Definition Language) defines the structure. SQL is a query language, DML manipulates data, and DBMS is the system itself."
  },
  {
    "id": 9,
    "type": "multiple_choice",
    "question": "DML is mainly used to:",
    "options": [
      "Define database structures.",
      "Insert, update, delete, and retrieve data.",
      "Design hardware.",
      "Create security policies."
    ],
    "correct_answer": 1,
    "explanation": "DML (Data Manipulation Language) works with the actual data. Defining structures is DDL, hardware design and security policies are different roles."
  },
  {
    "id": 10,
    "type": "multiple_choice",
    "question": "SQL is:",
    "options": [
      "A hardware component.",
      "A file-based system.",
      "The most common query language used in relational DBMSs.",
      "A type of database administrator."
    ],
    "correct_answer": 2,
    "explanation": "SQL is the standard language for relational databases. It is not hardware, not a file system, and not a person (DBA)."
  },
  {
    "id": 11,
    "type": "multiple_choice",
    "question": "Which of the following is an advantage of a DBMS?",
    "options": [
      "Data Inconsistency",
      "Poor Data Sharing",
      "Data Integrity",
      "Data Redundancy"
    ],
    "correct_answer": 2,
    "explanation": "Data integrity (accuracy and consistency) is a DBMS advantage. The other three are problems that DBMS fixes."
  },
  {
    "id": 12,
    "type": "multiple_choice",
    "question": "Data Integrity ensures:",
    "options": [
      "Duplicate records are created.",
      "Accuracy and consistency of data.",
      "Data is stored in separate files.",
      "Data is hidden from users."
    ],
    "correct_answer": 1,
    "explanation": "Data integrity means your data is accurate and consistent. Duplicates are bad, separate files are old-fashioned, hiding data is security."
  },
  {
    "id": 13,
    "type": "multiple_choice",
    "question": "Concurrency means:",
    "options": [
      "Multiple users can access data simultaneously without conflict.",
      "Data is duplicated in many files.",
      "Data is stored physically on disks.",
      "Data is converted into information."
    ],
    "correct_answer": 0,
    "explanation": "Concurrency allows many users at the same time without messing up each other's work. Duplication is redundancy, storage is physical, conversion is processing."
  },
  {
    "id": 14,
    "type": "multiple_choice",
    "question": "Data Independence means:",
    "options": [
      "Data is independent of electricity.",
      "Data can be shared between departments.",
      "Application programs are insulated from changes in data.",
      "Data does not need security."
    ],
    "correct_answer": 2,
    "explanation": "Data independence means changing how data is stored doesn't break your applications. Sharing is different, and data always needs security."
  },
  {
    "id": 15,
    "type": "multiple_choice",
    "question": "Which is NOT one of the five DBMS environment components?",
    "options": ["Hardware", "Software", "Procedures", "Internet"],
    "correct_answer": 3,
    "explanation": "The five components are Hardware, Software, Data, Procedures, and People. The Internet is not one of them."
  },
  {
    "id": 16,
    "type": "multiple_choice",
    "question": "The five major DBMS environment components are:",
    "options": [
      "Hardware, Software, Data, Procedures, People",
      "Hardware, Security, SQL, Data, People",
      "Software, Queries, Files, Data, People",
      "Hardware, Tables, Data, SQL, Users"
    ],
    "correct_answer": 0,
    "explanation": "The correct five are Hardware, Software, Data, Procedures, and People. Security, SQL, files, and tables are parts of those components, not separate ones."
  },
  {
    "id": 17,
    "type": "multiple_choice",
    "question": "The component that contains the DBMS, operating system, and application programs is:",
    "options": ["Data", "Software", "Procedures", "Hardware"],
    "correct_answer": 1,
    "explanation": "The Software component includes the DBMS, operating system, and applications. Data is the stored information, procedures are rules, hardware is physical devices."
  },
  {
    "id": 18,
    "type": "multiple_choice",
    "question": "Procedures refer to:",
    "options": [
      "Raw facts stored in the database.",
      "Instructions and rules governing the use of the database.",
      "Application programs written by developers.",
      "Hardware devices used by the DBMS."
    ],
    "correct_answer": 1,
    "explanation": "Procedures are the instructions and rules like how to log in or make backups. Raw facts are data, programs are software, devices are hardware."
  },
  {
    "id": 19,
    "type": "multiple_choice",
    "question": "The Data Administrator (DA) is responsible for:",
    "options": [
      "Database planning, policies, standards, and procedures.",
      "Writing application programs.",
      "Running SQL queries.",
      "Designing storage structures."
    ],
    "correct_answer": 0,
    "explanation": "The DA handles the big-picture planning, policies, and standards. Writing programs is for developers, SQL is for users, storage design is for the DBA."
  },
  {
    "id": 20,
    "type": "multiple_choice",
    "question": "The Database Administrator (DBA) is responsible for:",
    "options": [
      "Physical database implementation, security, and performance.",
      "Defining business rules only.",
      "Writing reports for end-users.",
      "Developing operating systems."
    ],
    "correct_answer": 0,
    "explanation": "The DBA handles the technical side: implementing, securing, and tuning the database. Business rules are for designers, reports for users, OS for system developers."
  },
  {
    "id": 21,
    "type": "multiple_choice",
    "question": "The logical database designer focuses on:",
    "options": [
      "Storage structures and access methods.",
      "Entities, attributes, relationships, and constraints.",
      "Security implementation.",
      "Hardware installation."
    ],
    "correct_answer": 1,
    "explanation": "Logical design is about 'what' – entities, attributes, relationships. Storage and access are physical design, security and hardware are other roles."
  },
  {
    "id": 22,
    "type": "multiple_choice",
    "question": "The physical database designer is responsible for:",
    "options": [
      "Identifying entities and attributes.",
      "Developing policies.",
      "Determining how the database is physically stored.",
      "Training end-users."
    ],
    "correct_answer": 2,
    "explanation": "Physical design is about 'how' – storage, indexing, etc. Identifying entities is logical design, policies are for DA, training is for procedures."
  },
  {
    "id": 23,
    "type": "multiple_choice",
    "question": "Which of the following is part of conceptual database design?",
    "options": [
      "Selecting storage devices.",
      "Choosing indexing methods.",
      "Designing independently of implementation details.",
      "Installing a DBMS."
    ],
    "correct_answer": 2,
    "explanation": "Conceptual design ignores implementation details. Storage devices and indexing are physical design, installation is a DBA task."
  },
  {
    "id": 24,
    "type": "multiple_choice",
    "question": "Application developers are responsible for:",
    "options": [
      "Writing programs that interact with the database.",
      "Managing database policies.",
      "Designing hardware.",
      "Maintaining physical storage."
    ],
    "correct_answer": 0,
    "explanation": "Application developers write the programs that use the database. Policies are for DA, hardware and storage are for engineers and DBA."
  },
  {
    "id": 25,
    "type": "multiple_choice",
    "question": "A naïve user is someone who:",
    "options": [
      "Understands SQL and database structures.",
      "Uses specially written programs and menus without DBMS knowledge.",
      "Designs databases.",
      "Maintains database security."
    ],
    "correct_answer": 1,
    "explanation": "A naïve user has no DBMS knowledge and uses menus/forms. Understanding SQL is a sophisticated user, design and security are professional roles."
  },
  {
    "id": 26,
    "type": "multiple_choice",
    "question": "A sophisticated user:",
    "options": [
      "Uses only menus.",
      "Has no knowledge of databases.",
      "Understands database structures and may use SQL.",
      "Is responsible for hardware maintenance."
    ],
    "correct_answer": 2,
    "explanation": "A sophisticated user understands database structure and can use SQL. Menus only is for naïve users, hardware maintenance is for IT staff."
  },
  {
    "id": 27,
    "type": "multiple_choice",
    "question": "Which statement best describes a database?",
    "options": [
      "It belongs to one department only.",
      "It minimizes duplication and can be shared by many users.",
      "It stores only processed information.",
      "It is a collection of operating systems."
    ],
    "correct_answer": 1,
    "explanation": "A database minimizes duplication and is shared. Belonging to one department is a file-based system, it stores raw and processed data, not operating systems."
  },
  {
    "id": 28,
    "type": "multiple_choice",
    "question": "Which problem of file-based systems makes data sharing difficult?",
    "options": [
      "Poor Data Sharing",
      "Data Integrity",
      "Concurrency",
      "Scalability"
    ],
    "correct_answer": 0,
    "explanation": "File-based systems literally have 'poor data sharing' as a problem. Integrity, concurrency, and scalability are also issues, but sharing difficulty is directly poor data sharing."
  },
  {
    "id": 29,
    "type": "multiple_choice",
    "question": "Which DBMS advantage allows the system to support large numbers of users and data?",
    "options": ["Security", "Scalability", "Data Integrity", "Procedures"],
    "correct_answer": 1,
    "explanation": "Scalability means growing to handle more users and data. Security protects data, integrity ensures accuracy, procedures are rules."
  },
  {
    "id": 30,
    "type": "multiple_choice",
    "question": "The ultimate purpose of a DBMS is to:",
    "options": [
      "Transform data into meaningful information.",
      "Increase data redundancy.",
      "Replace operating systems.",
      "Eliminate users."
    ],
    "correct_answer": 0,
    "explanation": "A DBMS turns raw data into useful information. It reduces redundancy, works with operating systems, and serves users."
  },
  {
    "id": 31,
    "type": "multiple_choice",
    "question": "Which statement best defines a file-based system?",
    "options": [
      "Software designed to define and control access to databases.",
      "A collection of application programs that perform services for end-users.",
      "A collection of interconnected records that describe themselves.",
      "A central repository of organizational data."
    ],
    "correct_answer": 1,
    "explanation": "A file-based system is a collection of application programs for end-users. The first option is a DBMS, the third and fourth describe a database."
  },
  {
    "id": 32,
    "type": "multiple_choice",
    "question": "Why is it useful to study file-based systems even though they are largely obsolete?",
    "options": [
      "They are faster than DBMSs.",
      "They help us understand problems that database systems were designed to solve.",
      "They eliminate redundancy.",
      "They are used in all modern organizations."
    ],
    "correct_answer": 1,
    "explanation": "Studying file-based systems shows us the problems (redundancy, inconsistency) that databases were created to fix. They are not faster, don't eliminate redundancy, and are not widely used today."
  },
  {
    "id": 33,
    "type": "multiple_choice",
    "question": "Which of the following is NOT a characteristic of a database?",
    "options": [
      "Shared organizational resource.",
      "Minimal duplication of data.",
      "Accessible by several users concurrently.",
      "Separate duplicate files maintained by departments."
    ],
    "correct_answer": 3,
    "explanation": "Separate duplicate files is a file-based system. A database is shared, has minimal duplication, and supports concurrent access."
  },
  {
    "id": 34,
    "type": "multiple_choice",
    "question": "Which DBMS facility allows users to specify data types and constraints?",
    "options": ["DML", "SQL", "DDL", "DBA"],
    "correct_answer": 2,
    "explanation": "DDL (Data Definition Language) specifies data types and constraints. DML manipulates data, SQL includes both but DDL is the specific facility, DBA is a person."
  },
  {
    "id": 35,
    "type": "multiple_choice",
    "question": "Which operation is performed using DML?",
    "options": ["CREATE", "ALTER", "SELECT", "DEFINE"],
    "correct_answer": 2,
    "explanation": "SELECT is a DML operation (retrieving data). CREATE, ALTER, and DEFINE are DDL operations for defining structure."
  },
  {
    "id": 36,
    "type": "multiple_choice",
    "question": "The most common query language used in relational databases is:",
    "options": ["Java", "SQL", "COBOL", "Pascal"],
    "correct_answer": 1,
    "explanation": "SQL is the standard query language for relational databases. Java, COBOL, and Pascal are general programming languages."
  },
  {
    "id": 37,
    "type": "multiple_choice",
    "question": "Which DBMS advantage hides complex storage details from users?",
    "options": ["Data Redundancy", "Abstraction", "Poor Data Sharing", "File Synchronization"],
    "correct_answer": 1,
    "explanation": "Abstraction hides storage complexity. Data redundancy is a problem, poor data sharing is a file-system problem, file synchronization is not a DBMS advantage."
  },
  {
    "id": 38,
    "type": "multiple_choice",
    "question": "Which component serves as the bridge between machine and human components in a DBMS environment?",
    "options": ["Hardware", "Data", "Procedures", "Software"],
    "correct_answer": 3,
    "explanation": "Software (DBMS, OS, apps) bridges hardware (machines) and people/procedures (humans). Data is passive, procedures are on the human side."
  },
  {
    "id": 39,
    "type": "multiple_choice",
    "question": "Which component contains instructions such as how to log on, make backups, and start or stop the DBMS?",
    "options": ["Data", "Procedures", "Hardware", "Security"],
    "correct_answer": 1,
    "explanation": "Procedures contain the instructions and rules. Data is facts, hardware is physical devices, security is a feature not a component."
  },
  {
    "id": 40,
    "type": "multiple_choice",
    "question": "Which of the following is considered hardware in a DBMS environment?",
    "options": ["SQL", "Database tables", "Servers and storage devices", "User manuals"],
    "correct_answer": 2,
    "explanation": "Hardware includes physical devices like servers and storage. SQL is a language, tables are data structures, user manuals are procedures."
  },
  {
    "id": 41,
    "type": "multiple_choice",
    "question": "The Data Administrator is mainly concerned with:",
    "options": [
      "Physical implementation of databases.",
      "Security and performance tuning.",
      "Database planning, standards, and policies.",
      "Writing application programs."
    ],
    "correct_answer": 2,
    "explanation": "The DA handles planning, standards, and policies. Physical implementation and tuning are the DBA's job, writing programs is for developers."
  },
  {
    "id": 42,
    "type": "multiple_choice",
    "question": "The Database Administrator is mainly concerned with:",
    "options": [
      "Conceptual database design.",
      "Physical realization of the database.",
      "Collecting business requirements.",
      "Writing reports."
    ],
    "correct_answer": 1,
    "explanation": "The DBA handles the physical implementation. Conceptual design is for logical designers, requirements are for analysts, reports are for users."
  },
  {
    "id": 43,
    "type": "multiple_choice",
    "question": "Which professional identifies entities, attributes, and relationships?",
    "options": ["DBA", "Application Developer", "Logical Database Designer", "End User"],
    "correct_answer": 2,
    "explanation": "The logical database designer identifies entities, attributes, and relationships. DBA does physical work, developers write code, end users use the system."
  },
  {
    "id": 44,
    "type": "multiple_choice",
    "question": "Business rules are another name for:",
    "options": ["Constraints", "Queries", "Procedures", "Transactions"],
    "correct_answer": 0,
    "explanation": "Business rules are constraints on the data. Queries retrieve data, procedures are instructions, transactions are units of work."
  },
  {
    "id": 45,
    "type": "multiple_choice",
    "question": "Which stage of database design is independent of implementation details?",
    "options": [
      "Physical Database Design",
      "Application Design",
      "Conceptual Database Design",
      "Security Design"
    ],
    "correct_answer": 2,
    "explanation": "Conceptual design ignores how the database will be physically built. Physical design depends on implementation, application design depends on both."
  },
  {
    "id": 46,
    "type": "multiple_choice",
    "question": "The physical database designer is responsible for:",
    "options": [
      "Identifying entities.",
      "Determining storage structures and access methods.",
      "Defining organizational policies.",
      "Writing SQL reports for users."
    ],
    "correct_answer": 1,
    "explanation": "Physical design means deciding storage structures and access methods. Identifying entities is logical design, policies are for DA, reports are for users."
  },
  {
    "id": 47,
    "type": "multiple_choice",
    "question": "Application developers usually work from specifications produced by:",
    "options": ["End Users", "Database Designers", "Systems Analysts", "Data Administrators"],
    "correct_answer": 2,
    "explanation": "Systems analysts produce specifications. End users give requirements, designers design the schema, DA handles policies."
  },
  {
    "id": 48,
    "type": "multiple_choice",
    "question": "Which database operation may be requested by an application program?",
    "options": ["Retrieve data", "Insert data", "Update data", "All of the above"],
    "correct_answer": 3,
    "explanation": "Application programs can do everything: retrieve, insert, update, and delete data."
  },
  {
    "id": 49,
    "type": "multiple_choice",
    "question": "Which user category typically accesses databases through menus and forms without knowing anything about the DBMS?",
    "options": ["DBA", "Sophisticated User", "Naïve User", "Logical Designer"],
    "correct_answer": 2,
    "explanation": "Naïve users use menus and forms and know nothing about the DBMS. Everyone else listed has DBMS knowledge."
  },
  {
    "id": 50,
    "type": "multiple_choice",
    "question": "Which statement about sophisticated users is TRUE?",
    "options": [
      "They are unaware of the database structure.",
      "They can use SQL to perform operations on the database.",
      "They only use menus and forms.",
      "They are responsible for hardware maintenance."
    ],
    "correct_answer": 1,
    "explanation": "Sophisticated users understand the structure and can use SQL. Being unaware or using only menus describes naïve users, hardware maintenance is for IT staff."
  },
  {
    "id": 51,
    "type": "multiple_choice",
    "question": "Which of the following converts data into information?",
    "options": [
      "File-Based System",
      "Database Management System",
      "Hardware",
      "Physical Database Designer"
    ],
    "correct_answer": 1,
    "explanation": "A DBMS processes raw data into meaningful information. File-based systems do this poorly, hardware is physical, a designer is a person."
  },
  {
    "id": 52,
    "type": "multiple_choice",
    "question": "Which term refers to raw facts?",
    "options": ["Database", "Information", "Data", "SQL"],
    "correct_answer": 2,
    "explanation": "Data is raw facts. A database stores data, information is processed data, SQL is a language."
  },
  {
    "id": 53,
    "type": "multiple_choice",
    "question": "Which term refers to processed and meaningful data?",
    "options": ["Information", "Data", "Database", "DDL"],
    "correct_answer": 0,
    "explanation": "Information is data that has been processed to be meaningful. Data is raw, a database stores both, DDL defines structure."
  },
  {
    "id": 54,
    "type": "multiple_choice",
    "question": "Which role would most likely be responsible for ensuring satisfactory application performance?",
    "options": ["End User", "DBA", "Application Developer", "Data Administrator"],
    "correct_answer": 2,
    "explanation": "Application developers ensure their code performs well. DBA handles database performance, users just use it, DA handles policies."
  },
  {
    "id": 55,
    "type": "multiple_choice",
    "question": "Which of these is both a DBMS advantage and a major improvement over file-based systems?",
    "options": [
      "Data Inconsistency",
      "Data Redundancy",
      "Data Integrity",
      "Duplicate Files"
    ],
    "correct_answer": 2,
    "explanation": "Data integrity (accuracy and consistency) is a DBMS advantage. The other three are problems that file-based systems have and DBMS fixes."
  },
  
  
  {
        "id": 56,
        "type": "multiple_choice",
        "question": "Which level shows only the data relevant to each user and hides the rest?",
        "options": [
            "Internal Level",
            "Conceptual Level",
            "External Level",
            "Physical Level"
        ],
        "correct_answer": 2,
        "explanation": "The External Level is the user's view of the database, showing only relevant data and hiding the rest."
    },
    {
        "id": 57,
        "type": "multiple_choice",
        "question": "Which level defines all entities, attributes, relationships, constraints, and security rules?",
        "options": [
            "External Level",
            "Conceptual Level",
            "Internal Level",
            "View Level"
        ],
        "correct_answer": 1,
        "explanation": "The Conceptual Level describes the entire logical structure of the database, including entities, attributes, relationships, constraints, and security rules."
    },
    {
        "id": 58,
        "type": "multiple_choice",
        "question": "Which level deals with file structures, indexing, and space optimization for performance?",
        "options": [
            "External Level",
            "Conceptual Level",
            "Internal Level",
            "Logical Level"
        ],
        "correct_answer": 2,
        "explanation": "The Internal Level shows how data is physically stored, including file structures, indexing, and space optimization."
    },
    {
        "id": 59,
        "type": "multiple_choice",
        "question": "Which level provides both the mapping and the desired independence between the external and internal levels?",
        "options": [
            "External Level",
            "Conceptual Level",
            "Internal Level",
            "Physical Level"
        ],
        "correct_answer": 1,
        "explanation": "The Conceptual Level provides the mapping and independence between the external and internal levels."
    },
    {
        "id": 60,
        "type": "multiple_choice",
        "question": "The way users perceive the data is called the:",
        "options": [
            "Internal level",
            "External level",
            "Conceptual level",
            "Physical level"
        ],
        "correct_answer": 1,
        "explanation": "The external level is how users perceive the data."
    },
    {
        "id": 61,
        "type": "multiple_choice",
        "question": "The way the DBMS and operating system perceive the data is the:",
        "options": [
            "External level",
            "View level",
            "Internal level",
            "Logical level"
        ],
        "correct_answer": 2,
        "explanation": "The internal level is how the DBMS and operating system perceive the data."
    },
    {
        "id": 62,
        "type": "multiple_choice",
        "question": "Which schema provides user-specific views of the database?",
        "options": [
            "Internal schema",
            "Conceptual schema",
            "External schema",
            "Physical schema"
        ],
        "correct_answer": 2,
        "explanation": "The External Schema provides user-specific views of the database."
    },
    {
        "id": 63,
        "type": "multiple_choice",
        "question": "The Conceptual/Internal mapping connects:",
        "options": [
            "User views to the conceptual schema",
            "Logical view with physical storage",
            "External schemas to each other",
            "Internal schema to the operating system"
        ],
        "correct_answer": 1,
        "explanation": "The Conceptual/Internal mapping connects the logical view with physical storage."
    },
    {
        "id": 64,
        "type": "multiple_choice",
        "question": "A database schema is the ______ while a database instance is the ______.",
        "options": [
            "Actual data, blueprint",
            "Blueprint, actual data at a particular time",
            "User view, storage structure",
            "Metadata, schema"
        ],
        "correct_answer": 1,
        "explanation": "The schema is the blueprint (intension), while the instance is the actual data at a particular time (extension/state)."
    },
    {
        "id": 65,
        "type": "multiple_choice",
        "question": "The schema is also called the intension; an instance is called the:",
        "options": [
            "Extension (or state)",
            "Catalog",
            "Metadata",
            "Dictionary"
        ],
        "correct_answer": 0,
        "explanation": "The schema is the intension; an instance is the extension or state of the database."
    },
    {
        "id": 66,
        "type": "multiple_choice",
        "question": "Physical Data Independence allows you to:",
        "options": [
            "Change user views without affecting storage",
            "Change the internal schema without affecting the conceptual schema",
            "Add new entities without changing external views",
            "Modify relationships without affecting users"
        ],
        "correct_answer": 1,
        "explanation": "Physical Data Independence means changing the internal schema without affecting the conceptual schema."
    },
    {
        "id": 67,
        "type": "multiple_choice",
        "question": "Changing from one indexing method to another for performance is an example of:",
        "options": [
            "Logical data independence",
            "External data independence",
            "Physical data independence",
            "Conceptual data independence"
        ],
        "correct_answer": 2,
        "explanation": "Changing indexing methods is a physical change that does not affect the conceptual schema, demonstrating Physical Data Independence."
    },
    {
        "id": 68,
        "type": "multiple_choice",
        "question": "Logical Data Independence allows:",
        "options": [
            "Changing internal storage without affecting conceptual schema",
            "Changing conceptual schema without affecting external schemas",
            "Changing file structures without affecting queries",
            "Changing compression methods without affecting users"
        ],
        "correct_answer": 1,
        "explanation": "Logical Data Independence allows changing the conceptual schema without affecting external schemas."
    },
    {
        "id": 69,
        "type": "multiple_choice",
        "question": "A data sublanguage consists of:",
        "options": [
            "3GL and 4GL",
            "DDL and DML",
            "Procedural and nonprocedural",
            "Query language and report generator"
        ],
        "correct_answer": 1,
        "explanation": "A data sublanguage includes Data Definition Language (DDL) and Data Manipulation Language (DML)."
    },
    {
        "id": 70,
        "type": "multiple_choice",
        "question": "Data Definition Language (DDL) is used to:",
        "options": [
            "Insert, update, and delete data",
            "Define entities, attributes, relationships, and constraints",
            "Generate reports and forms",
            "Write application programs"
        ],
        "correct_answer": 1,
        "explanation": "DDL defines and names entities, attributes, relationships, and applies integrity and security constraints."
    },
    {
        "id": 71,
        "type": "multiple_choice",
        "question": "When DDL statements are compiled, they generate:",
        "options": [
            "Database instances",
            "Query results",
            "Metadata stored in the system catalog",
            "User views"
        ],
        "correct_answer": 2,
        "explanation": "DDL compilation generates metadata stored in the system catalog (also called data dictionary)."
    },
    {
        "id": 72,
        "type": "multiple_choice",
        "question": "The system catalog is also known as:",
        "options": [
            "Data dictionary or data director",
            "Internal schema",
            "Transaction log",
            "Storage manager"
        ],
        "correct_answer": 0,
        "explanation": "The system catalog is also called a data dictionary or data director."
    },
    {
        "id": 73,
        "type": "multiple_choice",
        "question": "Data Manipulation Language (DML) is used to:",
        "options": [
            "Define database schema",
            "Create indexes and file structures",
            "Insert, modify, retrieve, and delete data",
            "Manage user access rights"
        ],
        "correct_answer": 2,
        "explanation": "DML is used to insert, modify, retrieve, and delete data in a database."
    },
    {
        "id": 74,
        "type": "multiple_choice",
        "question": "Procedural DML requires the user to specify:",
        "options": [
            "Only what data is needed",
            "How to get the data step by step",
            "The output format only",
            "The integrity constraints"
        ],
        "correct_answer": 1,
        "explanation": "Procedural DML tells the system how to get the data step by step."
    },
    {
        "id": 75,
        "type": "multiple_choice",
        "question": "Nonprocedural DML (like SQL) requires the user to specify:",
        "options": [
            "The exact storage path",
            "The indexing method to use",
            "What data is needed, not how to get it",
            "The file structure"
        ],
        "correct_answer": 2,
        "explanation": "Nonprocedural DML specifies what data is needed, not how to retrieve it."
    },
    {
        "id": 76,
        "type": "multiple_choice",
        "question": "Fourth-Generation Languages (4GLs) are:",
        "options": [
            "Procedural and low-level like assembly",
            "Nonprocedural and high-level for faster development",
            "Another name for C++ and Java",
            "Used only for operating system programming"
        ],
        "correct_answer": 1,
        "explanation": "4GLs are high-level, nonprocedural languages designed for faster application development."
    },
    {
        "id": 77,
        "type": "multiple_choice",
        "question": "Which of the following is a 4GL tool?",
        "options": [
            "C compiler",
            "Assembler",
            "Report generator",
            "Linker"
        ],
        "correct_answer": 2,
        "explanation": "Report generators are examples of 4GL tools, along with query generators, spreadsheets, and application generators."
    },
    {
        "id": 78,
        "type": "multiple_choice",
        "question": "Query and Report Generators in 4GL are used to:",
        "options": [
            "Compile DDL statements",
            "Ask questions and format output from data",
            "Manage storage allocation",
            "Define internal schemas"
        ],
        "correct_answer": 1,
        "explanation": "Query and Report Generators allow users to ask questions and format output from data."
    },
    {
        "id": 79,
        "type": "multiple_choice",
        "question": "Application Generators in 4GL:",
        "options": [
            "Require full manual coding",
            "Auto-generate app code with minimal input",
            "Only generate forms, not code",
            "Cannot be used for databases"
        ],
        "correct_answer": 1,
        "explanation": "Application Generators auto-generate application code with minimal user input."
    },
    {
        "id": 80,
        "type": "multiple_choice",
        "question": "A data model is a:",
        "options": [
            "Physical storage device",
            "High-level abstract description of how data is organized",
            "Programming language compiler",
            "User interface design"
        ],
        "correct_answer": 1,
        "explanation": "A data model is a high-level, abstract description of how data is organized, related, and constrained within an organization."
    },
    {
        "id": 81,
        "type": "multiple_choice",
        "question": "The three broad categories of data models are:",
        "options": [
            "External, conceptual, internal",
            "Object-based, record-based, physical",
            "Relational, network, hierarchical",
            "DDL, DML, 4GL"
        ],
        "correct_answer": 1,
        "explanation": "The three broad categories are object-based, record-based, and physical data models."
    },
    {
        "id": 82,
        "type": "multiple_choice",
        "question": "In an object-based data model, an entity is:",
        "options": [
            "A field within a record",
            "A real-world object you want to store data about",
            "An indexing method",
            "A storage structure"
        ],
        "correct_answer": 1,
        "explanation": "An entity is a real-world object (e.g., person, product, place) you want to store data about."
    },
    {
        "id": 83,
        "type": "multiple_choice",
        "question": "In an object-based data model, a relationship shows:",
        "options": [
            "How fields are physically arranged",
            "How two or more entities are connected",
            "The sequence of record storage",
            "The compression algorithm"
        ],
        "correct_answer": 1,
        "explanation": "A relationship shows how two or more entities are connected (e.g., a student enrolled in a course)."
    },
    {
        "id": 84,
        "type": "multiple_choice",
        "question": "Which is a type of object-based data model?",
        "options": [
            "Relational",
            "Hierarchical",
            "Entity-Relationship (ER)",
            "Network"
        ],
        "correct_answer": 2,
        "explanation": "Entity-Relationship (ER) is an object-based data model, along with Semantic, Functional, and Object-oriented models."
    },
    {
        "id": 85,
        "type": "multiple_choice",
        "question": "Record-based data models organize data as:",
        "options": [
            "Objects with methods",
            "Fixed-format structures with fields (records)",
            "Entity-relationship diagrams",
            "Physical access paths only"
        ],
        "correct_answer": 1,
        "explanation": "Record-based data models organize data as fixed-format structures with fields, called records."
    },
    {
        "id": 86,
        "type": "multiple_choice",
        "question": "Which is a type of record-based data model?",
        "options": [
            "Functional",
            "Semantic",
            "Relational",
            "Object-oriented"
        ],
        "correct_answer": 2,
        "explanation": "Relational, Network, and Hierarchical are record-based data models."
    },
    {
        "id": 87,
        "type": "multiple_choice",
        "question": "The Relational data model belongs to which category?",
        "options": [
            "Object-based",
            "Record-based",
            "Physical",
            "Hierarchical"
        ],
        "correct_answer": 1,
        "explanation": "The Relational data model is a record-based data model."
    },
    {
        "id": 88,
        "type": "multiple_choice",
        "question": "Physical data models describe:",
        "options": [
            "Business data requirements",
            "Entities, attributes, and relationships",
            "How data is actually stored on a computer system",
            "User views and formatting"
        ],
        "correct_answer": 2,
        "explanation": "Physical data models describe how data is actually stored on a computer system, including record structures, ordering, and access paths."
    },
    {
        "id": 89,
        "type": "multiple_choice",
        "question": "Access paths in physical data models include:",
        "options": [
            "Tables and foreign keys",
            "Indexes, pointers, and links",
            "Entity classes",
            "User privileges"
        ],
        "correct_answer": 1,
        "explanation": "Access paths include indexes, pointers, and links used to find and retrieve data quickly."
    },
    {
        "id": 90,
        "type": "multiple_choice",
        "question": "Conceptual modeling is the process of creating:",
        "options": [
            "A physical storage layout",
            "A high-level abstract model of data requirements",
            "User-specific external views",
            "Compilation of DDL statements"
        ],
        "correct_answer": 1,
        "explanation": "Conceptual modeling creates a high-level, abstract model of how data is used in an organization, independent of storage or system details."
    },
    {
        "id": 91,
        "type": "multiple_choice",
        "question": "A conceptual model is independent of:",
        "options": [
            "Business requirements",
            "Entities and relationships",
            "DBMS, programming languages, and physical storage details",
            "Integrity constraints"
        ],
        "correct_answer": 2,
        "explanation": "A conceptual model does not consider the DBMS, programming languages, or any physical storage details."
    },
    {
        "id": 92,
        "type": "multiple_choice",
        "question": "The Conceptual Model focuses on:",
        "options": [
            "DBMS-specific table structures",
            "Business data requirements",
            "Record ordering and indexing",
            "File organization and encryption"
        ],
        "correct_answer": 1,
        "explanation": "The Conceptual Model focuses on business data requirements, not technology-specific details."
    },
    {
        "id": 93,
        "type": "multiple_choice",
        "question": "The Logical Model depends on:",
        "options": [
            "No technology at all",
            "A specific DBMS (e.g., relational model)",
            "Physical storage only",
            "The operating system"
        ],
        "correct_answer": 1,
        "explanation": "The Logical Model depends on a specific DBMS model, such as the relational model."
    },
    {
        "id": 94,
        "type": "multiple_choice",
        "question": "Which model includes tables, keys, and normalization rules?",
        "options": [
            "Conceptual Model",
            "Physical Model",
            "Logical Model",
            "External Model"
        ],
        "correct_answer": 2,
        "explanation": "The Logical Model includes tables, keys, and normalization rules."
    },
    {
        "id": 95,
        "type": "multiple_choice",
        "question": "The Conceptual Model includes:",
        "options": [
            "Storage paths and indexes",
            "Entities, relationships, and constraints",
            "Record formats and compression",
            "File structures and hashing"
        ],
        "correct_answer": 1,
        "explanation": "The Conceptual Model includes entities, relationships, and constraints."
    },
    {
        "id": 96,
        "type": "multiple_choice",
        "question": "Which of the following is a function of a DBMS?",
        "options": [
            "Web server management",
            "Concurrency control services",
            "HTML page generation",
            "Operating system scheduling"
        ],
        "correct_answer": 1,
        "explanation": "Concurrency control services are a standard DBMS function, along with transaction support, recovery, integrity, and utility services."
    },
    {
        "id": 97,
        "type": "multiple_choice",
        "question": "Transaction support in a DBMS provides:",
        "options": [
            "Faster indexing",
            "Grouping of operations into atomic units",
            "Report generation",
            "User interface design"
        ],
        "correct_answer": 1,
        "explanation": "Transaction support groups operations into atomic units that either全部 complete or全部 fail."
    },
    {
        "id": 98,
        "type": "multiple_choice",
        "question": "Recovery services in a DBMS are responsible for:",
        "options": [
            "User authentication",
            "Restoring the database after a failure",
            "Generating forms",
            "Compiling DML into machine code"
        ],
        "correct_answer": 1,
        "explanation": "Recovery services restore the database after a failure."
    },
    {
        "id": 99,
        "type": "multiple_choice",
        "question": "Concurrency control services ensure:",
        "options": [
            "Data is encrypted",
            "Multiple users can access data without conflicts",
            "Queries run faster",
            "Storage is compressed"
        ],
        "correct_answer": 1,
        "explanation": "Concurrency control services allow multiple users to access data without conflicts."
    },
    {
        "id": 100,
        "type": "multiple_choice",
        "question": "Integrity services in a DBMS ensure:",
        "options": [
            "Fast query response times",
            "Data is accurate and consistent with constraints",
            "Storage devices are optimized",
            "Users have different views"
        ],
        "correct_answer": 1,
        "explanation": "Integrity services ensure data is accurate and consistent with defined constraints."
    },
    {
        "id": 101,
        "type": "multiple_choice",
        "question": "A user-accessible catalog in a DBMS contains:",
        "options": [
            "Only user passwords",
            "Metadata about all database objects",
            "Actual data records",
            "Index structures only"
        ],
        "correct_answer": 1,
        "explanation": "The user-accessible catalog contains metadata describing all database objects."
    },
    {
        "id": 102,
        "type": "multiple_choice",
        "question": "Utility services of a DBMS include:",
        "options": [
            "Query optimization only",
            "Backup, recovery, and database maintenance",
            "User view definition",
            "Constraint checking"
        ],
        "correct_answer": 1,
        "explanation": "Utility services include backup, recovery, and general database maintenance."
    },
    {
        "id": 103,
        "type": "multiple_choice",
        "question": "Support for data communication in a DBMS allows:",
        "options": [
            "Faster local processing",
            "Data sharing over networks",
            "Better compression algorithms",
            "User-defined functions in C++"
        ],
        "correct_answer": 1,
        "explanation": "Support for data communication allows data sharing over networks."
    },
    {
        "id": 104,
        "type": "multiple_choice",
        "question": "Services to promote data independence in a DBMS allow:",
        "options": [
            "Data duplication",
            "Changes at lower levels without affecting higher levels",
            "Unlimited data storage",
            "Automatic indexing"
        ],
        "correct_answer": 1,
        "explanation": "Data independence services ensure changes at lower levels do not affect higher levels."
    },
    {
        "id": 105,
        "type": "multiple_choice",
        "question": "Which of the following is NOT a typical function of a DBMS?",
        "options": [
            "Transaction support",
            "Concurrency control services",
            "Web browser rendering",
            "Recovery services"
        ],
        "correct_answer": 2,
        "explanation": "Web browser rendering is not a DBMS function; DBMS functions include transaction support, concurrency control, recovery, integrity, and utility services."
    }






]
}
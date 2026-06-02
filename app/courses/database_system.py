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
    "explanation": "A database is a shared collection of logically related data (and a description of itself). Option 0 describes a DBMS; option 2 describes data; option 3 describes a file-based system."
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
    "explanation": "Data = raw facts. Option 0 describes information; option 1 describes a file; option 3 describes information again."
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
    "explanation": "Information = data + meaning/processing. Option 1 describes a file-based system; option 2 describes SQL; option 3 describes redundancy."
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
    "explanation": "DBMS is software. Option 0 describes a database; option 2 describes a file-based system; option 3 describes a procedure."
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
    "explanation": "File-based systems suffer from uncontrolled data redundancy. Data integrity, data independence, and concurrency are DBMS advantages, not file-system advantages."
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
    "explanation": "Redundancy = duplication. Option 1 describes security; option 2 describes information processing; option 3 describes concurrency."
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
    "explanation": "Inconsistency = different versions of same data. Option 0 describes a relational structure; option 2 describes security; option 3 describes backup."
  },
  {
    "id": 8,
    "type": "multiple_choice",
    "question": "Which language is used to define data structures and constraints?",
    "options": ["SQL", "DML", "DDL", "DBMS"],
    "correct_answer": 2,
    "explanation": "DDL (Data Definition Language). SQL is a query language; DML manipulates data; DBMS is the system itself."
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
    "explanation": "DML = Data Manipulation Language. Option 0 is DDL; option 2 is hardware design; option 3 is administration."
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
    "explanation": "SQL = Structured Query Language. Option 0 is hardware; option 1 is file-based system; option 4 is DBA."
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
    "explanation": "Data integrity (accuracy/consistency) is a DBMS advantage. Inconsistency, poor sharing, and uncontrolled redundancy are file-system problems."
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
    "explanation": "Integrity = accuracy + consistency. Option 0 is redundancy; option 2 is file-based approach; option 3 is security, not integrity."
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
    "explanation": "Concurrency = simultaneous access with control. Option 1 is redundancy; option 2 is storage; option 3 is processing."
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
    "explanation": "Data independence = changes to storage/structures don't affect applications. Option 1 is nonsense; option 2 is sharing; option 4 is false."
  },
  {
    "id": 15,
    "type": "multiple_choice",
    "question": "Which is NOT one of the five DBMS environment components?",
    "options": ["Hardware", "Software", "Procedures", "Internet"],
    "correct_answer": 3,
    "explanation": "The five components are Hardware, Software, Data, Procedures, People. Internet is not one of them."
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
    "explanation": "Correct five: Hardware, Software, Data, Procedures, People. Security, SQL, files, tables are subcomponents or tools."
  },
  {
    "id": 17,
    "type": "multiple_choice",
    "question": "The component that contains the DBMS, operating system, and application programs is:",
    "options": ["Data", "Software", "Procedures", "Hardware"],
    "correct_answer": 1,
    "explanation": "Software component includes DBMS, OS, and apps. Data is the database itself; procedures are rules; hardware is physical devices."
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
    "explanation": "Procedures = instructions/rules (login, backup, etc.). Option 0 is data; option 2 is software; option 3 is hardware."
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
    "explanation": "DA = strategic/planning role. Option 1 is application developer; option 2 is sophisticated user; option 3 is physical DBA."
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
    "explanation": "DBA = technical/operational role. Option 1 is logical designer; option 2 is end-user or developer; option 3 is OS developer."
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
    "explanation": "Logical design = what (entities, attributes, relationships). Option 0 is physical design; option 2 is DBA; option 3 is hardware."
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
    "explanation": "Physical design = how (storage, indexing). Option 0 is logical design; option 1 is DA; option 3 is procedures/training."
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
    "explanation": "Conceptual design = independent of physical/implementation details. Options 0,1 are physical; option 3 is installation."
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
    "explanation": "Application developers = write application programs. Option 1 is DA; option 2 is hardware engineer; option 3 is DBA."
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
    "explanation": "Naïve user = no DBMS knowledge, uses menus/forms. Option 0 is sophisticated user; option 2 is designer; option 3 is DBA."
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
    "explanation": "Sophisticated user = understands structure, may use SQL. Option 0/1 describe naïve user; option 3 is hardware role."
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
    "explanation": "Database = shared, minimal redundancy. Option 0 is file-based; option 2 is false (stores raw data too); option 3 is OS."
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
    "explanation": "File-based systems literally have 'poor data sharing' as a limitation. Integrity, concurrency, scalability are also problems but not the direct answer to 'makes sharing difficult'."
  },
  {
    "id": 29,
    "type": "multiple_choice",
    "question": "Which DBMS advantage allows the system to support large numbers of users and data?",
    "options": ["Security", "Scalability", "Data Integrity", "Procedures"],
    "correct_answer": 1,
    "explanation": "Scalability = growth in users/data. Security is protection; integrity is accuracy; procedures are rules."
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
    "explanation": "DBMS's purpose = turn data into information. Option 1 is opposite; option 2 is false; option 3 is false."
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
    "explanation": "File-based system = collection of application programs for end-users. Option 0 is DBMS; option 2 is database; option 3 is database."
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
    "explanation": "Studying file-based systems reveals the problems (redundancy, inconsistency, poor sharing) that DBMSs solve. They are not faster, don't eliminate redundancy, and are not widely used today."
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
    "explanation": "Separate duplicate files = file-based system, not a database. Database is shared, minimal redundancy, concurrent access."
  },
  {
    "id": 34,
    "type": "multiple_choice",
    "question": "Which DBMS facility allows users to specify data types and constraints?",
    "options": ["DML", "SQL", "DDL", "DBA"],
    "correct_answer": 2,
    "explanation": "DDL defines data types/constraints. DML manipulates data; SQL includes both but DDL is the specific facility; DBA is a role."
  },
  {
    "id": 35,
    "type": "multiple_choice",
    "question": "Which operation is performed using DML?",
    "options": ["CREATE", "ALTER", "SELECT", "DEFINE"],
    "correct_answer": 2,
    "explanation": "SELECT is DML (retrieval). CREATE, ALTER, DEFINE are DDL operations."
  },
  {
    "id": 36,
    "type": "multiple_choice",
    "question": "The most common query language used in relational databases is:",
    "options": ["Java", "SQL", "COBOL", "Pascal"],
    "correct_answer": 1,
    "explanation": "SQL is the standard query language for relational DBMSs. Java/COBOL/Pascal are programming languages."
  },
  {
    "id": 37,
    "type": "multiple_choice",
    "question": "Which DBMS advantage hides complex storage details from users?",
    "options": ["Data Redundancy", "Abstraction", "Poor Data Sharing", "File Synchronization"],
    "correct_answer": 1,
    "explanation": "Abstraction = hiding storage complexity. Data redundancy is a problem; poor data sharing is a file-system problem; file synchronization is not a DBMS advantage."
  },
  {
    "id": 38,
    "type": "multiple_choice",
    "question": "Which component serves as the bridge between machine and human components in a DBMS environment?",
    "options": ["Hardware", "Data", "Procedures", "Software"],
    "correct_answer": 3,
    "explanation": "Software (DBMS, OS, apps) bridges hardware (machine) and people/procedures (human). Data is passive; procedures are human-side."
  },
  {
    "id": 39,
    "type": "multiple_choice",
    "question": "Which component contains instructions such as how to log on, make backups, and start or stop the DBMS?",
    "options": ["Data", "Procedures", "Hardware", "Security"],
    "correct_answer": 1,
    "explanation": "Procedures = instructions/rules. Data is raw facts; hardware is physical; security is an attribute, not a component."
  },
  {
    "id": 40,
    "type": "multiple_choice",
    "question": "Which of the following is considered hardware in a DBMS environment?",
    "options": ["SQL", "Database tables", "Servers and storage devices", "User manuals"],
    "correct_answer": 2,
    "explanation": "Hardware = physical devices (servers, storage). SQL is language; tables are data structures; manuals are procedures/people."
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
    "explanation": "DA = strategic (planning, policies). Physical implementation and performance tuning = DBA; writing apps = developer."
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
    "explanation": "DBA = physical realization (implementation, security, performance). Conceptual design = logical designer; requirements = analyst; reports = end-user."
  },
  {
    "id": 43,
    "type": "multiple_choice",
    "question": "Which professional identifies entities, attributes, and relationships?",
    "options": ["DBA", "Application Developer", "Logical Database Designer", "End User"],
    "correct_answer": 2,
    "explanation": "Logical designer identifies entities/attributes/relationships. DBA does physical; developer writes code; end user uses system."
  },
  {
    "id": 44,
    "type": "multiple_choice",
    "question": "Business rules are another name for:",
    "options": ["Constraints", "Queries", "Procedures", "Transactions"],
    "correct_answer": 0,
    "explanation": "Business rules = constraints on data. Queries retrieve data; procedures are instructions; transactions are units of work."
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
    "explanation": "Conceptual design is independent of implementation (physical). Physical design depends on storage; application design depends on both; security design is cross-cutting."
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
    "explanation": "Physical designer = storage structures/access methods. Identifying entities = logical designer; policies = DA; reports = user/developer."
  },
  {
    "id": 47,
    "type": "multiple_choice",
    "question": "Application developers usually work from specifications produced by:",
    "options": ["End Users", "Database Designers", "Systems Analysts", "Data Administrators"],
    "correct_answer": 2,
    "explanation": "Systems analysts produce specifications. End users provide requirements; designers design schema; DA does policies."
  },
  {
    "id": 48,
    "type": "multiple_choice",
    "question": "Which database operation may be requested by an application program?",
    "options": ["Retrieve data", "Insert data", "Update data", "All of the above"],
    "correct_answer": 3,
    "explanation": "Application programs can retrieve, insert, update, and delete data (all DML operations)."
  },
  {
    "id": 49,
    "type": "multiple_choice",
    "question": "Which user category typically accesses databases through menus and forms without knowing anything about the DBMS?",
    "options": ["DBA", "Sophisticated User", "Naïve User", "Logical Designer"],
    "correct_answer": 2,
    "explanation": "Naïve user uses menus/forms, no DBMS knowledge. DBA/sophisticated user/designer all have DBMS knowledge."
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
    "explanation": "Sophisticated users understand structure and may use SQL. Unaware/only menus = naïve user; hardware maintenance = DBA/IT staff."
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
    "explanation": "DBMS processes raw data into meaningful information. File-based systems don't do this well; hardware is physical; designer is a role."
  },
  {
    "id": 52,
    "type": "multiple_choice",
    "question": "Which term refers to raw facts?",
    "options": ["Database", "Information", "Data", "SQL"],
    "correct_answer": 2,
    "explanation": "Data = raw facts. Database = collection of data; information = processed data; SQL = language."
  },
  {
    "id": 53,
    "type": "multiple_choice",
    "question": "Which term refers to processed and meaningful data?",
    "options": ["Information", "Data", "Database", "DDL"],
    "correct_answer": 0,
    "explanation": "Information = processed/meaningful data. Data is raw; database is storage; DDL is definition language."
  },
  {
    "id": 54,
    "type": "multiple_choice",
    "question": "Which role would most likely be responsible for ensuring satisfactory application performance?",
    "options": ["End User", "DBA", "Application Developer", "Data Administrator"],
    "correct_answer": 2,
    "explanation": "Application developer ensures application performance (code efficiency). DBA ensures database performance; end user uses; DA does policy."
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
    "explanation": "Data integrity is a DBMS advantage. Inconsistency, redundancy, duplicate files are problems of file-based systems."
  }





]
}
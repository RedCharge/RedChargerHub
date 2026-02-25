cpp_programming_quiz = {
    "course_code": "BCP 203",
    "course_name": "Computer Organization Architecture",
    "total_questions": 80,
    "questions": [
    
    {
        "id": 1,
        "type": "multiple_choice",
        "question": "In C++, which of the following modes would you use to open a file for BOTH reading and writing without deleting existing content?",
        "options": [
            "ios::out",
            "ios::in | ios::out",
            "ios::trunc",
            "ios::app | ios::in"
        ],
        "correct_answer": 1,
        "explanation": "ios::in enables reading, and ios::out enables writing. Combining them with the bitwise OR operator (|) opens the file for both reading and writing without truncating (deleting) the existing content by default."
    },
    {
        "id": 2,
        "type": "multiple_choice",
        "question": "Which of the following correctly summarizes the relationship between `ifstream`, `ofstream`, and `fstream`?",
        "options": [
            "All three are identical in function",
            "ifstream is for reading, ofstream is for writing, fstream supports both",
            "ofstream is for reading, ifstream is for writing, fstream is for binary only",
            "fstream is used only for random access"
        ],
        "correct_answer": 1,
        "explanation": "ifstream (input file stream) is derived from istream for reading files. ofstream (output file stream) is derived from ostream for writing files. fstream (file stream) is derived from iostream and can be used for both input and output operations."
    },
    {
        "id": 3,
        "type": "multiple_choice",
        "question": "What is the purpose of calling `file.close()` after file operations?",
        "options": [
            "Deletes the file from disk",
            "Saves changes and releases the file resource back to the OS",
            "Resets the file pointer to the beginning",
            "Converts the file to binary format"
        ],
        "correct_answer": 1,
        "explanation": "Closing a file flushes any remaining data in the buffer to the file, ensuring all changes are saved. It also disassociates the stream object from the file, freeing the operating system resource for other processes."
    },
    {
        "id": 4,
        "type": "multiple_choice",
        "question": "File handling in C++ makes persistent data storage possible because:",
        "options": [
            "RAM retains data even after the program closes",
            "Files on secondary storage survive program termination",
            "The operating system automatically backs up all variables",
            "C++ compresses data into ROM"
        ],
        "correct_answer": 1,
        "explanation": "RAM is volatile, meaning its contents are lost when power is cut or the program ends. Secondary storage (like hard drives or SSDs) is non-volatile, so data written to files there persists independently of the program's lifecycle."
    },
    {
        "id": 5,
        "type": "multiple_choice",
        "question": "What class in C++ is used specifically for writing data to files?",
        "options": [
            "ifstream",
            "ofstream",
            "fstream",
            "iostream"
        ],
        "correct_answer": 1,
        "explanation": "ofstream stands for 'output file stream'. It is specifically designed and provides convenient methods for creating files and writing data to them."
    },
    {
        "id": 6,
        "type": "multiple_choice",
        "question": "Which of the following correctly pairs a data structure with its most appropriate application?",
        "options": [
            "Graph — process scheduling in OS",
            "Tree — computer network topology",
            "Priority Queue — managing process scheduling in OS",
            "Stack — representing file system hierarchy"
        ],
        "correct_answer": 2,
        "explanation": "A priority queue is ideal for scheduling because it always allows the highest priority process (or the one with the earliest deadline) to be processed next. Trees are better for hierarchies, and graphs for general network topologies."
    },
    {
        "id": 7,
        "type": "multiple_choice",
        "question": "What is the role of `file << \"Name: \" << studentName << endl;` in file handling?",
        "options": [
            "Reads the variable studentName from the file",
            "Writes the string 'Name: ' followed by the value of studentName and a newline to the file",
            "Deletes a record from the file",
            "Searches the file for the name"
        ],
        "correct_answer": 1,
        "explanation": "The insertion operator (<<), when used with an output file stream (like ofstream or fstream in output mode), sends data to the file. This line writes a literal string, then the contents of the `studentName` variable, and finally a newline character to the file."
    },
    {
        "id": 8,
        "type": "multiple_choice",
        "question": "Which operation involves combining two data structures into one?",
        "options": [
            "Sorting",
            "Splitting",
            "Merging",
            "Reversal"
        ],
        "correct_answer": 2,
        "explanation": "Merging is the process of taking two or more sorted (or unsorted) data structures and combining their elements into a single data structure."
    },
    {
        "id": 9,
        "type": "multiple_choice",
        "question": "Which data structure is most appropriate for representing a file system hierarchy in a file explorer GUI?",
        "options": [
            "Queue",
            "Stack",
            "Graph",
            "Tree"
        ],
        "correct_answer": 3,
        "explanation": "A file system is a classic example of a tree structure. It has a root directory, and each directory can contain files and sub-directories, forming parent-child relationships without cycles (in a simple view)."
    },
    {
        "id": 10,
        "type": "multiple_choice",
        "question": "In random access files, what does the term 'block number' refer to?",
        "options": [
            "The total number of files on disk",
            "The address used to directly locate a specific block or record",
            "The number of bytes in a record",
            "The file's position in a directory"
        ],
        "correct_answer": 1,
        "explanation": "In random/direct access, data is often organized into fixed-size blocks or records. A 'block number' is essentially the index or address of a specific block, which the system uses to calculate the exact byte offset and jump directly to that data."
    },
    {
        "id": 11,
        "type": "multiple_choice",
        "question": "If a file has records of 100 bytes each, and you want to access the 5th record (zero-indexed), the byte offset is:",
        "options": [
            "5 bytes",
            "100 bytes",
            "500 bytes",
            "505 bytes"
        ],
        "correct_answer": 2,
        "explanation": "The byte offset is calculated as `record_number * record_size`. For the zero-indexed 5th record, this is 5 * 100 = 500 bytes. The first byte of the file is offset 0, so the 5th record starts at byte 500."
    },
    {
        "id": 12,
        "type": "multiple_choice",
        "question": "Which stream object is used for standard input in C++?",
        "options": [
            "cout",
            "cerr",
            "cin",
            "clog"
        ],
        "correct_answer": 2,
        "explanation": "cin (character input) is the standard input stream object, typically associated with the keyboard. It is used with the extraction operator (>>) to read data."
    },
    {
        "id": 13,
        "type": "multiple_choice",
        "question": "Random (direct) access allows you to:",
        "options": [
            "Read data only from the beginning of the file",
            "Read or write data at any position without reading preceding data",
            "Access data only in reverse order",
            "Write data only to the end of a file"
        ],
        "correct_answer": 1,
        "explanation": "The key characteristic of random access is the ability to move the file pointer directly to any location (byte offset) in the file and perform an I/O operation there, without having to process all the data that comes before it."
    },
    {
        "id": 14,
        "type": "multiple_choice",
        "question": "Which keyword/class would you use to both read from AND write to the same file in C++?",
        "options": [
            "ifstream",
            "ofstream",
            "fstream",
            "biostream"
        ],
        "correct_answer": 2,
        "explanation": "fstream is the file stream class that inherits from both istream and ostream. This allows an fstream object to be used for both input (reading) and output (writing) operations on a file, provided it is opened in a mode that permits both."
    },
    {
        "id": 15,
        "type": "multiple_choice",
        "question": "Why is understanding file access methods important for beginner programmers?",
        "options": [
            "File access methods are only needed for advanced systems programming",
            "It helps programmers choose the most appropriate technique for their specific use case",
            "All file access methods work the same way so it doesn't matter",
            "File access methods are only relevant for database administrators"
        ],
        "correct_answer": 1,
        "explanation": "Different applications have different needs. A programmer needs to know whether to use sequential access (e.g., for processing a log file) or random access (e.g., for a database lookup) to write efficient and correct programs."
    },
    {
        "id": 16,
        "type": "multiple_choice",
        "question": "Which data structure would BEST represent a computer network with devices and connections between them?",
        "options": [
            "Stack",
            "Queue",
            "Tree",
            "Graph"
        ],
        "correct_answer": 3,
        "explanation": "A graph is a non-linear data structure consisting of nodes (vertices) and edges. This perfectly models a computer network, where devices are nodes and the connections (wired or wireless) are the edges, which can have arbitrary relationships, not just hierarchical ones."
    },
    {
        "id": 17,
        "type": "multiple_choice",
        "question": "Which statement about sequential access is CORRECT?",
        "options": [
            "It can jump to any record directly",
            "It is the most efficient method for very large databases",
            "It reads each record one after another in order",
            "It requires records to be stored at fixed memory addresses"
        ],
        "correct_answer": 2,
        "explanation": "Sequential access means that to get to a particular piece of data, you must read all the data that precedes it in the file, in order. It's like playing a tape from the beginning."
    },
    {
        "id": 18,
        "type": "multiple_choice",
        "question": "In C++ file programs, why is `file.close()` important even though the OS closes files when the program ends?",
        "options": [
            "It prevents file corruption and ensures all buffered data is written to disk",
            "It deletes the file from memory",
            "It converts the file from binary to text",
            "It is required by the compiler"
        ],
        "correct_answer": 0,
        "explanation": "Data written to a file stream is often buffered. `close()` forces a flush of this buffer, ensuring all data is physically written to the disk. While the OS will eventually close it, calling `close()` explicitly is good practice to prevent data loss if the program crashes later and to free the resource immediately."
    },
    {
        "id": 19,
        "type": "multiple_choice",
        "question": "In C++, which of the following correctly declares a file stream object for reading?",
        "options": [
            "ofstream myFile;",
            "readstream myFile;",
            "ifstream myFile;",
            "filestream myFile;"
        ],
        "correct_answer": 2,
        "explanation": "ifstream (input file stream) is the class specifically designed for reading data from files. Declaring an ifstream object creates a stream for input operations."
    },
    {
        "id": 20,
        "type": "multiple_choice",
        "question": "In database management systems, which data structure is commonly used to store and retrieve data efficiently using a key?",
        "options": [
            "Stack",
            "Queue",
            "Key-value or tree (index) structure",
            "Linked list"
        ],
        "correct_answer": 2,
        "explanation": "Databases use indexing structures, often based on balanced trees (like B-Trees) or hash tables, to allow for rapid lookup of records based on a key value without having to scan the entire table."
    },
    {
        "id": 21,
        "type": "multiple_choice",
        "question": "What is a key DISADVANTAGE of random access files?",
        "options": [
            "They cannot be used with modern storage devices",
            "They require fixed record sizes, which can waste space for variable-length data",
            "They are slower than sequential access for every task",
            "They do not support the write operation"
        ],
        "correct_answer": 1,
        "explanation": "To calculate the position of a record (offset = record_number * record_size), each record must have a fixed size. If you store variable-length data (like names), you must allocate the maximum possible size for each record, which can lead to significant wasted space."
    },
    {
        "id": 22,
        "type": "multiple_choice",
        "question": "Which operation involves arranging elements in a data structure in a particular order?",
        "options": [
            "Merging",
            "Splitting",
            "Sorting",
            "Indexing"
        ],
        "correct_answer": 2,
        "explanation": "Sorting is the process of arranging data in a specific order, such as ascending or descending, numerical or lexicographical."
    },
    {
        "id": 23,
        "type": "multiple_choice",
        "question": "A CSV file stores student grades and is read line by line to compute averages. Which access method is being used?",
        "options": [
            "Random access",
            "Direct access",
            "Sequential access",
            "Indexed access"
        ],
        "correct_answer": 2,
        "explanation": "Reading a file 'line by line' from the beginning to the end is the definition of sequential access. Each line is processed in order."
    },
    {
        "id": 24,
        "type": "multiple_choice",
        "question": "In the code: `ofstream file(\"students.txt\", ios::app);`—what does this line do if students.txt already contains data?",
        "options": [
            "Deletes the existing data and starts fresh",
            "Refuses to open the file",
            "Opens the file and positions the pointer at the end to append",
            "Opens the file in read-only mode"
        ],
        "correct_answer": 2,
        "explanation": "ios::app (append mode) ensures that all output operations happen at the end of the file. The existing content is preserved, and new data is written after it."
    },
    {
        "id": 25,
        "type": "multiple_choice",
        "question": "Which of the following scenarios benefits MOST from random access?",
        "options": [
            "Printing all student names in a class register from start to end",
            "Generating a report of all sales transactions for the year",
            "Looking up a specific employee record using an ID number",
            "Backing up all records in a log file"
        ],
        "correct_answer": 2,
        "explanation": "Looking up a specific record by an ID is a classic use case for random access. It would be highly inefficient to read all preceding employee records just to find the one you need. Random access allows the program to jump directly to that record's location."
    },
    {
        "id": 26,
        "type": "multiple_choice",
        "question": "What is the main difference between sequential access and random access?",
        "options": [
            "Sequential access is faster than random access in all cases",
            "Sequential access reads records in order; random access can directly access any record",
            "Random access is only possible with text files",
            "Sequential access requires larger files"
        ],
        "correct_answer": 1,
        "explanation": "This is the core distinction. Sequential access processes data in a linear, one-after-the-other fashion. Random (or direct) access allows non-sequential, immediate access to any data record based on its location."
    },
    {
        "id": 27,
        "type": "multiple_choice",
        "question": "What does `ios::app` mode do when opening a file?",
        "options": [
            "Overwrites all existing content",
            "Opens the file for reading only",
            "Appends new data to the end of the existing file",
            "Creates a binary file"
        ],
        "correct_answer": 2,
        "explanation": "ios::app stands for 'append'. When a file is opened in this mode, the output file pointer is positioned at the end of the file before every write operation, ensuring that all data written is added to the end."
    },
    {
        "id": 28,
        "type": "multiple_choice",
        "question": "Which of the following file extensions typically indicates a binary file?",
        "options": [
            ".txt",
            ".csv",
            ".bin",
            ".md"
        ],
        "correct_answer": 2,
        "explanation": ".bin is a common extension for binary files, indicating that the data is stored in a raw, non-human-readable format. .txt, .csv, and .md are typically text-based."
    },
    {
        "id": 29,
        "type": "multiple_choice",
        "question": "What is the purpose of a stream object like `cin` or `cout` in C++?",
        "options": [
            "To define variables in memory",
            "To handle the flow of data between the program and input/output devices",
            "To allocate memory for arrays",
            "To execute system commands"
        ],
        "correct_answer": 1,
        "explanation": "A stream is an abstraction that represents a flow of data. `cin` handles the flow of input data from an input device (usually the keyboard) into the program. `cout` handles the flow of output data from the program to an output device (usually the screen)."
    },
    {
        "id": 30,
        "type": "multiple_choice",
        "question": "Why must records in a random access file typically have a fixed size?",
        "options": [
            "To save disk space",
            "To allow direct computation of each record's byte offset",
            "To make the file human-readable",
            "Because C++ does not support variable-length records"
        ],
        "correct_answer": 1,
        "explanation": "The ability to 'jump' directly to a record relies on knowing exactly where it starts. With fixed-size records, the starting byte of record N is always `N * record_size`. If records had variable sizes, this simple calculation wouldn't work."
    },
    {
        "id": 31,
        "type": "multiple_choice",
        "question": "Which C++ function reads an entire line of input including spaces?",
        "options": [
            "cin >>",
            "scanf()",
            "getline(cin, variable)",
            "read()"
        ],
        "correct_answer": 2,
        "explanation": "The extraction operator (>>) stops reading at the first whitespace. `getline()` reads all characters until it encounters a newline character, making it suitable for reading strings that contain spaces."
    },
    {
        "id": 32,
        "type": "multiple_choice",
        "question": "Which of these data structure applications involves managing hierarchical data displayed in a GUI?",
        "options": [
            "Using a queue to schedule OS processes",
            "Using a graph to represent network topology",
            "Using a tree to represent a file system in a file explorer",
            "Using a stack to reverse a linked list"
        ],
        "correct_answer": 2,
        "explanation": "A file explorer GUI displays folders and files in a hierarchical manner, which is a perfect visual representation of a tree data structure. Each folder is a node that can contain child nodes (subfolders or files)."
    },
    {
        "id": 33,
        "type": "multiple_choice",
        "question": "A teacher records daily attendance in a file as students arrive. To find a specific student, the system reads names from the beginning. This is an example of:",
        "options": [
            "Random access",
            "Indexed access",
            "Sequential access",
            "Binary access"
        ],
        "correct_answer": 2,
        "explanation": "Reading names from the beginning until the target is found is sequential search on a file. The file is accessed in the order the data was written."
    },
    {
        "id": 34,
        "type": "multiple_choice",
        "question": "In sequential access, what happens to the file pointer after a READ operation?",
        "options": [
            "It returns to the beginning of the file",
            "It moves forward by one record",
            "It moves to the end of the file",
            "It remains at the same position"
        ],
        "correct_answer": 1,
        "explanation": "After a read operation in sequential access, the file pointer is automatically advanced to the next byte or record, ready for the subsequent read. This is what allows the program to read the file from start to finish."
    },
    {
        "id": 35,
        "type": "multiple_choice",
        "question": "A file contains 1,000 student records stored sequentially. To find the 800th student, the program must:",
        "options": [
            "Jump directly to record 800",
            "Read all 799 records before reaching record 800",
            "Use an index to locate record 800",
            "Load all records into RAM at once"
        ],
        "correct_answer": 1,
        "explanation": "This is the limitation of sequential access. There is no direct path to record 800. The program must start at record 1 and read, in order, every record until it finally reaches the 800th one."
    },
    {
        "id": 36,
        "type": "multiple_choice",
        "question": "What is the output of this code if 'data.txt' cannot be opened? `ofstream file(\"data.txt\"); if (!file.is_open()) { cerr << \"File error!\"; }`",
        "options": [
            "File error!",
            "Nothing is printed",
            "The program terminates silently",
            "data.txt is created automatically"
        ],
        "correct_answer": 0,
        "explanation": "The condition `!file.is_open()` is true because the file failed to open. The code inside the `if` block executes, printing 'File error!' to the standard error stream (cerr)."
    },
    {
        "id": 37,
        "type": "multiple_choice",
        "question": "In the context of file handling, what is a 'file pointer'?",
        "options": [
            "A C++ pointer variable that stores a file's memory address",
            "An internal marker indicating the current position in the file for the next read/write operation",
            "A function that opens a file",
            "A data type used to declare files"
        ],
        "correct_answer": 1,
        "explanation": "The file pointer (or position indicator) is an internal value maintained by the stream object. It keeps track of the byte offset where the next read or write operation will occur within the file."
    },
    {
        "id": 38,
        "type": "multiple_choice",
        "question": "Which operation involves breaking a data structure into smaller parts?",
        "options": [
            "Indexing",
            "Splitting",
            "Merging",
            "Sorting"
        ],
        "correct_answer": 1,
        "explanation": "Splitting is the opposite of merging. It is the process of dividing a single data structure into two or more smaller, independent data structures."
    },
    {
        "id": 39,
        "type": "multiple_choice",
        "question": "Which of the following is TRUE about random access files?",
        "options": [
            "They must be read from the first record every time",
            "They are only suitable for small files",
            "They allow retrieval of any record directly using its position",
            "They are incompatible with binary data"
        ],
        "correct_answer": 2,
        "explanation": "The defining feature of random access files is the ability to directly access any record by its numerical position or byte offset, without needing to read previous records."
    },
    {
        "id": 40,
        "type": "multiple_choice",
        "question": "Which of the following correctly uses the `<<` operator to write data to a file?",
        "options": [
            "file >> \"Hello\";",
            "cout << file << \"Hello\";",
            "file << \"Hello\";",
            "write(file, \"Hello\");"
        ],
        "correct_answer": 2,
        "explanation": "The insertion operator (<<) is used with an output stream (like an ofstream object named `file`) to send data to that stream, which then writes it to the file."
    },
    {
        "id": 41,
        "type": "multiple_choice",
        "question": "Which of the following best defines sequential file access?",
        "options": [
            "Data is accessed by jumping to any position in the file",
            "Data is read or written in order, one record after another from the beginning",
            "Data is accessed using an index table",
            "Data is read in reverse order"
        ],
        "correct_answer": 1,
        "explanation": "Sequential access processes data in a linear, predetermined order. To read record N, you must first read records 1 through N-1."
    },
    {
        "id": 42,
        "type": "multiple_choice",
        "question": "Which stream object is used for standard output in C++?",
        "options": [
            "cin",
            "cerr",
            "clog",
            "cout"
        ],
        "correct_answer": 3,
        "explanation": "cout (character output) is the standard output stream object, typically associated with the console or terminal. It is used with the insertion operator (<<) to display data."
    },
    {
        "id": 43,
        "type": "multiple_choice",
        "question": "What class in C++ is used specifically for reading data from files?",
        "options": [
            "ofstream",
            "wstream",
            "ifstream",
            "readstream"
        ],
        "correct_answer": 2,
        "explanation": "ifstream (input file stream) is the class designed for reading data from files. It provides the extraction operator (>>) and other functions like `getline()` for input."
    },
    {
        "id": 44,
        "type": "multiple_choice",
        "question": "What does it mean that sequential access 'is not very efficient when searching for specific data within large files'?",
        "options": [
            "The file becomes corrupted during search",
            "Every record from the start must be examined until the target is found, making it slow for large datasets",
            "The file pointer cannot move forward in large files",
            "Sequential access deletes records after reading them"
        ],
        "correct_answer": 1,
        "explanation": "Inefficiency in this context refers to the time complexity. In the worst-case scenario (the target is the last record) or if the target doesn't exist, a sequential search must read the entire file, which is very slow for large files."
    },
    {
        "id": 45,
        "type": "multiple_choice",
        "question": "In C++ file handling, what is the significance of the `<fstream>` library compared to `<iostream>`?",
        "options": [
            "<fstream> is used for console I/O while <iostream> is for file I/O",
            "<fstream> provides classes specifically for file I/O (ifstream, ofstream, fstream), while <iostream> handles console I/O (cin, cout)",
            "Both libraries are identical",
            "<fstream> is only available in C++17 and later"
        ],
        "correct_answer": 1,
        "explanation": "<iostream> contains the definitions for basic console streams like cin, cout, cerr, and clog. <fstream> builds upon this by providing classes that allow these stream operations to be directed to and from files."
    },
    {
        "id": 46,
        "type": "multiple_choice",
        "question": "In C++, data stored in RAM is described as 'transient.' This means:",
        "options": [
            "It is permanently stored",
            "It is erased when the application terminates",
            "It is compressed before storage",
            "It is encrypted automatically"
        ],
        "correct_answer": 1,
        "explanation": "'Transient' means temporary or not persistent. Data in RAM is volatile; it requires power to be maintained and is lost when the program that allocated it ends or the computer is shut down."
    },
    {
        "id": 47,
        "type": "multiple_choice",
        "question": "A bank system directly retrieves a customer record using an account number without reading all previous records. This is an example of:",
        "options": [
            "Sequential access",
            "Binary search",
            "Random (direct) access",
            "Indexed sequential access"
        ],
        "correct_answer": 2,
        "explanation": "The key phrase is 'directly retrieves... without reading all previous records'. This is the hallmark of random/direct access. The system likely uses the account number to calculate or look up the exact location of the record on the disk."
    },
    {
        "id": 48,
        "type": "multiple_choice",
        "question": "In random access, how is the byte position of record N (zero-indexed) calculated?",
        "options": [
            "N + record size",
            "N - record size",
            "Record size × N",
            "File size ÷ N"
        ],
        "correct_answer": 2,
        "explanation": "This is the fundamental formula for random access with fixed-size records. Multiplying the zero-based record index by the size of each record gives the exact byte offset from the beginning of the file where that record starts."
    },
    {
        "id": 49,
        "type": "multiple_choice",
        "question": "A file has 1,000 fixed-size records, each 50 bytes long. Using random access, what is the byte offset for record number 7 (zero-indexed)?",
        "options": [
            "7 bytes",
            "350 bytes",
            "357 bytes",
            "700 bytes"
        ],
        "correct_answer": 1,
        "explanation": "Applying the formula: offset = record_number * record_size = 7 * 50 = 350 bytes. The 7th record (which is the 8th record if counting from 1) starts at the 351st byte of the file."
    },
    {
        "id": 50,
        "type": "multiple_choice",
        "question": "If `file.is_open()` returns false, what is the CORRECT action to take?",
        "options": [
            "Continue writing to the file anyway",
            "Handle the error, typically by displaying an error message and exiting or retrying",
            "Delete the file and create a new one",
            "Convert the file to binary format"
        ],
        "correct_answer": 1,
        "explanation": "`is_open()` returning false indicates the file stream failed to establish a connection with the file (e.g., file doesn't exist for reading, or permissions issue). Attempting further I/O operations would be invalid. The correct practice is to handle this error gracefully."
    },
    {
        "id": 51,
        "type": "multiple_choice",
        "question": "Sequential access is described as 'reasonable for tape.' Why?",
        "options": [
            "Tape storage supports fast random positioning",
            "Tape is a magnetic medium that reads data linearly from start to end",
            "Tape uses binary encoding requiring sequential decoding",
            "Tape is exclusively used in modern SSDs"
        ],
        "correct_answer": 1,
        "explanation": "Magnetic tape is a sequential access medium by its physical nature. To read a specific point on a tape, the drive must physically wind the tape to that location, which means passing over all preceding data. This makes it inherently suited for sequential processing."
    },
    {
        "id": 52,
        "type": "multiple_choice",
        "question": "What will the following code print if 'hello.txt' does not exist? `ofstream file(\"hello.txt\"); if (file.is_open()) { file << \"first data.\"; cout << \"Data written.\"; file.close(); } else { cerr << \"Error opening file.\"; }`",
        "options": [
            "Error opening file.",
            "Data written.",
            "Nothing — the program crashes",
            "first data."
        ],
        "correct_answer": 1,
        "explanation": "When an ofstream object is constructed with a filename, it attempts to create the file. If the file doesn't exist, it is created. Therefore, `file.is_open()` will return true, and the 'if' block will execute, printing 'Data written.'"
    },
    {
        "id": 53,
        "type": "multiple_choice",
        "question": "In the student registration program using sequential access, which file mode ensures new records are added without deleting old ones?",
        "options": [
            "ios::in",
            "ios::out",
            "ios::trunc",
            "ios::app"
        ],
        "correct_answer": 3,
        "explanation": "ios::app (append mode) is the correct choice. It ensures that all write operations happen at the end of the file, thus preserving the existing records."
    },
    {
        "id": 54,
        "type": "multiple_choice",
        "question": "What happens when you open a file using `ofstream file(\"test.txt\")` and the file does not already exist?",
        "options": [
            "An error is thrown and the program crashes",
            "Nothing happens — the file is not created",
            "The file is created automatically by ofstream",
            "The program waits for the user to create the file"
        ],
        "correct_answer": 2,
        "explanation": "One of the primary features of ofstream is that if the file specified for output does not exist, it will be created automatically (assuming the file system permissions allow it)."
    },
    {
        "id": 55,
        "type": "multiple_choice",
        "question": "Accessing element at index `i` in an array is an example of which data structure operation?",
        "options": [
            "Reversal",
            "Sorting",
            "Merging",
            "Indexing"
        ],
        "correct_answer": 3,
        "explanation": "Indexing is the operation of accessing an element directly using its position (index) within a data structure. Arrays provide constant-time indexing."
    },
    {
        "id": 56,
        "type": "multiple_choice",
        "question": "When using `ofstream` with no mode specified, what is the default behavior?",
        "options": [
            "The file is opened in read-only mode",
            "The file is opened in append mode",
            "The file is truncated (overwritten) if it already exists",
            "The file is opened in binary mode"
        ],
        "correct_answer": 2,
        "explanation": "By default, ofstream opens a file with `ios::out` mode. For an existing file, this mode discards the old content (truncates the file to zero length) before writing new data, effectively overwriting it."
    },
    {
        "id": 57,
        "type": "multiple_choice",
        "question": "What does the `<<` operator do when used with an ofstream object?",
        "options": [
            "Reads data from the file",
            "Compares two file streams",
            "Writes data to the file",
            "Closes the file"
        ],
        "correct_answer": 2,
        "explanation": "The << operator is the stream insertion operator. When used with an output stream like ofstream, it inserts (or writes) the data on its right-hand side into the stream, which then sends it to the file."
    },
    {
        "id": 58,
        "type": "multiple_choice",
        "question": "In C++, `cerr` is used for error messages instead of `cout` because:",
        "options": [
            "cerr writes to a file automatically",
            "cerr is unbuffered and outputs immediately to standard error stream",
            "cerr is faster for large messages",
            "cerr is only available in <fstream>"
        ],
        "correct_answer": 1,
        "explanation": "The key difference is buffering. `cout` is typically buffered, meaning output might be held temporarily. `cerr` is unbuffered, so any error message sent to it is printed immediately. This is crucial for debugging, especially if a program crashes, ensuring error messages aren't lost in a buffer."
    },
    {
        "id": 59,
        "type": "multiple_choice",
        "question": "What does `file.is_open()` return when a file has been successfully opened?",
        "options": [
            "0",
            "-1",
            "true (non-zero)",
            "NULL"
        ],
        "correct_answer": 2,
        "explanation": "`is_open()` is a member function that returns a boolean value. It returns `true` (which is implicitly converted to a non-zero integer value) if the file stream is successfully associated with an open file, and `false` otherwise."
    },
    {
        "id": 60,
        "type": "multiple_choice",
        "question": "Reversing the order of elements in a stack is an example of which operation?",
        "options": [
            "Merging",
            "Sorting",
            "Reversal",
            "Splitting"
        ],
        "correct_answer": 2,
        "explanation": "Reversal is the operation that changes the order of elements, making the first element the last and the last element the first."
    },
    {
        "id": 61,
        "type": "multiple_choice",
        "question": "Which real-world scenario is BEST suited for sequential access?",
        "options": [
            "Retrieving a specific bank account using an account number",
            "Reading log files from top to bottom to calculate class averages",
            "Directly accessing employee record number 200 out of 500",
            "Searching a database using a primary key"
        ],
        "correct_answer": 1,
        "explanation": "Calculating an average from a log file typically requires processing every record from the beginning to the end, which is a perfect fit for sequential access. The other options require direct access to a specific record, which is inefficient with sequential access."
    },
    {
        "id": 62,
        "type": "multiple_choice",
        "question": "Which access method supports reading or writing data at any block or record using its address without scanning previous records?",
        "options": [
            "Sequential access",
            "Indexed access",
            "Random (direct) access",
            "Linked access"
        ],
        "correct_answer": 2,
        "explanation": "Random (or direct) access is defined by the ability to address any data location directly. The 'address' can be a byte offset, a block number, or a record number, allowing the system to move the read/write head directly to that spot without sequential scanning."
    },
    {
        "id": 63,
        "type": "multiple_choice",
        "question": "Which of the following is a DISADVANTAGE of sequential file access?",
        "options": [
            "It is easy to implement",
            "It processes records in order",
            "It is inefficient when searching for specific records in large files",
            "It is supported by all storage media"
        ],
        "correct_answer": 2,
        "explanation": "This is the primary disadvantage of sequential access. Because you cannot jump directly to a record, any search operation has the potential to be very slow, as it may require reading a significant portion of the file."
    },
    {
        "id": 64,
        "type": "multiple_choice",
        "question": "What does the term 'stream' refer to in C++ file handling?",
        "options": [
            "A database connection",
            "A flow of bytes used to perform input and output operations",
            "A method of encrypting data",
            "A type of variable declaration"
        ],
        "correct_answer": 1,
        "explanation": "In C++ I/O, a stream is an abstract representation of a data source or sink. It acts as a conduit or a 'flow' of bytes between the program and a device (like a file, console, or network connection)."
    },
    {
        "id": 65,
        "type": "multiple_choice",
        "question": "Which statement about the <fstream> header is CORRECT?",
        "options": [
            "It is used only for console input/output",
            "It provides ifstream, ofstream, and fstream classes for file handling",
            "It replaces <iostream> completely",
            "It is only available in C, not C++"
        ],
        "correct_answer": 1,
        "explanation": "The <fstream> header file contains the definitions for the file stream classes: ifstream (input file stream), ofstream (output file stream), and fstream (file stream for both input and output)."
    },
    {
        "id": 66,
        "type": "multiple_choice",
        "question": "A priority queue data structure is mentioned in the slides as being useful for:",
        "options": [
            "Storing hierarchical file systems",
            "Representing computer network topology",
            "Managing process scheduling in operating systems",
            "Implementing routing algorithms in networks"
        ],
        "correct_answer": 2,
        "explanation": "Priority queues are commonly used in OS process scheduling (e.g., the 'ready queue' where the process with the highest priority runs next) and also in algorithms like Dijkstra's for finding the shortest path."
    },
    {
        "id": 67,
        "type": "multiple_choice",
        "question": "In sequential access, what happens to the file pointer after a WRITE operation?",
        "options": [
            "It returns to the beginning",
            "It stays in the same position",
            "Memory is allocated and the pointer moves to the end of file",
            "The file is automatically closed"
        ],
        "correct_answer": 2,
        "explanation": "Similar to reading, after a write operation, the file pointer is automatically advanced. It moves to the position immediately following the data that was just written, ready for the next sequential write operation."
    },
    {
        "id": 68,
        "type": "multiple_choice",
        "question": "A programmer needs to frequently update specific records in a large employee database file. Which access method would be MOST efficient?",
        "options": [
            "Sequential access because it reads all records",
            "Random (direct) access because it can jump directly to any record",
            "Text file access because it is human-readable",
            "Append mode because it preserves all data"
        ],
        "correct_answer": 1,
        "explanation": "For frequent, targeted updates, you need to locate and modify specific records quickly. Random access is designed for this, allowing you to seek directly to the record's location. Sequential access would be far too slow."
    },
    {
        "id": 69,
        "type": "multiple_choice",
        "question": "Which file type is MORE compact and efficient but NOT easily readable in a standard text editor?",
        "options": [
            ".txt file",
            ".csv file",
            "Binary file",
            "Markdown file"
        ],
        "correct_answer": 2,
        "explanation": "Binary files store data in the same format as it is represented in memory. This is often more compact and faster for programs to read/write, but the resulting file is not human-readable because it contains raw bytes, not character codes."
    },
    {
        "id": 70,
        "type": "multiple_choice",
        "question": "Which C++ header file provides classes for file input and output operations?",
        "options": [
            "<iostream>",
            "<stdio.h>",
            "<fstream>",
            "<fileio>"
        ],
        "correct_answer": 2,
        "explanation": "<fstream> is the correct header. It provides the file stream classes like ifstream, ofstream, and fstream."
    },
    {
        "id": 71,
        "type": "multiple_choice",
        "question": "A student mistakenly uses `ifstream` to write data to a file. What will happen?",
        "options": [
            "The data is written successfully",
            "The file is deleted",
            "A compile-time or runtime error will occur since ifstream is for reading only",
            "The data is written in binary format"
        ],
        "correct_answer": 2,
        "explanation": "ifstream is derived from `istream`, which is designed for input. It does not have the necessary methods (like the << operator) for output. This will likely result in a compiler error, as the stream object won't have the member functions or operators needed for writing."
    },
    {
        "id": 72,
        "type": "multiple_choice",
        "question": "Which of the following is an example of a text file?",
        "options": [
            "image.png",
            "program.exe",
            "data.csv",
            "archive.bin"
        ],
        "correct_answer": 2,
        "explanation": "A .csv (Comma-Separated Values) file stores tabular data in plain text, with each line representing a row and commas separating the values. It can be opened and read in any text editor."
    },
    {
        "id": 73,
        "type": "multiple_choice",
        "question": "In the student registration program, what does `getline(cin, studentName)` do differently from `cin >> studentName`?",
        "options": [
            "It reads only the first word",
            "It reads a single character",
            "It reads the entire line including spaces",
            "It reads data from a file, not keyboard"
        ],
        "correct_answer": 2,
        "explanation": "The extraction operator (`>>`) is whitespace-delimited, meaning it stops reading when it encounters a space, tab, or newline. `getline()` reads all characters until it reaches a newline character, making it capable of reading strings that contain spaces (like a full name)."
    },
    {
        "id": 74,
        "type": "multiple_choice",
        "question": "Binary files differ from text files because they:",
        "options": [
            "Are always larger than text files",
            "Store data in raw machine-level format not easily human-readable",
            "Can only store integers",
            "Are only used in operating systems"
        ],
        "correct_answer": 1,
        "explanation": "Text files store data as a sequence of characters (using an encoding like ASCII or UTF-8). Binary files store data in the same format as it is stored in memory, which is a sequence of bytes that may represent integers, floats, or other data structures directly. This raw format is not intended to be human-readable."
    },
    {
        "id": 75,
        "type": "multiple_choice",
        "question": "Which is more suitable for processing large amounts of sequential data like audit logs?",
        "options": [
            "Random access with fixed records",
            "Sequential access reading record by record",
            "Binary search on a sorted array",
            "Direct access using account numbers"
        ],
        "correct_answer": 1,
        "explanation": "Audit logs are typically processed in chronological order, from oldest to newest. Sequential access is perfectly suited for this type of 'streaming' data processing, as it reads the data in the order it was written."
    },
    {
        "id": 76,
        "type": "multiple_choice",
        "question": "In C++ file handling, what does `endl` do when written to a file stream?",
        "options": [
            "Ends the program",
            "Writes a newline character and flushes the stream buffer",
            "Closes the file",
            "Moves the file pointer to the beginning"
        ],
        "correct_answer": 1,
        "explanation": "`endl` is a manipulator. When inserted into a stream, it does two things: it inserts a newline character ('\\n') into the stream, and then it calls `flush()` on the stream, which forces any buffered data to be written to the destination (the file)."
    },
    {
        "id": 77,
        "type": "multiple_choice",
        "question": "Which of the following correctly describes the formula for finding a record's byte position in random access?",
        "options": [
            "Position = file size / record number",
            "Position = record size × record number",
            "Position = record size + record number",
            "Position = record number - record size"
        ],
        "correct_answer": 1,
        "explanation": "For a zero-indexed record number, the correct formula is `record_number * record_size`. This gives the exact byte offset from the beginning of the file."
    },
    {
        "id": 78,
        "type": "multiple_choice",
        "question": "What does the `>>` operator do when used with an ifstream object?",
        "options": [
            "Writes data to the file",
            "Reads data from the file into a variable",
            "Deletes data from the file",
            "Moves the file pointer backward"
        ],
        "correct_answer": 1,
        "explanation": "The `>>` operator is the stream extraction operator. When used with an input stream like ifstream, it extracts data from the stream (the file) and stores it in the provided variable."
    },
    {
        "id": 79,
        "type": "multiple_choice",
        "question": "Which of the following is an ADVANTAGE of random access over sequential access?",
        "options": [
            "Simpler implementation",
            "Works well with tape storage",
            "Can retrieve any specific record without reading all preceding records",
            "Requires less disk space"
        ],
        "correct_answer": 2,
        "explanation": "This is the main advantage of random access. It provides fast, direct access to any data item, which is essential for applications like databases or interactive systems where specific records need to be retrieved quickly."
    },
    {
        "id": 80,
        "type": "multiple_choice",
        "question": "A school examination system reads all student records from the beginning to calculate the class average. Which file access method is this?",
        "options": [
            "Direct access",
            "Random access",
            "Sequential access",
            "Binary file access"
        ],
        "correct_answer": 2,
        "explanation": "The key phrase is 'reads all student records from the beginning'. This is the defining characteristic of sequential access. To calculate the average, the program must process every record in the order they are stored."
    }
    ]
}
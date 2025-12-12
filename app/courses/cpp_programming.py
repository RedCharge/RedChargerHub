cpp_programming_quiz = {
    "course_code": "BCP 203",
    "course_name": "Computer Organization Architecture",
    "total_questions": 50,
    "questions": [
    {
        "id": 1,
        "type": "multiple_choice",
        "question": "What is the correct syntax to output 'Hello World' in C++?",
        "options": [
            "System.out.println('Hello World');",
            "cout << 'Hello World';",
            "printf('Hello World');",
            "Console.WriteLine('Hello World');"
        ],
        "correct_answer": 1,
        "explanation": "In C++, cout << is used to output text to the console. The << operator is called the insertion operator."
    },
    {
        "id": 2,
        "type": "multiple_choice",
        "question": "Which header file is required for input/output operations in C++?",
        "options": [
            "<stdio.h>",
            "<iostream>",
            "<inputoutput>",
            "<console.h>"
        ],
        "correct_answer": 1,
        "explanation": "<iostream> is the standard header file for input/output operations in C++. It contains declarations for cout, cin, etc."
    },
    {
        "id": 3,
        "type": "multiple_choice",
        "question": "What does the 'using namespace std;' statement do?",
        "options": [
            "It imports all standard library functions",
            "It allows you to use standard library names without std:: prefix",
            "It declares a new namespace called 'std'",
            "It includes all header files automatically"
        ],
        "correct_answer": 1,
        "explanation": "'using namespace std;' brings all names from the std namespace into the current scope, so you don't need to write std:: before cout, cin, etc."
    },
    {
        "id": 4,
        "type": "true_false",
        "question": "Every C++ program must have a main() function.",
        "options": [
            "True",
            "False"
        ],
        "correct_answer": 0,
        "explanation": "True. Every C++ program must have exactly one main() function, which is the entry point of the program."
    },
    {
        "id": 5,
        "type": "multiple_choice",
        "question": "Which of these is a valid comment in C++?",
        "options": [
            "<!-- This is a comment -->",
            "/* This is a comment */",
            "# This is a comment",
            "' This is a comment"
        ],
        "correct_answer": 1,
        "explanation": "C++ supports two types of comments: single-line comments starting with // and multi-line comments between /* and */."
    },
    {
        "id": 6,
        "type": "multiple_choice",
        "question": "What is the size of an 'int' data type in C++ on most 32-bit systems?",
        "options": [
            "1 byte",
            "2 bytes",
            "4 bytes",
            "8 bytes"
        ],
        "correct_answer": 2,
        "explanation": "On most 32-bit systems, an int is 4 bytes (32 bits). However, the exact size can vary depending on the compiler and system architecture."
    },
    {
        "id": 7,
        "type": "multiple_choice",
        "question": "Which operator is used to assign a value to a variable?",
        "options": [
            "==",
            "=",
            ":=",
            "=>"
        ],
        "correct_answer": 1,
        "explanation": "The = operator is the assignment operator used to assign a value to a variable."
    },
    {
        "id": 8,
        "type": "multiple_choice",
        "question": "What is the output of: cout << 5/2;",
        "options": [
            "2.5",
            "2",
            "2.0",
            "2.500000"
        ],
        "correct_answer": 1,
        "explanation": "When both operands are integers, the division operator performs integer division, so 5/2 results in 2 (the decimal part is truncated)."
    },
    {
        "id": 9,
        "type": "true_false",
        "question": "In C++, 'float' and 'double' are both used for floating-point numbers, but 'double' has higher precision.",
        "options": [
            "True",
            "False"
        ],
        "correct_answer": 0,
        "explanation": "True. 'float' typically uses 4 bytes (single precision) while 'double' uses 8 bytes (double precision), giving it higher precision."
    },
    {
        "id": 10,
        "type": "multiple_choice",
        "question": "Which of these is NOT a valid variable name in C++?",
        "options": [
            "_myVar",
            "myVar123",
            "123myVar",
            "my_var"
        ],
        "correct_answer": 2,
        "explanation": "Variable names cannot start with a digit. They must start with a letter or underscore."
    },
    {
        "id": 11,
        "type": "multiple_choice",
        "question": "What is the output of: cout << (10 > 9);",
        "options": [
            "10",
            "9",
            "1",
            "true"
        ],
        "correct_answer": 2,
        "explanation": "In C++, relational operators return 1 for true and 0 for false. Since 10 > 9 is true, it outputs 1."
    },
    {
        "id": 12,
        "type": "multiple_choice",
        "question": "Which loop executes at least once even if the condition is false initially?",
        "options": [
            "for loop",
            "while loop",
            "do-while loop",
            "if-else loop"
        ],
        "correct_answer": 2,
        "explanation": "The do-while loop executes the body first, then checks the condition, so it always executes at least once."
    },
    {
        "id": 13,
        "type": "true_false",
        "question": "The 'break' statement is used to exit from a loop or switch statement.",
        "options": [
            "True",
            "False"
        ],
        "correct_answer": 0,
        "explanation": "True. The break statement terminates the loop or switch statement and transfers execution to the statement immediately following."
    },
    {
        "id": 14,
        "type": "multiple_choice",
        "question": "What does the '++' operator do?",
        "options": [
            "Adds 2 to a variable",
            "Multiplies a variable by itself",
            "Increments a variable by 1",
            "Checks if a variable is positive"
        ],
        "correct_answer": 2,
        "explanation": "The ++ operator is the increment operator. It increases the value of a variable by 1."
    },
    {
        "id": 15,
        "type": "multiple_choice",
        "question": "Which of these is the correct way to declare an array of 5 integers?",
        "options": [
            "int array[5];",
            "array int[5];",
            "int[5] array;",
            "array[5] int;"
        ],
        "correct_answer": 0,
        "explanation": "The correct syntax is: type name[size]; So for an array of 5 integers: int array[5];"
    },
    {
        "id": 16,
        "type": "multiple_choice",
        "question": "What is the index of the first element in an array?",
        "options": [
            "0",
            "1",
            "-1",
            "Depends on the array declaration"
        ],
        "correct_answer": 0,
        "explanation": "In C++, array indices start at 0, so the first element is at index 0."
    },
    {
        "id": 17,
        "type": "true_false",
        "question": "In C++, a function can return multiple values using the return statement.",
        "options": [
            "True",
            "False"
        ],
        "correct_answer": 1,
        "explanation": "False. A function can only return one value directly. To return multiple values, you can use pointers, references, structures, or arrays."
    },
    {
        "id": 18,
        "type": "multiple_choice",
        "question": "Which keyword is used to define a function in C++?",
        "options": [
            "def",
            "function",
            "void",
            "No specific keyword is required"
        ],
        "correct_answer": 3,
        "explanation": "In C++, functions are defined by specifying the return type followed by the function name and parameters. No special keyword like 'def' or 'function' is needed."
    },
    {
        "id": 19,
        "type": "multiple_choice",
        "question": "What is the purpose of the 'return' statement in a function?",
        "options": [
            "To print a value",
            "To exit the program",
            "To send a value back to the calling code",
            "To pause the function execution"
        ],
        "correct_answer": 2,
        "explanation": "The return statement sends a value back to the calling code and exits the function."
    },
    {
        "id": 20,
        "type": "multiple_choice",
        "question": "Which of these is a valid function declaration?",
        "options": [
            "function add(int a, int b)",
            "int add(int a, int b)",
            "def add(int a, int b)",
            "add(int a, int b): int"
        ],
        "correct_answer": 1,
        "explanation": "The correct syntax is: return_type function_name(parameters). So 'int add(int a, int b)' is valid."
    },
    {
        "id": 21,
        "type": "true_false",
        "question": "In C++, all variables must be declared before they are used.",
        "options": [
            "True",
            "False"
        ],
        "correct_answer": 0,
        "explanation": "True. C++ requires all variables to be declared with their type before they can be used."
    },
    {
        "id": 22,
        "type": "multiple_choice",
        "question": "What does the 'cin' object do?",
        "options": [
            "It outputs data to the console",
            "It reads input from the user",
            "It checks if input is valid",
            "It converts input to uppercase"
        ],
        "correct_answer": 1,
        "explanation": "cin (character input) is used to read input from the standard input (usually keyboard)."
    },
    {
        "id": 23,
        "type": "multiple_choice",
        "question": "What is the output of: cout << sizeof(char);",
        "options": [
            "1",
            "2",
            "4",
            "8"
        ],
        "correct_answer": 0,
        "explanation": "The sizeof operator returns the size in bytes. A char is always 1 byte in C++."
    },
    {
        "id": 24,
        "type": "multiple_choice",
        "question": "Which operator is used for logical AND?",
        "options": [
            "&&",
            "||",
            "!",
            "&"
        ],
        "correct_answer": 0,
        "explanation": "&& is the logical AND operator. It returns true only if both operands are true."
    },
    {
        "id": 25,
        "type": "true_false",
        "question": "A 'switch' statement can be used instead of multiple 'if-else if' statements when checking the same variable against different values.",
        "options": [
            "True",
            "False"
        ],
        "correct_answer": 0,
        "explanation": "True. A switch statement provides a cleaner way to handle multiple conditions on the same variable."
    },
    {
        "id": 26,
        "type": "multiple_choice",
        "question": "What is a pointer in C++?",
        "options": [
            "A variable that stores the address of another variable",
            "A variable that stores multiple values",
            "A special type of array",
            "A function that points to another function"
        ],
        "correct_answer": 0,
        "explanation": "A pointer is a variable that stores the memory address of another variable."
    },
    {
        "id": 27,
        "type": "multiple_choice",
        "question": "Which operator is used to get the address of a variable?",
        "options": [
            "*",
            "&",
            "->",
            "::"
        ],
        "correct_answer": 1,
        "explanation": "The & operator is the address-of operator. It returns the memory address of a variable."
    },
    {
        "id": 28,
        "type": "multiple_choice",
        "question": "What does the '*' operator do when used with pointers?",
        "options": [
            "Gets the address of a variable",
            "Declares a pointer variable",
            "Dereferences a pointer (gets the value at the address)",
            "Multiplies two pointers"
        ],
        "correct_answer": 2,
        "explanation": "The * operator, when used with pointers, is the dereference operator. It accesses the value stored at the memory address the pointer points to."
    },
    {
        "id": 29,
        "type": "true_false",
        "question": "In C++, the 'new' operator is used to dynamically allocate memory.",
        "options": [
            "True",
            "False"
        ],
        "correct_answer": 0,
        "explanation": "True. The 'new' operator allocates memory dynamically on the heap and returns a pointer to it."
    },
    {
        "id": 30,
        "type": "multiple_choice",
        "question": "What is the purpose of the 'delete' operator?",
        "options": [
            "To remove a variable",
            "To free dynamically allocated memory",
            "To delete a file",
            "To remove an element from an array"
        ],
        "correct_answer": 1,
        "explanation": "The 'delete' operator deallocates memory that was previously allocated with 'new'."
    },
    {
        "id": 31,
        "type": "multiple_choice",
        "question": "What is a reference in C++?",
        "options": [
            "A pointer that cannot be changed",
            "An alias for an existing variable",
            "A constant pointer",
            "A pointer to a pointer"
        ],
        "correct_answer": 1,
        "explanation": "A reference is an alias for an existing variable. It must be initialized when declared and cannot be made to refer to a different variable later."
    },
    {
        "id": 32,
        "type": "multiple_choice",
        "question": "Which of these correctly declares a reference to an integer variable x?",
        "options": [
            "int ref = x;",
            "int &ref = x;",
            "int *ref = x;",
            "ref int = x;"
        ],
        "correct_answer": 1,
        "explanation": "The correct syntax is: type &reference_name = variable_name; So 'int &ref = x;' declares ref as a reference to x."
    },
    {
        "id": 33,
        "type": "true_false",
        "question": "In C++, structures (struct) can contain both data members and member functions.",
        "options": [
            "True",
            "False"
        ],
        "correct_answer": 0,
        "explanation": "True. Unlike C, C++ structs can have member functions (methods) as well as data members."
    },
    {
        "id": 34,
        "type": "multiple_choice",
        "question": "What is the default access specifier for members of a class in C++?",
        "options": [
            "public",
            "private",
            "protected",
            "Depends on the compiler"
        ],
        "correct_answer": 1,
        "explanation": "For classes, the default access specifier is private. For structs, the default is public."
    },
    {
        "id": 35,
        "type": "multiple_choice",
        "question": "What is a constructor?",
        "options": [
            "A function that destroys an object",
            "A special member function that initializes objects",
            "A function that converts between types",
            "A function that allocates memory"
        ],
        "correct_answer": 1,
        "explanation": "A constructor is a special member function that is automatically called when an object is created, used to initialize the object."
    },
    {
        "id": 36,
        "type": "multiple_choice",
        "question": "Which of these is NOT a type of constructor?",
        "options": [
            "Default constructor",
            "Parameterized constructor",
            "Copy constructor",
            "Destructor constructor"
        ],
        "correct_answer": 3,
        "explanation": "Destructor is not a type of constructor. It's a separate function that destroys objects. Constructors include default, parameterized, and copy constructors."
    },
    {
        "id": 37,
        "type": "true_false",
        "question": "Function overloading allows multiple functions with the same name but different parameters.",
        "options": [
            "True",
            "False"
        ],
        "correct_answer": 0,
        "explanation": "True. Function overloading is a feature that allows creating multiple functions with the same name but different parameter lists."
    },
    {
        "id": 38,
        "type": "multiple_choice",
        "question": "What is inheritance in C++?",
        "options": [
            "Creating multiple objects from a class",
            "A mechanism where a new class derives properties from an existing class",
            "Passing parameters to functions",
            "Allocating memory for objects"
        ],
        "correct_answer": 1,
        "explanation": "Inheritance is an OOP concept where a new class (derived class) inherits properties and behaviors from an existing class (base class)."
    },
    {
        "id": 39,
        "type": "multiple_choice",
        "question": "Which keyword is used for inheritance?",
        "options": [
            "inherits",
            "extends",
            ":",
            "derive"
        ],
        "correct_answer": 2,
        "explanation": "In C++, inheritance is specified using a colon (:). For example: class Derived : public Base"
    },
    {
        "id": 40,
        "type": "multiple_choice",
        "question": "What is polymorphism?",
        "options": [
            "Having multiple forms",
            "Using the same function name for different purposes",
            "Both A and B",
            "None of the above"
        ],
        "correct_answer": 2,
        "explanation": "Polymorphism means 'many forms'. In C++, it allows functions or operators to have different implementations based on the objects they are acting upon."
    },
    {
        "id": 41,
        "type": "true_false",
        "question": "Virtual functions enable runtime polymorphism in C++.",
        "options": [
            "True",
            "False"
        ],
        "correct_answer": 0,
        "explanation": "True. Virtual functions allow derived classes to override base class functions, and the correct function is called at runtime based on the actual object type."
    },
    {
        "id": 42,
        "type": "multiple_choice",
        "question": "What is an abstract class?",
        "options": [
            "A class with no data members",
            "A class that cannot be instantiated",
            "A class with only private members",
            "A class that inherits from multiple classes"
        ],
        "correct_answer": 1,
        "explanation": "An abstract class is a class that contains at least one pure virtual function and cannot be instantiated. It's designed to be inherited by other classes."
    },
    {
        "id": 43,
        "type": "multiple_choice",
        "question": "Which operator is used for dynamic memory allocation?",
        "options": [
            "alloc",
            "malloc",
            "new",
            "create"
        ],
        "correct_answer": 2,
        "explanation": "The 'new' operator is used for dynamic memory allocation in C++. It allocates memory on the heap and returns a pointer to it."
    },
    {
        "id": 44,
        "type": "multiple_choice",
        "question": "What is the purpose of exception handling?",
        "options": [
            "To prevent all errors",
            "To handle runtime errors gracefully",
            "To improve program speed",
            "To reduce code size"
        ],
        "correct_answer": 1,
        "explanation": "Exception handling allows a program to handle runtime errors gracefully, preventing crashes and allowing for recovery or clean termination."
    },
    {
        "id": 45,
        "type": "multiple_choice",
        "question": "Which keywords are used for exception handling?",
        "options": [
            "try, catch, finally",
            "try, catch, throw",
            "try, except, throw",
            "try, handle, throw"
        ],
        "correct_answer": 1,
        "explanation": "C++ uses try, catch, and throw for exception handling. 'finally' is used in some other languages like Java, but not in standard C++."
    },
    {
        "id": 46,
        "type": "true_false",
        "question": "Templates in C++ allow writing generic code that works with different data types.",
        "options": [
            "True",
            "False"
        ],
        "correct_answer": 0,
        "explanation": "True. Templates enable generic programming by allowing functions and classes to operate with generic types."
    },
    {
        "id": 47,
        "type": "multiple_choice",
        "question": "What is the Standard Template Library (STL)?",
        "options": [
            "A collection of template classes and functions",
            "A set of standard headers",
            "A compiler feature",
            "A debugging tool"
        ],
        "correct_answer": 0,
        "explanation": "STL is a powerful set of C++ template classes and functions that provide common data structures and algorithms."
    },
    {
        "id": 48,
        "type": "multiple_choice",
        "question": "Which of these is an STL container?",
        "options": [
            "vector",
            "array",
            "list",
            "All of the above"
        ],
        "correct_answer": 3,
        "explanation": "All are STL containers. vector, array, and list are part of the STL container library."
    },
    {
        "id": 49,
        "type": "multiple_choice",
        "question": "What does the 'auto' keyword do in modern C++?",
        "options": [
            "Automatically deallocates memory",
            "Automatically determines variable type from initializer",
            "Creates automatic variables",
            "Automatically includes headers"
        ],
        "correct_answer": 1,
        "explanation": "The 'auto' keyword (in C++11 and later) automatically deduces the type of a variable from its initializer."
    },
    {
        "id": 50,
        "type": "true_false",
        "question": "C++ supports both procedural and object-oriented programming paradigms.",
        "options": [
            "True",
            "False"
        ],
        "correct_answer": 0,
        "explanation": "True. C++ is a multi-paradigm language that supports procedural, object-oriented, and generic programming."
    }
] }
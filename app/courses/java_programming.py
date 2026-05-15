java_programming_quiz = {
    "course_code": "BCP 203",
    "course_name": "Programmimg with java",
    "total_questions": 80,
    "questions": [
    
    
    {
        "id": 1,
        "type": "multiple_choice",
        "question": "Which company owns Oracle Java?",
        "options": ["IBM", "Oracle", "Microsoft", "Apple"],
        "correct_answer": 1,
        "explanation": "Oracle Corporation acquired Sun Microsystems in 2010 and now owns and maintains Java."
    },
    {
        "id": 2,
        "type": "multiple_choice",
        "question": "What is the output of: System.out.println(5 + 2 * 3);",
        "options": ["21", "11", "16", "13"],
        "correct_answer": 1,
        "explanation": "Multiplication has higher precedence than addition, so 2 * 3 = 6, then 5 + 6 = 11."
    },
    {
        "id": 3,
        "type": "multiple_choice",
        "question": "Which component executes Java bytecode?",
        "options": ["JDK", "JVM", "JRE", "javac"],
        "correct_answer": 1,
        "explanation": "The Java Virtual Machine (JVM) interprets or compiles bytecode into native machine code for execution."
    },
    {
        "id": 4,
        "type": "multiple_choice",
        "question": "What is wrong with this line? System.out.println(\"Hello\")",
        "options": ["Missing semicolon", "Wrong brackets", "Wrong keyword", "No error"],
        "correct_answer": 0,
        "explanation": "Java statements must end with a semicolon (;). The correct line is System.out.println(\"Hello\");"
    },
    {
        "id": 5,
        "type": "multiple_choice",
        "question": "Which keyword defines a class in Java?",
        "options": ["define", "object", "class", "create"],
        "correct_answer": 2,
        "explanation": "The 'class' keyword is used to declare a new class in Java."
    },
    {
        "id": 6,
        "type": "multiple_choice",
        "question": "What is the output of: int x = 10; System.out.println(x++);",
        "options": ["11", "9", "10", "Error"],
        "correct_answer": 2,
        "explanation": "Post-increment (x++) returns the current value (10) before incrementing."
    },
    {
        "id": 7,
        "type": "multiple_choice",
        "question": "Which command compiles a Java program?",
        "options": ["java Test.java", "javac Test.java", "run Test.java", "compile Test.java"],
        "correct_answer": 1,
        "explanation": "The javac command (Java compiler) compiles .java source files into .class bytecode files."
    },
    {
        "id": 8,
        "type": "multiple_choice",
        "question": "Which data type stores decimal numbers?",
        "options": ["int", "boolean", "double", "char"],
        "correct_answer": 2,
        "explanation": "double stores floating-point decimal numbers with double precision."
    },
    {
        "id": 9,
        "type": "multiple_choice",
        "question": "What is the output of: System.out.println(10 / 4);",
        "options": ["2.5", "2", "3", "2.0"],
        "correct_answer": 1,
        "explanation": "Integer division truncates the decimal part, so 10/4 = 2 (not 2.5)."
    },
    {
        "id": 10,
        "type": "multiple_choice",
        "question": "Which statement about Java is TRUE?",
        "options": ["Java is case-insensitive", "Java files use .js", "Java is case-sensitive", "Java has no classes"],
        "correct_answer": 2,
        "explanation": "Java is case-sensitive, meaning 'Hello' and 'hello' are different identifiers."
    },
    {
        "id": 11,
        "type": "multiple_choice",
        "question": "Which symbol starts a single-line comment?",
        "options": ["##", "//", "<!--", "%%"],
        "correct_answer": 1,
        "explanation": "// begins a single-line comment in Java. Everything after // is ignored by the compiler."
    },
    {
        "id": 12,
        "type": "multiple_choice",
        "question": "What is the output of: System.out.println(\"3\" + 2);",
        "options": ["5", "32", "Error", "6"],
        "correct_answer": 1,
        "explanation": "String concatenation: '3' + 2 = '32' because one operand is a String."
    },
    {
        "id": 13,
        "type": "multiple_choice",
        "question": "Which Scanner method reads a full line?",
        "options": ["next()", "nextInt()", "nextLine()", "nextDouble()"],
        "correct_answer": 2,
        "explanation": "nextLine() reads the entire line including spaces until the newline character."
    },
    {
        "id": 14,
        "type": "multiple_choice",
        "question": "What is the output of: char grade = 'A'; System.out.println(grade);",
        "options": ["65", "A", "Error", "\"A\""],
        "correct_answer": 1,
        "explanation": "The char variable stores a single character, and println prints the character 'A'."
    },
    {
        "id": 15,
        "type": "multiple_choice",
        "question": "What does JDK stand for?",
        "options": ["Java Debug Kit", "Java Development Kit", "Java Design Kit", "Java Documentation Kit"],
        "correct_answer": 1,
        "explanation": "JDK (Java Development Kit) includes tools for developing Java programs, including the compiler and JRE."
    },
    {
        "id": 16,
        "type": "multiple_choice",
        "question": "What is the output of: System.out.println(4 % 3);",
        "options": ["0", "1", "3", "4"],
        "correct_answer": 1,
        "explanation": "% is the modulo operator, giving the remainder when 4 is divided by 3, which is 1."
    },
    {
        "id": 17,
        "type": "multiple_choice",
        "question": "Which file extension is used for Java source files?",
        "options": [".class", ".exe", ".java", ".js"],
        "correct_answer": 2,
        "explanation": "Java source files use the .java extension, which are compiled into .class files."
    },
    {
        "id": 18,
        "type": "multiple_choice",
        "question": "Which operator means AND in Java?",
        "options": ["||", "&&", "!!", "=="],
        "correct_answer": 1,
        "explanation": "&& is the logical AND operator, returning true only if both operands are true."
    },
    {
        "id": 19,
        "type": "multiple_choice",
        "question": "What is wrong with this declaration: int age = \"20\";",
        "options": ["Missing semicolon", "int cannot store text", "Wrong variable name", "No error"],
        "correct_answer": 1,
        "explanation": "int variables store numeric values, not Strings. Quotes make '20' a String literal."
    },
    {
        "id": 20,
        "type": "multiple_choice",
        "question": "What is the output of: System.out.println((2 + 3) * 2);",
        "options": ["7", "10", "12", "5"],
        "correct_answer": 1,
        "explanation": "Parentheses have highest precedence: (2+3)=5, then 5*2=10."
    },
    {
        "id": 21,
        "type": "multiple_choice",
        "question": "Which method reads integers using Scanner?",
        "options": ["next()", "nextLine()", "nextInt()", "nextDouble()"],
        "correct_answer": 2,
        "explanation": "nextInt() reads an integer value from the input stream."
    },
    {
        "id": 22,
        "type": "multiple_choice",
        "question": "Which of these is NOT a primitive type?",
        "options": ["int", "boolean", "String", "char"],
        "correct_answer": 2,
        "explanation": "String is a reference type (class) in Java, not a primitive type. Primitives are int, boolean, char, double, etc."
    },
    {
        "id": 23,
        "type": "multiple_choice",
        "question": "What is the output of: boolean pass = true; System.out.println(pass);",
        "options": ["TRUE", "true", "1", "False"],
        "correct_answer": 1,
        "explanation": "println outputs the boolean literal 'true' in lowercase."
    },
    {
        "id": 24,
        "type": "multiple_choice",
        "question": "What does JVM stand for?",
        "options": ["Java Virtual Machine", "Java Variable Machine", "Java Vendor Machine", "Java Visual Machine"],
        "correct_answer": 0,
        "explanation": "JVM (Java Virtual Machine) executes Java bytecode and provides platform independence."
    },
    {
        "id": 25,
        "type": "multiple_choice",
        "question": "Which line correctly creates a Scanner object?",
        "options": [
            "Scanner sc = new Scanner(System.in);",
            "Scanner sc = Scanner(System.in);",
            "scanner sc = new scanner();",
            "input Scanner = new input();"
        ],
        "correct_answer": 0,
        "explanation": "Correct syntax: 'new Scanner(System.in)' creates a Scanner reading from standard input."
    },
    {
        "id": 26,
        "type": "multiple_choice",
        "question": "What is the output of: int x = 5; x += 3; System.out.println(x);",
        "options": ["5", "3", "8", "15"],
        "correct_answer": 2,
        "explanation": "x += 3 is shorthand for x = x + 3, so 5 + 3 = 8."
    },
    {
        "id": 27,
        "type": "multiple_choice",
        "question": "Which company originally created Java?",
        "options": ["IBM", "Oracle", "Sun Microsystems", "Intel"],
        "correct_answer": 2,
        "explanation": "Sun Microsystems developed Java in 1995, led by James Gosling. Oracle acquired Sun in 2010."
    },
    {
        "id": 28,
        "type": "multiple_choice",
        "question": "What is the output of: System.out.println(\"Java\".length());",
        "options": ["3", "4", "5", "Error"],
        "correct_answer": 1,
        "explanation": "length() returns the number of characters in the String: 'J','a','v','a' = 4."
    },
    {
        "id": 29,
        "type": "multiple_choice",
        "question": "Which symbol ends a Java statement correctly?",
        "options": [":", ";", ",", "#"],
        "correct_answer": 1,
        "explanation": "Semicolons (;) terminate statements in Java, similar to C/C++."
    },
    {
        "id": 30,
        "type": "multiple_choice",
        "question": "What is the output of: System.out.println(7 > 3);",
        "options": ["true", "false", "1", "Error"],
        "correct_answer": 0,
        "explanation": "The comparison operator > returns a boolean value: true if 7 is greater than 3."
    },
    {
        "id": 31,
        "type": "multiple_choice",
        "question": "Which keyword creates an object in Java?",
        "options": ["object", "create", "new", "class"],
        "correct_answer": 2,
        "explanation": "The 'new' keyword allocates memory and creates an object instance of a class."
    },
    {
        "id": 32,
        "type": "multiple_choice",
        "question": "What is the output of: System.out.println(\"A\" + \"TU\");",
        "options": ["A TU", "ATU", "TUA", "Error"],
        "correct_answer": 1,
        "explanation": "String concatenation joins 'A' and 'TU' to form 'ATU'."
    },
    {
        "id": 33,
        "type": "multiple_choice",
        "question": "Which method reads decimal values?",
        "options": ["nextInt()", "nextLine()", "nextDouble()", "next()"],
        "correct_answer": 2,
        "explanation": "nextDouble() reads a floating-point decimal number from the Scanner input."
    },
    {
        "id": 34,
        "type": "multiple_choice",
        "question": "What is the output of: int a = 2; int b = 3; System.out.println(a * b + 1);",
        "options": ["5", "6", "7", "8"],
        "correct_answer": 2,
        "explanation": "Multiplication before addition: 2*3=6, then 6+1=7."
    },
    {
        "id": 35,
        "type": "multiple_choice",
        "question": "Which line is valid?",
        "options": [
            "double gpa = 3.5;",
            "double = 3.5 gpa;",
            "gpa double = 3.5;",
            "double gpa : 3.5;"
        ],
        "correct_answer": 0,
        "explanation": "Valid variable declaration: type (double) followed by name (gpa) then assignment (= 3.5) and semicolon."
    },
    {
        "id": 36,
        "type": "multiple_choice",
        "question": "Which command runs a Java program?",
        "options": ["javac Hello.java", "java Hello", "compile Hello", "run Hello.java"],
        "correct_answer": 1,
        "explanation": "The java command executes the compiled .class file (without the .class extension)."
    },
    {
        "id": 37,
        "type": "multiple_choice",
        "question": "What is the output of: System.out.println(9 / 2.0);",
        "options": ["4", "4.5", "5", "4.0"],
        "correct_answer": 1,
        "explanation": "When one operand is double, division produces a double result: 9 / 2.0 = 4.5."
    },
    {
        "id": 38,
        "type": "multiple_choice",
        "question": "Which operator gives remainder?",
        "options": ["/", "*", "%", "+"],
        "correct_answer": 2,
        "explanation": "% is the modulo (remainder) operator."
    },
    {
        "id": 39,
        "type": "multiple_choice",
        "question": "What is the output of: String name = \"Ama\"; System.out.println(name.toUpperCase());",
        "options": ["ama", "Ama", "AMA", "Error"],
        "correct_answer": 2,
        "explanation": "toUpperCase() converts all characters to uppercase: 'Ama' becomes 'AMA'."
    },
    {
        "id": 40,
        "type": "multiple_choice",
        "question": "Which is a correct variable name?",
        "options": ["2name", "student-name", "studentName", "student name"],
        "correct_answer": 2,
        "explanation": "studentName uses camelCase, starts with a letter, no spaces or hyphens. Hyphens and spaces are invalid; numbers cannot start identifiers."
    },
    {
        "id": 41,
        "type": "multiple_choice",
        "question": "What is the output of: System.out.println(5 == 5);",
        "options": ["true", "false", "5", "Error"],
        "correct_answer": 0,
        "explanation": "== compares equality, returning true when both sides are equal."
    },
    {
        "id": 42,
        "type": "multiple_choice",
        "question": "Which package contains Scanner?",
        "options": ["java.lang", "java.util", "java.io", "java.net"],
        "correct_answer": 1,
        "explanation": "Scanner is in java.util package, requiring import java.util.Scanner;"
    },
    {
        "id": 43,
        "type": "multiple_choice",
        "question": "What is the output of: System.out.println(\"Java\".charAt(2));",
        "options": ["J", "a", "v", "Error"],
        "correct_answer": 2,
        "explanation": "charAt(2) returns the character at index 2: indices 0='J', 1='a', 2='v', 3='a'."
    },
    {
        "id": 44,
        "type": "multiple_choice",
        "question": "Which loop repeats while a condition is true?",
        "options": ["switch", "if", "while", "break"],
        "correct_answer": 2,
        "explanation": "The while loop repeats execution of a block as long as its boolean condition remains true."
    },
    {
        "id": 45,
        "type": "multiple_choice",
        "question": "What is the output of: int x = 1; x++; x++; System.out.println(x);",
        "options": ["1", "2", "3", "4"],
        "correct_answer": 2,
        "explanation": "x++ increments x by 1 each time: 1 → 2 → 3."
    },
    {
        "id": 46,
        "type": "multiple_choice",
        "question": "Which symbol is used for modulo?",
        "options": ["&", "%", "#", "@"],
        "correct_answer": 1,
        "explanation": "% is the modulo operator, giving the remainder of division."
    },
    {
        "id": 47,
        "type": "multiple_choice",
        "question": "What is the output of: System.out.println(2 + \"2\");",
        "options": ["4", "22", "Error", "2"],
        "correct_answer": 1,
        "explanation": "2 (int) + '2' (String) results in String concatenation: '22'."
    },
    {
        "id": 48,
        "type": "multiple_choice",
        "question": "Which keyword is used to make decisions in Java?",
        "options": ["loop", "choose", "if", "run"],
        "correct_answer": 2,
        "explanation": "The 'if' keyword executes a block conditionally based on a boolean expression."
    },
    {
        "id": 49,
        "type": "multiple_choice",
        "question": "What is the output of: System.out.println(10 > 5 && 2 < 1);",
        "options": ["true", "false", "1", "Error"],
        "correct_answer": 1,
        "explanation": "AND (&&) requires both conditions true. 10>5 is true but 2<1 is false, so the result is false."
    },
    {
        "id": 50,
        "type": "multiple_choice",
        "question": "Which data type stores True/False values?",
        "options": ["int", "boolean", "String", "double"],
        "correct_answer": 1,
        "explanation": "boolean can hold only true or false values in Java."
    },
    {
        "id": 51,
        "type": "multiple_choice",
        "question": "What is the output of: System.out.println(\"Hello\".substring(1));",
        "options": ["ello", "Hello", "H", "Error"],
        "correct_answer": 0,
        "explanation": "substring(1) returns characters from index 1 to the end: 'ello'."
    },
    {
        "id": 52,
        "type": "multiple_choice",
        "question": "Which operator is used for assignment?",
        "options": ["==", "=", "!=", "<="],
        "correct_answer": 1,
        "explanation": "= is the assignment operator, storing a value into a variable. == checks equality."
    },
    {
        "id": 53,
        "type": "multiple_choice",
        "question": "What is the output of: System.out.println(3 + 4 + \"Java\");",
        "options": ["Java7", "34Java", "7Java", "Error"],
        "correct_answer": 2,
        "explanation": "Left to right evaluation: 3+4=7, then 7 + 'Java' = '7Java'."
    },
    {
        "id": 54,
        "type": "multiple_choice",
        "question": "Which statement prints output to the console?",
        "options": ["System.in.println()", "print.output()", "System.out.println()", "output.print()"],
        "correct_answer": 2,
        "explanation": "System.out.println() is the standard method for console output in Java."
    },
    {
        "id": 55,
        "type": "multiple_choice",
        "question": "What is the output of: System.out.println(\"JAVA\".toLowerCase());",
        "options": ["JAVA", "java", "Java", "Error"],
        "correct_answer": 1,
        "explanation": "toLowerCase() converts all characters to lowercase: 'JAVA' becomes 'java'."
    },
    {
        "id": 56,
        "type": "multiple_choice",
        "question": "Which data type stores a single character?",
        "options": ["String", "char", "boolean", "double"],
        "correct_answer": 1,
        "explanation": "char stores a single 16-bit Unicode character using single quotes."
    },
    {
        "id": 57,
        "type": "multiple_choice",
        "question": "What is the output of: int x = 8; System.out.println(x > 5 ? \"Yes\" : \"No\");",
        "options": ["true", "false", "Yes", "No"],
        "correct_answer": 2,
        "explanation": "Ternary operator: condition x>5 is true, so 'Yes' is returned and printed."
    },
    {
        "id": 58,
        "type": "multiple_choice",
        "question": "Which statement about 'main' is correct?",
        "options": ["It is optional", "It starts Java execution", "It ends compilation", "It creates variables"],
        "correct_answer": 1,
        "explanation": "public static void main(String[] args) is the entry point for Java applications."
    },
    {
        "id": 59,
        "type": "multiple_choice",
        "question": "What is the output of: System.out.println(Math.sqrt(25));",
        "options": ["25", "6", "5.0", "5"],
        "correct_answer": 2,
        "explanation": "Math.sqrt() returns the square root as double, so 25 → 5.0."
    },
    {
        "id": 60,
        "type": "multiple_choice",
        "question": "Which Java slogan means programs can run on different systems?",
        "options": ["Think Different", "Write Once, Run Anywhere", "Java Everywhere", "Code Once Use Forever"],
        "correct_answer": 1,
        "explanation": "'Write Once, Run Anywhere' (WORA) describes Java's platform independence through the JVM."
    },
    
    
    {
        "id": 61,
        "type": "multiple_choice",
        "question": "What is the primary role of the `javac` command?",
        "options": [
            "Run a Java program",
            "Compile a `.java` file into bytecode",
            "Debug a Java program",
            "Optimize memory usage"
        ],
        "correct_answer": 1,
        "explanation": "The javac command is the Java compiler. It reads source code from .java files and translates it into platform-independent bytecode stored in .class files."
    },
    {
        "id": 62,
        "type": "multiple_choice",
        "question": "What does the `java` command do?",
        "options": [
            "Compiles source code",
            "Starts the JVM to run a `.class` file",
            "Renames files",
            "Checks syntax only"
        ],
        "correct_answer": 1,
        "explanation": "The java command launches the Java Virtual Machine (JVM), which then loads and executes the bytecode contained in the specified .class file."
    },
    {
        "id": 63,
        "type": "multiple_choice",
        "question": "A student names her file `helloworld.java` but writes `public class Helloworld` inside. What happens when she runs `javac helloworld.java`?",
        "options": [
            "Compiles successfully",
            "Compile error due to class name mismatch",
            "Runtime error",
            "Creates wrong `.class` name"
        ],
        "correct_answer": 1,
        "explanation": "Java requires the filename of a public class to exactly match the class name, including case. Since 'helloworld.java' does not match 'Helloworld', the compiler produces an error."
    },
    {
        "id": 64,
        "type": "multiple_choice",
        "question": "Why can a `.class` file run on any OS with a JVM?",
        "options": [
            "It contains machine code for all OSes",
            "It contains platform-independent bytecode",
            "It auto-updates per OS",
            "It is plain text"
        ],
        "correct_answer": 1,
        "explanation": "The .class file contains bytecode, which is a standardized, intermediate representation. The JVM translates this bytecode into native machine code at runtime, making it platform-independent."
    },
    {
        "id": 65,
        "type": "multiple_choice",
        "question": "What does `System.out.println()` do that `System.out.print()` does not?",
        "options": [
            "Prints a space",
            "Moves to a new line after output",
            "Prints only strings",
            "Clears the console"
        ],
        "correct_answer": 1,
        "explanation": "println() outputs its argument (or a blank line if called with no argument) and then terminates the line, moving the cursor to the beginning of the next line. print() outputs its argument but leaves the cursor on the same line."
    },
    {
        "id": 66,
        "type": "multiple_choice",
        "question": "In which situation would `System.out.print()` be preferred?",
        "options": [
            "Printing a single line",
            "Printing multiple items on the same line",
            "Printing an error message",
            "Ending a program"
        ],
        "correct_answer": 1,
        "explanation": "print() is ideal when you want to build output incrementally on the same line, such as when prompting for input on the same line or formatting a sentence from multiple variables."
    },
    {
        "id": 67,
        "type": "multiple_choice",
        "question": "A student runs `java MyProgram.java` after successful compilation. What mistake did they make?",
        "options": [
            "Forgot to compile again",
            "Should run `java MyProgram` (without `.java`)",
            "Should run `javac MyProgram`",
            "No mistake"
        ],
        "correct_answer": 1,
        "explanation": "The java command expects the name of a class (which corresponds to a .class file), not the source filename. The correct command is 'java MyProgram'."
    },
    {
        "id": 68,
        "type": "multiple_choice",
        "question": "Which is a correct Java rule about class names and file names?",
        "options": [
            "File name can be anything",
            "Public class name must match file name",
            "Class names must be lowercase",
            "File extension can be `.txt`"
        ],
        "correct_answer": 1,
        "explanation": "If a class is declared as public, the source code filename must be exactly the class name with a .java extension. This is a strict rule enforced by the compiler."
    },
    {
        "id": 69,
        "type": "multiple_choice",
        "question": "If a public class is named `School`, the file must be:",
        "options": [
            "`school.java`",
            "`School.java`",
            "`school.class`",
            "Any name"
        ],
        "correct_answer": 1,
        "explanation": "The filename must match the public class name exactly, including case: School.java."
    },
    {
        "id": 70,
        "type": "multiple_choice",
        "question": "What happens if a file contains two public classes?",
        "options": [
            "Compiles fine",
            "Compile error",
            "Only first class works",
            "Runs but ignores second"
        ],
        "correct_answer": 1,
        "explanation": "A Java source file can have at most one public class. Having two public classes in the same file results in a compile-time error."
    },
    {
        "id": 71,
        "type": "multiple_choice",
        "question": "What does the `.class` file contain?",
        "options": [
            "Source code",
            "Java bytecode",
            "Machine code",
            "Plain text"
        ],
        "correct_answer": 1,
        "explanation": "The .class file contains Java bytecode, which is an intermediate representation of the program that is executed by the JVM."
    },
    {
        "id": 72,
        "type": "multiple_choice",
        "question": "The line `System.out.println;` (as in Q10) causes:",
        "options": [
            "No error",
            "Compile error — missing parentheses",
            "Runtime error",
            "Prints nothing"
        ],
        "correct_answer": 1,
        "explanation": "println is a method, so it must be called with parentheses, even if no arguments are passed. Without parentheses, the compiler interprets it as a variable reference, leading to an error."
    },
    {
        "id": 73,
        "type": "multiple_choice",
        "question": "In Q11, what is the bug in `Public class Profile`?",
        "options": [
            "Missing semicolon",
            "`Public` should be `public`",
            "Wrong file name",
            "Missing main method"
        ],
        "correct_answer": 1,
        "explanation": "Java keywords are case-sensitive. The class declaration keyword is 'public' (lowercase p), not 'Public'."
    },
    {
        "id": 74,
        "type": "multiple_choice",
        "question": "What does `System.out.println()` print if given nothing inside parentheses?",
        "options": [
            "Nothing",
            "A blank line",
            "An error",
            "A space"
        ],
        "correct_answer": 1,
        "explanation": "Calling println() with no argument prints only a newline character, resulting in a blank line in the output."
    },
    {
        "id": 75,
        "type": "multiple_choice",
        "question": "What is the output of: `System.out.print(\"A\"); System.out.print(\"B\");`",
        "options": [
            "AB",
            "A B",
            "A\\nB",
            "A\\n\\nB"
        ],
        "correct_answer": 0,
        "explanation": "Because print() does not add a newline, the 'A' and 'B' are placed consecutively on the same line: 'AB'."
    },
    {
        "id": 76,
        "type": "multiple_choice",
        "question": "What is the output of: `System.out.println(\"Hello\"); System.out.println(); System.out.println(\"World\");`",
        "options": [
            "Hello\\nWorld",
            "Hello\\n\\nWorld",
            "HelloWorld",
            "Hello World"
        ],
        "correct_answer": 1,
        "explanation": "The first println prints 'Hello' and a newline. The second println prints only a newline. The third prints 'World' and a newline, resulting in a blank line between 'Hello' and 'World'."
    },
    {
        "id": 77,
        "type": "multiple_choice",
        "question": "In `System.out.println(\"\\\\\\\"\")`, what is printed?",
        "options": [
            "\\\"",
            "\\\\\\\"",
            "\\",
            "\""
        ],
        "correct_answer": 0,
        "explanation": "The sequence \\\\ produces a single backslash, and \\\" produces a single double-quote character. Together they output \\\"."
    },
    {
        "id": 78,
        "type": "multiple_choice",
        "question": "What does `System.out.println(\"C:\\\\Temp\")` print?",
        "options": [
            "C:\\Temp",
            "C:\\\\Temp",
            "C:Temp",
            "Error"
        ],
        "correct_answer": 0,
        "explanation": "The escape sequence \\\\ is interpreted as a single backslash character, so the output becomes C:\\Temp."
    },
    {
        "id": 79,
        "type": "multiple_choice",
        "question": "A line starting with `//` inside a Java program is:",
        "options": [
            "Compiled",
            "Ignored as a comment",
            "Printed",
            "An error"
        ],
        "correct_answer": 1,
        "explanation": "// denotes a single-line comment. The compiler ignores all text after // on that line."
    },
    {
        "id": 80,
        "type": "multiple_choice",
        "question": "What is printed by: `System.out.println(\"/* not a comment */\");`",
        "options": [
            "/* not a comment */",
            "not a comment",
            "(blank)",
            "Error"
        ],
        "correct_answer": 0,
        "explanation": "The text is inside a String literal (double quotes), so it is treated as data to be printed, not as a comment. The output includes the /* and */ characters."
    },
    {
        "id": 81,
        "type": "multiple_choice",
        "question": "What happens if `main` is written as `public static void Main(String[] args)`?",
        "options": [
            "Runs normally",
            "Compile error (case-sensitive)",
            "Runtime error",
            "Prints nothing"
        ],
        "correct_answer": 1,
        "explanation": "The JVM looks for 'main' with a lowercase 'm'. 'Main' is a different method name, so the program will compile but the JVM will report a missing main method at runtime."
    },
    {
        "id": 82,
        "type": "multiple_choice",
        "question": "Which is a valid `main` method signature?",
        "options": [
            "`public void main(String[] args)`",
            "`public static void main(String[] args)`",
            "`static public void main()`",
            "`public static main(String[] args)`"
        ],
        "correct_answer": 1,
        "explanation": "The exact required signature for the entry point is 'public static void main(String[] args)'. Variations in keywords, return type, or parameter type are not recognized by the JVM."
    },
    {
        "id": 83,
        "type": "multiple_choice",
        "question": "What does `javac` produce if no errors exist?",
        "options": [
            "`.java` file",
            "`.class` file",
            "`.exe` file",
            "`.jar` file"
        ],
        "correct_answer": 1,
        "explanation": "The Java compiler outputs one or more .class files (bytecode) corresponding to each class defined in the source file."
    },
    {
        "id": 84,
        "type": "multiple_choice",
        "question": "A missing semicolon at line end causes:",
        "options": [
            "Runtime error",
            "Compile error",
            "Logical error",
            "Warning only"
        ],
        "correct_answer": 1,
        "explanation": "In Java, statements must end with a semicolon. Its absence is a syntax error caught at compile time."
    },
    {
        "id": 85,
        "type": "multiple_choice",
        "question": "In Q14, what is printed after `System.out.println(\" \");`?",
        "options": [
            "Nothing",
            "A space",
            "Blank line",
            "Null"
        ],
        "correct_answer": 0,
        "explanation": "The string contains a single space character, so a space followed by a newline is printed."
    },
    {
        "id": 86,
        "type": "multiple_choice",
        "question": "What is printed by: `System.out.print(\"1\\n2\");`",
        "options": [
            "1\\n2",
            "1 2",
            "1\n   2",
            "\"1\\n2\""
        ],
        "correct_answer": 2,
        "explanation": "The escape sequence \\n is interpreted as a newline character, so '1' is printed, then a newline, then '2'."
    },
    {
        "id": 87,
        "type": "multiple_choice",
        "question": "Which prints a blank line?",
        "options": [
            "`System.out.print(\"\");`",
            "`System.out.println();`",
            "`System.out.println(\" \");`",
            "`System.out.print(\"\\n\");`"
        ],
        "correct_answer": 1,
        "explanation": "println() with no argument prints only the line separator (newline), creating a blank line. print(\"\") prints nothing, and print(\"\\n\") also prints a blank line but is less conventional."
    },
    {
        "id": 88,
        "type": "multiple_choice",
        "question": "In Q19, the last `println()` must produce a blank line. Which is correct?",
        "options": [
            "`System.out.println();`",
            "`System.out.print(\"\");`",
            "`System.out.println(\"\\n\");`",
            "`System.out.print(\"\\n\");`"
        ],
        "correct_answer": 0,
        "explanation": "The typical and correct way to produce a blank line is an empty println() call, which prints only the newline character."
    },
    {
        "id": 89,
        "type": "multiple_choice",
        "question": "What is wrong with: `System.out.println(\"She said \\\"Hello\\\"\");`",
        "options": [
            "Missing closing quote",
            "Nothing — it’s correct",
            "Should use single quotes",
            "Backslash not allowed"
        ],
        "correct_answer": 1,
        "explanation": "This line is correct. The backslashes escape the inner double quotes, allowing them to be printed as literal characters."
    },
    {
        "id": 90,
        "type": "multiple_choice",
        "question": "Which escape sequence represents a newline?",
        "options": [
            "\\t",
            "\\n",
            "\\r",
            "\\b"
        ],
        "correct_answer": 1,
        "explanation": "\\n is the newline (line feed) character. \\t is tab, \\r is carriage return, and \\b is backspace."
    },
    {
        "id": 91,
        "type": "multiple_choice",
        "question": "Which escape sequence represents a tab?",
        "options": [
            "\\t",
            "\\n",
            "\\r",
            "\\\\"
        ],
        "correct_answer": 0,
        "explanation": "\\t is the escape sequence for a horizontal tab character."
    },
    {
        "id": 92,
        "type": "multiple_choice",
        "question": "What does `System.out.println(\"\\\\\");` print?",
        "options": [
            "\\",
            "\\\\",
            "/",
            "Error"
        ],
        "correct_answer": 0,
        "explanation": "The escape sequence \\\\ is interpreted as a single backslash character. Therefore, a single backslash is printed."
    },
    {
        "id": 93,
        "type": "multiple_choice",
        "question": "A file `hello.java` contains `public class HelloWorld`. Compilation:",
        "options": [
            "Succeeds",
            "Fails — wrong file name",
            "Fails — wrong class name inside",
            "Succeeds but won’t run"
        ],
        "correct_answer": 1,
        "explanation": "For a public class, the filename must match the class name. Since 'hello.java' does not equal 'HelloWorld.java', compilation fails."
    },
    {
        "id": 94,
        "type": "multiple_choice",
        "question": "Which command runs a compiled Java program `Test`?",
        "options": [
            "`java Test.java`",
            "`java Test`",
            "`javac Test`",
            "`run Test`"
        ],
        "correct_answer": 1,
        "explanation": "After compilation, the program is run with 'java Test', where Test is the name of the class containing the main method."
    },
    {
        "id": 95,
        "type": "multiple_choice",
        "question": "Which command compiles `Test.java`?",
        "options": [
            "`java Test.java`",
            "`javac Test`",
            "`javac Test.java`",
            "`compile Test.java`"
        ],
        "correct_answer": 2,
        "explanation": "The Java compiler command is 'javac', followed by the source filename (including .java extension)."
    },
    {
        "id": 96,
        "type": "multiple_choice",
        "question": "What is printed? `System.out.print(\"A\"); System.out.println(\"B\"); System.out.print(\"C\");`",
        "options": [
            "ABC",
            "AB\\nC",
            "A\\nB\\nC",
            "A B C"
        ],
        "correct_answer": 1,
        "explanation": "First, print(\"A\") outputs 'A' without newline. Then println(\"B\") outputs 'B' followed by a newline. Finally, print(\"C\") outputs 'C' on the next line."
    },
    {
        "id": 97,
        "type": "multiple_choice",
        "question": "What is printed? `System.out.println(\"====\"); System.out.println(\"\"); System.out.println(\"====\");`",
        "options": [
            "====\\n\\n====",
            "====\\n \\n====",
            "====\\nnull\\n====",
            "====\\n\\n\\n===="
        ],
        "correct_answer": 0,
        "explanation": "The first println prints '====' + newline. The second prints an empty string (\"\") followed by a newline, resulting in a blank line. The third prints '====' + newline."
    },
    {
        "id": 98,
        "type": "multiple_choice",
        "question": "Which is a valid class declaration?",
        "options": [
            "`public class 1stClass`",
            "`public class FirstClass`",
            "`public class first-class`",
            "`Public class FirstClass`"
        ],
        "correct_answer": 1,
        "explanation": "A class name must start with a letter (or underscore or dollar sign), cannot contain hyphens, and keywords must be lowercase. 'public class FirstClass' follows all rules."
    },
    {
        "id": 99,
        "type": "multiple_choice",
        "question": "Multiple `println` statements without arguments:",
        "options": [
            "Print blanks",
            "Cause errors",
            "Print spaces",
            "Are ignored"
        ],
        "correct_answer": 0,
        "explanation": "Each println() call without an argument prints a blank line (just the line separator)."
    },
    {
        "id": 100,
        "type": "multiple_choice",
        "question": "In Q17, blanks must be filled to match output. What does `System.out.print` with no argument do?",
        "options": [
            "Prints nothing",
            "Causes error",
            "Prints a space",
            "Prints null"
        ],
        "correct_answer": 1,
        "explanation": "Unlike println(), print() must be called with an argument. print() with no argument is a compile-time error."
    },
    {
        "id": 101,
        "type": "multiple_choice",
        "question": "In Q18, if output has multiple spaces, which method is likely used?",
        "options": [
            "`println()`",
            "`print(\" \")`",
            "`print()`",
            "`printf()`"
        ],
        "correct_answer": 1,
        "explanation": "To print spaces without moving to a new line, you would use print(\" \") repeatedly. println() would add unwanted newlines."
    },
    {
        "id": 102,
        "type": "multiple_choice",
        "question": "What is wrong with: `System.out.println(\\\"Hello\\\");`",
        "options": [
            "Missing parentheses",
            "Missing quotes inside",
            "Backslash before quote wrong place",
            "Correct"
        ],
        "correct_answer": 0,
        "explanation": "The parentheses for the method call are missing entirely. The correct syntax is println(\"Hello\");"
    },
    {
        "id": 103,
        "type": "multiple_choice",
        "question": "A Java source file can have at most:",
        "options": [
            "One public class",
            "Unlimited public classes",
            "No public classes",
            "One class total"
        ],
        "correct_answer": 0,
        "explanation": "A .java file can have multiple classes, but at most one of them can be declared public."
    },
    {
        "id": 104,
        "type": "multiple_choice",
        "question": "In Q9 (Banner program), `System.out.println;` (line 6) should be:",
        "options": [
            "`System.out.println();`",
            "`System.out.print();`",
            "`System.out.println(\"\");`",
            "Remove line"
        ],
        "correct_answer": 0,
        "explanation": "The line is missing parentheses. The correct call to print a blank line is System.out.println();"
    },
    {
        "id": 105,
        "type": "multiple_choice",
        "question": "What is output? `System.out.print(\"Hello \"); System.out.println(\"World\");`",
        "options": [
            "HelloWorld",
            "Hello World",
            "Hello\\nWorld",
            "Hello World\\n"
        ],
        "correct_answer": 1,
        "explanation": "print(\"Hello \") outputs 'Hello ' (with trailing space). println(\"World\") outputs 'World' and then a newline. The result is 'Hello World' followed by a newline."
    },
    {
        "id": 106,
        "type": "multiple_choice",
        "question": "Which prints `\"Hi\"` with quotes?",
        "options": [
            "`System.out.println(\"Hi\");`",
            "`System.out.println(\"\\\"Hi\\\"\");`",
            "`System.out.println('\"Hi\"');`",
            "`System.out.println(\"\"Hi\"\");`"
        ],
        "correct_answer": 1,
        "explanation": "To include double quote characters inside a String literal, you must escape them using \\\". The correct string is \\\"Hi\\\"."
    },
    {
        "id": 107,
        "type": "multiple_choice",
        "question": "In Q13, the output after `System.out.println();` is:",
        "options": [
            "Blank line",
            "Nothing",
            "Space",
            "Null"
        ],
        "correct_answer": 0,
        "explanation": "An empty println() produces a blank line (line separator only)."
    },
    {
        "id": 108,
        "type": "multiple_choice",
        "question": "What does the JVM do?",
        "options": [
            "Compiles code",
            "Executes bytecode",
            "Edits source",
            "Manages filenames"
        ],
        "correct_answer": 1,
        "explanation": "The Java Virtual Machine (JVM) is responsible for loading and executing the bytecode contained in .class files."
    },
    {
        "id": 109,
        "type": "multiple_choice",
        "question": "Which is a legal Java identifier for a class?",
        "options": [
            "2Cool",
            "Cool$2",
            "Cool-2",
            "class"
        ],
        "correct_answer": 1,
        "explanation": "Identifiers can start with a letter, underscore, or dollar sign. They can contain digits after the first character. 'Cool$2' is legal (though $ is unconventional). 'class' is a keyword and cannot be used."
    },
    {
        "id": 110,
        "type": "multiple_choice",
        "question": "If output must match exactly, `System.out.print` vs `println` matters because:",
        "options": [
            "`print` adds no newline",
            "`println` is faster",
            "`print` only works with strings",
            "`println` clears screen"
        ],
        "correct_answer": 0,
        "explanation": "The critical difference is that print() leaves the cursor at the end of the printed text, while println() adds a line separator. This affects the exact layout of the output."
    }


    ]
}
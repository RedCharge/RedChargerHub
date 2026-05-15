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
    }

    ]
}
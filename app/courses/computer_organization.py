computer_organization_quiz = {
    "course_code": "BCP 203",
    "course_name": "Computer Organization Architecture",
    "total_questions": 50,
    "questions": [
        # Multiple Choice Questions (1-25)
        
    
    
    {
        "id": 1,
        "type": "multiple_choice",
        "question": "What is a stored-program computer?",
        "options": [
            "A computer where programs are permanently wired into hardware",
            "A computer that stores both instructions and data in the same memory",
            "A computer that runs only one program at a time",
            "A computer that stores programs only in external storage"
        ],
        "correct_answer": 1,
        "explanation": "A stored-program computer is defined by its ability to store both the program instructions and the data they operate on in the same memory space."
    },
    {
        "id": 2,
        "type": "multiple_choice",
        "question": "Which statement best describes the Von Neumann architecture?",
        "options": [
            "Separate memory for data and instructions",
            "Uses two processors simultaneously",
            "Data and instructions share the same memory and bus",
            "Programs cannot be modified once stored"
        ],
        "correct_answer": 2,
        "explanation": "The Von Neumann architecture is characterized by a single, shared memory space and a single bus for transferring both instructions and data."
    },
    {
        "id": 3,
        "type": "multiple_choice",
        "question": "What is the main feature of Harvard architecture?",
        "options": [
            "Instructions and data share the same memory",
            "Instructions and data use separate memory systems",
            "Programs run only in cache memory",
            "Programs are hardwired"
        ],
        "correct_answer": 1,
        "explanation": "The Harvard architecture's defining feature is the use of physically separate storage and signal pathways for instructions and data."
    },
    {
        "id": 4,
        "type": "multiple_choice",
        "question": "Moore’s Law states that:",
        "options": [
            "Processor speed doubles every year",
            "The number of transistors on a chip roughly doubles every two years",
            "Memory size doubles every month",
            "Computers become slower as they get smaller"
        ],
        "correct_answer": 1,
        "explanation": "Moore's Law is the observation that the number of transistors in a dense integrated circuit doubles about every two years."
    },
    {
        "id": 5,
        "type": "multiple_choice",
        "question": "According to Amdahl’s Law:",
        "options": [
            "Overall system performance depends on the slowest component",
            "System speed improvement is limited by the portion that cannot be improved",
            "Memory capacity limits processor speed",
            "Performance depends only on processor frequency"
        ],
        "correct_answer": 1,
        "explanation": "Amdahl's Law is used to find the maximum expected improvement to an overall system when only part of the system is improved. It highlights the diminishing returns of optimizing a portion of a workload."
    },
    {
        "id": 6,
        "type": "multiple_choice",
        "question": "Little’s Law in computing systems relates:",
        "options": [
            "Processing speed and power consumption",
            "System throughput, number of tasks, and response time",
            "Cache size and memory size",
            "CPU frequency and instruction set"
        ],
        "correct_answer": 1,
        "explanation": "Little's Law describes the relationship between the average number of items in a system (L), the average arrival rate of items (λ), and the average time an item spends in the system (W), expressed as L = λW."
    },
    {
        "id": 7,
        "type": "multiple_choice",
        "question": "What is an embedded system?",
        "options": [
            "A computer designed for general-purpose computing",
            "A computer system built to perform a specific dedicated function",
            "A computer with multiple processors",
            "A computer used only for networking"
        ],
        "correct_answer": 1,
        "explanation": "An embedded system is a specialized computer system designed for a dedicated function, often with real-time computing constraints, and is embedded as part of a complete device."
    },
    {
        "id": 8,
        "type": "multiple_choice",
        "question": "Which processor type is most commonly used in embedded systems?",
        "options": [
            "ARM processors",
            "Quantum processors",
            "Mainframe processors",
            "GPU processors"
        ],
        "correct_answer": 0,
        "explanation": "ARM processors are the most widely used architecture in embedded systems due to their low power consumption and high performance for mobile and dedicated applications."
    },
    {
        "id": 9,
        "type": "multiple_choice",
        "question": "A register in a processor is primarily made up of:",
        "options": [
            "Magnetic disks",
            "Flip-flops",
            "Capacitors",
            "Optical cells"
        ],
        "correct_answer": 1,
        "explanation": "Registers are small, fast storage locations within the CPU, typically implemented using flip-flops, which are circuits that can store a single bit of data."
    },
    {
        "id": 10,
        "type": "multiple_choice",
        "question": "Why are registers used in a CPU?",
        "options": [
            "To permanently store programs",
            "To provide high-speed temporary storage for instructions and data",
            "To replace RAM",
            "To store operating systems"
        ],
        "correct_answer": 1,
        "explanation": "Registers are the top of the memory hierarchy, providing the fastest possible access to data and instructions that the CPU is currently processing."
    },
    {
        "id": 11,
        "type": "multiple_choice",
        "question": "Which register holds the address of the next instruction?",
        "options": [
            "Instruction Register",
            "Memory Address Register",
            "Program Counter",
            "Accumulator"
        ],
        "correct_answer": 2,
        "explanation": "The Program Counter (PC), also called the instruction pointer, contains the memory address of the next instruction to be fetched and executed."
    },
    {
        "id": 12,
        "type": "multiple_choice",
        "question": "Which register stores the current instruction being executed?",
        "options": [
            "Instruction Register",
            "Memory Buffer Register",
            "Program Counter",
            "Status Register"
        ],
        "correct_answer": 0,
        "explanation": "The Instruction Register (IR) holds the current instruction that has been fetched from memory and is being decoded and executed by the control unit."
    },
    {
        "id": 13,
        "type": "multiple_choice",
        "question": "The accumulator register is mainly used for:",
        "options": [
            "Storing addresses",
            "Storing intermediate arithmetic and logical results",
            "Storing programs permanently",
            "Managing interrupts"
        ],
        "correct_answer": 1,
        "explanation": "The accumulator is a register in which intermediate arithmetic and logic results are stored. It is a default destination for many operation results."
    },
    {
        "id": 14,
        "type": "multiple_choice",
        "question": "Which register holds the address of a memory location being accessed?",
        "options": [
            "MAR",
            "MBR",
            "IR",
            "PC"
        ],
        "correct_answer": 0,
        "explanation": "The Memory Address Register (MAR) holds the address of the memory location that the CPU is about to read from or write to."
    },
    {
        "id": 15,
        "type": "multiple_choice",
        "question": "Which register stores data read from or written to memory?",
        "options": [
            "MAR",
            "MBR",
            "IR",
            "PC"
        ],
        "correct_answer": 1,
        "explanation": "The Memory Buffer Register (MBR), also known as the Memory Data Register (MDR), acts as a buffer, holding the data that is being transferred to or from the memory."
    },
    {
        "id": 16,
        "type": "multiple_choice",
        "question": "Interconnection structures allow communication between:",
        "options": [
            "CPU, memory, and input/output devices",
            "Only processors",
            "Only storage devices",
            "Only input devices"
        ],
        "correct_answer": 0,
        "explanation": "The interconnection structure, such as a system bus, provides the communication pathways that link the CPU, main memory, and all I/O modules."
    },
    {
        "id": 17,
        "type": "multiple_choice",
        "question": "Which transfer occurs when the CPU sends data to memory?",
        "options": [
            "Memory Read",
            "Memory Write",
            "I/O Read",
            "I/O Write"
        ],
        "correct_answer": 1,
        "explanation": "A memory write operation is performed when the CPU sends data to be stored in a specific memory location."
    },
    {
        "id": 18,
        "type": "multiple_choice",
        "question": "Which transfer occurs when data moves from memory to the CPU?",
        "options": [
            "Memory Read",
            "Memory Write",
            "I/O Write",
            "Interrupt Transfer"
        ],
        "correct_answer": 0,
        "explanation": "A memory read operation is performed when the CPU fetches instructions or data from a specific memory location."
    },
    {
        "id": 19,
        "type": "multiple_choice",
        "question": "A program is said to be hardwired when:",
        "options": [
            "It is stored in RAM",
            "It is implemented directly in hardware circuits",
            "It is stored in external memory",
            "It runs through software"
        ],
        "correct_answer": 1,
        "explanation": "A hardwired program is one where the control logic is implemented as a permanent part of the computer's circuitry, as opposed to being stored in memory as software instructions."
    },
    {
        "id": 20,
        "type": "multiple_choice",
        "question": "The first step in executing a program is:",
        "options": [
            "Decode instruction",
            "Fetch instruction from memory",
            "Execute instruction",
            "Store result"
        ],
        "correct_answer": 1,
        "explanation": "The instruction cycle begins with the fetch phase, where the CPU retrieves the next instruction from memory using the address in the Program Counter."
    },
    {
        "id": 21,
        "type": "multiple_choice",
        "question": "The instruction cycle typically follows which sequence?",
        "options": [
            "Execute → Decode → Fetch",
            "Fetch → Decode → Execute",
            "Decode → Fetch → Execute",
            "Execute → Fetch → Decode"
        ],
        "correct_answer": 1,
        "explanation": "The classic instruction cycle is a loop of three main stages: Fetch the instruction, Decode what it does, and then Execute it."
    },
    {
        "id": 22,
        "type": "multiple_choice",
        "question": "The system bus is best described as:",
        "options": [
            "A communication pathway connecting computer components",
            "A storage device",
            "A processor component",
            "A network cable"
        ],
        "correct_answer": 0,
        "explanation": "The system bus is a single computer bus that connects the major components of a computer system, combining the functions of a data bus, address bus, and control bus."
    },
    {
        "id": 23,
        "type": "multiple_choice",
        "question": "Which bus carries actual data between components?",
        "options": [
            "Address Bus",
            "Control Bus",
            "Data Bus",
            "System Clock"
        ],
        "correct_answer": 2,
        "explanation": "The data bus is a bidirectional pathway that carries the actual data being transferred between the CPU, memory, and I/O devices."
    },
    {
        "id": 24,
        "type": "multiple_choice",
        "question": "Which bus carries memory addresses from the CPU?",
        "options": [
            "Data Bus",
            "Address Bus",
            "Control Bus",
            "Expansion Bus"
        ],
        "correct_answer": 1,
        "explanation": "The address bus is a unidirectional bus that carries memory addresses from the CPU to other components like memory, specifying where data should be read from or written to."
    },
    {
        "id": 25,
        "type": "multiple_choice",
        "question": "Which bus carries control signals like read/write commands?",
        "options": [
            "Data Bus",
            "Address Bus",
            "Control Bus",
            "Processor Bus"
        ],
        "correct_answer": 2,
        "explanation": "The control bus carries command, timing, and status signals (like read, write, interrupt requests) to coordinate and manage the activities of all system components."
    },
    {
        "id": 26,
        "type": "multiple_choice",
        "question": "Which of the following is an example of a memory module?",
        "options": [
            "RAM",
            "ROM",
            "Cache",
            "All of the above"
        ],
        "correct_answer": 3,
        "explanation": "RAM (Random Access Memory), ROM (Read-Only Memory), and Cache memory are all distinct types of memory modules or technologies within a computer's memory hierarchy."
    },
    {
        "id": 27,
        "type": "multiple_choice",
        "question": "Which of the following is NOT a memory module?",
        "options": [
            "RAM",
            "ROM",
            "Hard Disk",
            "Monitor"
        ],
        "correct_answer": 3,
        "explanation": "A monitor is an output device, not a memory module. RAM, ROM, and Hard Disks (as storage) are all part of the memory/storage system."
    },
    {
        "id": 28,
        "type": "multiple_choice",
        "question": "Memory is considered internal when it is:",
        "options": [
            "Located inside the CPU or motherboard and directly accessible",
            "Stored outside the computer",
            "Stored in cloud servers",
            "Connected via network"
        ],
        "correct_answer": 0,
        "explanation": "Internal memory, such as RAM and cache, is located on the motherboard and is directly accessible by the CPU via high-speed buses."
    },
    {
        "id": 29,
        "type": "multiple_choice",
        "question": "Memory is considered external when it is:",
        "options": [
            "Built into the CPU",
            "Used for temporary storage only",
            "Located outside the main system memory like disks",
            "Used only by the operating system"
        ],
        "correct_answer": 2,
        "explanation": "External memory, or secondary storage, refers to storage devices that are not directly accessible by the CPU and must be accessed via I/O modules, such as hard drives and SSDs."
    },
    {
        "id": 30,
        "type": "multiple_choice",
        "question": "Cache memory is:",
        "options": [
            "Slow secondary storage",
            "A small high-speed memory between CPU and RAM",
            "External storage",
            "Permanent memory"
        ],
        "correct_answer": 1,
        "explanation": "Cache memory is a small, fast memory component located between the CPU and main memory (RAM) to store frequently accessed data and instructions, reducing average access time."
    },
    {
        "id": 31,
        "type": "multiple_choice",
        "question": "Disk cache refers to:",
        "options": [
            "A reserved portion of RAM used to store frequently accessed disk data",
            "Data stored permanently on disk",
            "CPU registers",
            "A backup storage system"
        ],
        "correct_answer": 0,
        "explanation": "Disk cache is a technique where a portion of main memory (RAM) is used to temporarily store data that has been recently read from or written to a disk, speeding up future access to that data."
    },
    {
        "id": 32,
        "type": "multiple_choice",
        "question": "Virtual memory is:",
        "options": [
            "Physical memory installed on the motherboard",
            "A technique that uses disk space to simulate additional RAM",
            "A type of cache memory",
            "Processor memory"
        ],
        "correct_answer": 1,
        "explanation": "Virtual memory is a memory management technique that uses a portion of the hard drive or SSD to act as an extension of RAM, allowing the system to run larger applications or multiple applications simultaneously than physical memory alone would allow."
    },
    {
        "id": 33,
        "type": "multiple_choice",
        "question": "What does the “diminishing returns” concept in Amdahl’s Law imply?",
        "options": [
            "Increasing processors always increases performance proportionally",
            "Speed improvement decreases as more parts of the system are optimized",
            "Performance always doubles with optimization",
            "System speed depends only on memory"
        ],
        "correct_answer": 1,
        "explanation": "Diminishing returns in the context of Amdahl's Law means that as you continue to optimize a portion of a system, the overall performance gain from each additional unit of optimization becomes smaller and smaller."
    },
    {
        "id": 34,
        "type": "multiple_choice",
        "question": "According to Amdahl’s Law, the main focus of optimization should be on:",
        "options": [
            "The part of the system already very fast",
            "The portion of the system executed most frequently",
            "Random system components",
            "External storage devices"
        ],
        "correct_answer": 1,
        "explanation": "Amdahl's Law dictates that the greatest overall performance improvement comes from optimizing the part of the system that accounts for the largest proportion of the execution time—the most frequent bottleneck."
    },
    {
        "id": 35,
        "type": "multiple_choice",
        "question": "Amdahl’s Law shows that improving only a small part of a system will:",
        "options": [
            "Produce massive performance gains",
            "Have little effect on overall system performance",
            "Double system speed",
            "Eliminate bottlenecks"
        ],
        "correct_answer": 1,
        "explanation": "If the part of the system being improved is only a small fraction of the total workload, the overall performance improvement will be minimal, as dictated by the law."
    },
    {
        "id": 36,
        "type": "multiple_choice",
        "question": "The primary implication of Amdahl’s Law for system designers is:",
        "options": [
            "Optimize every part equally",
            "Focus optimization on the largest performance bottleneck",
            "Ignore slow components",
            "Increase memory only"
        ],
        "correct_answer": 1,
        "explanation": "Amdahl's Law guides designers to identify and focus their efforts on the most significant performance bottlenecks to achieve the best overall speedup for their investment."
    },
    {
        "id": 37,
        "type": "multiple_choice",
        "question": "Which term best describes the relationship between workload and performance measurement?",
        "options": [
            "Matrix relationship",
            "Random relationship",
            "Non-measurable relationship",
            "Hardware-only relationship"
        ],
        "correct_answer": 0,
        "explanation": "The relationship between workload and performance is complex and can be thought of as a matrix or multidimensional relationship, where different performance metrics (throughput, response time) are affected differently by various workload characteristics."
    },
    {
        "id": 38,
        "type": "multiple_choice",
        "question": "In performance evaluation, metrics are used to:",
        "options": [
            "Decorate system documentation",
            "Measure and compare system performance",
            "Store programs in memory",
            "Control processors"
        ],
        "correct_answer": 1,
        "explanation": "Performance metrics provide quantifiable measures that allow engineers and users to evaluate, compare, and predict the performance of different systems or configurations."
    },
    {
        "id": 39,
        "type": "multiple_choice",
        "question": "Little’s Law relates which three quantities?",
        "options": [
            "CPU speed, RAM size, and disk capacity",
            "Throughput, response time, and number of tasks in the system",
            "Processor frequency, voltage, and temperature",
            "Data bus, address bus, and control bus"
        ],
        "correct_answer": 1,
        "explanation": "Little's Law establishes a fundamental relationship between the average number of items in a system (tasks), the average arrival rate of items (throughput), and the average time an item spends in the system (response time)."
    },
    {
        "id": 40,
        "type": "multiple_choice",
        "question": "Little’s Law can be expressed as:",
        "options": [
            "Performance = Time × Speed",
            "L = λ × W",
            "Speed = Instructions × Time",
            "Memory = Data × Address"
        ],
        "correct_answer": 1,
        "explanation": "The standard mathematical expression of Little's Law is L = λW, where L is the average number of items, λ is the average arrival rate, and W is the average time an item spends in the system."
    },
    {
        "id": 41,
        "type": "multiple_choice",
        "question": "In Little’s Law, **L** represents:",
        "options": [
            "System latency",
            "Average number of items in the system",
            "Processor load",
            "Program size"
        ],
        "correct_answer": 1,
        "explanation": "In the formula L = λW, 'L' stands for the average number of items or tasks currently present in the queuing system."
    },
    {
        "id": 42,
        "type": "multiple_choice",
        "question": "In Little’s Law, **λ (lambda)** represents:",
        "options": [
            "System clock speed",
            "Arrival rate or throughput",
            "Memory capacity",
            "Instruction length"
        ],
        "correct_answer": 1,
        "explanation": "In the formula L = λW, 'λ' (lambda) represents the average arrival rate of new items into the system, which, under steady-state conditions, is equal to the throughput."
    },
    {
        "id": 43,
        "type": "multiple_choice",
        "question": "In Little’s Law, **W** represents:",
        "options": [
            "Waiting time in the system",
            "Memory width",
            "CPU frequency",
            "Instruction size"
        ],
        "correct_answer": 0,
        "explanation": "In the formula L = λW, 'W' stands for the average time an item spends waiting in the system, also known as the average response time or sojourn time."
    },
    {
        "id": 44,
        "type": "multiple_choice",
        "question": "One major use of Little’s Law in computer systems is to:",
        "options": [
            "Design processor circuits",
            "Predict system performance under workload",
            "Build memory chips",
            "Replace operating systems"
        ],
        "correct_answer": 1,
        "explanation": "Little's Law is a powerful tool for performance modeling and prediction, allowing engineers to estimate metrics like response time based on observed throughput and queue lengths, and vice-versa."
    },
    {
        "id": 45,
        "type": "multiple_choice",
        "question": "Performance prediction in computer systems helps engineers to:",
        "options": [
            "Guess system speed randomly",
            "Estimate system behavior before implementation",
            "Eliminate hardware",
            "Remove software"
        ],
        "correct_answer": 1,
        "explanation": "Performance prediction uses models and laws like Amdahl's and Little's to anticipate how a system will behave under various conditions before it is built or deployed, aiding in design and capacity planning."
    },
    {
        "id": 46,
        "type": "multiple_choice",
        "question": "System metrics commonly used to measure performance include:",
        "options": [
            "Throughput and response time",
            "Keyboard type",
            "Monitor resolution",
            "Printer speed"
        ],
        "correct_answer": 0,
        "explanation": "Throughput (work done per unit time) and response time (time to complete a task) are two of the most fundamental and common metrics for evaluating computer system performance."
    },
    {
        "id": 47,
        "type": "multiple_choice",
        "question": "Which of the following best defines throughput?",
        "options": [
            "Number of tasks completed per unit time",
            "Time taken for a single instruction",
            "Size of memory",
            "Processor voltage"
        ],
        "correct_answer": 0,
        "explanation": "Throughput is a measure of the rate at which a system can complete work, such as the number of jobs, transactions, or requests processed per second."
    },
    {
        "id": 48,
        "type": "multiple_choice",
        "question": "Response time refers to:",
        "options": [
            "Time taken to complete a task from start to finish",
            "CPU temperature",
            "Memory size",
            "Number of registers"
        ],
        "correct_answer": 0,
        "explanation": "Response time, or latency, is the total elapsed time between submitting a request to a system and receiving the complete response."
    },
    
    {
        "id": 49,
        "type": "multiple_choice",
        "question": "Semiconductor memory is primarily built using:",
        "options": [
            "Magnetic materials",
            "Optical storage",
            "Semiconductor integrated circuits",
            "Mechanical components"
        ],
        "correct_answer": 2,
        "explanation": "Semiconductor memory uses integrated circuits based on semiconductor technology (typically silicon) to store data electronically."
    },
    {
        "id": 50,
        "type": "multiple_choice",
        "question": "One key property of semiconductor memory is:",
        "options": [
            "Very slow access time",
            "Electronic data storage using transistors",
            "Mechanical read/write heads",
            "Magnetic data storage"
        ],
        "correct_answer": 1,
        "explanation": "Semiconductor memory stores data using electronic circuits such as transistors and capacitors, without any moving parts."
    },
    {
        "id": 51,
        "type": "multiple_choice",
        "question": "Semiconductor memory is commonly used for:",
        "options": [
            "Main memory and cache",
            "Optical drives",
            "Magnetic disks",
            "Printers"
        ],
        "correct_answer": 0,
        "explanation": "Semiconductor memory like RAM and cache are essential components of a computer's main memory hierarchy."
    },
    {
        "id": 52,
        "type": "multiple_choice",
        "question": "Another important feature of semiconductor memory is:",
        "options": [
            "High reliability and fast access speed",
            "Very large mechanical parts",
            "Moving storage components",
            "Permanent magnetic coating"
        ],
        "correct_answer": 0,
        "explanation": "Semiconductor memory offers high reliability due to no moving parts and provides very fast access speeds compared to mechanical storage."
    },
    {
        "id": 53,
        "type": "multiple_choice",
        "question": "SRAM stands for:",
        "options": [
            "Static Random Access Memory",
            "Sequential Random Access Memory",
            "Static Read Access Memory",
            "Serial Random Access Memory"
        ],
        "correct_answer": 0,
        "explanation": "SRAM (Static Random Access Memory) is a type of semiconductor memory that uses flip-flops to store each bit and retains data as long as power is supplied."
    },
    {
        "id": 54,
        "type": "multiple_choice",
        "question": "DRAM stands for:",
        "options": [
            "Dynamic Random Access Memory",
            "Digital Random Access Memory",
            "Dynamic Read Access Memory",
            "Direct Random Access Memory"
        ],
        "correct_answer": 0,
        "explanation": "DRAM (Dynamic Random Access Memory) stores each bit in a separate capacitor within an integrated circuit, which requires periodic refreshing."
    },
    {
        "id": 55,
        "type": "multiple_choice",
        "question": "SRAM is typically used in:",
        "options": [
            "Cache memory",
            "Hard disks",
            "Optical storage",
            "Secondary storage"
        ],
        "correct_answer": 0,
        "explanation": "SRAM is faster and more expensive, making it ideal for CPU cache memory where speed is critical."
    },
    {
        "id": 56,
        "type": "multiple_choice",
        "question": "DRAM is commonly used for:",
        "options": [
            "CPU registers",
            "Main system memory",
            "Flash storage",
            "Magnetic storage"
        ],
        "correct_answer": 1,
        "explanation": "DRAM is denser and cheaper than SRAM, making it suitable for main system memory (RAM) where large capacity is needed."
    },
    {
        "id": 57,
        "type": "multiple_choice",
        "question": "In terms of speed:",
        "options": [
            "DRAM is faster than SRAM",
            "SRAM is faster than DRAM",
            "Both have equal speed",
            "DRAM and SRAM are extremely slow"
        ],
        "correct_answer": 1,
        "explanation": "SRAM is significantly faster than DRAM because it does not require refresh cycles and has lower access latency."
    },
    {
        "id": 58,
        "type": "multiple_choice",
        "question": "In terms of cost:",
        "options": [
            "SRAM is cheaper",
            "DRAM is more expensive",
            "SRAM is more expensive",
            "Both cost the same"
        ],
        "correct_answer": 2,
        "explanation": "SRAM is more expensive to manufacture because it requires more transistors per bit of storage (typically 6 transistors per bit) compared to DRAM (1 transistor and 1 capacitor per bit)."
    },
    {
        "id": 59,
        "type": "multiple_choice",
        "question": "In terms of size/density:",
        "options": [
            "DRAM has higher density",
            "SRAM has higher density",
            "Both have equal density",
            "SRAM uses less space per bit"
        ],
        "correct_answer": 0,
        "explanation": "DRAM has higher storage density because its simpler cell structure (one transistor and one capacitor) takes less space than SRAM's flip-flop design."
    },
    {
        "id": 60,
        "type": "multiple_choice",
        "question": "DRAM requires periodic:",
        "options": [
            "Rebooting",
            "Refreshing",
            "Formatting",
            "Encryption"
        ],
        "correct_answer": 1,
        "explanation": "DRAM cells leak charge over time and must be refreshed (read and rewritten) thousands of times per second to maintain data integrity."
    },
    {
        "id": 61,
        "type": "multiple_choice",
        "question": "SRAM does NOT require:",
        "options": [
            "Refresh cycles",
            "Transistors",
            "Power supply",
            "Addressing"
        ],
        "correct_answer": 0,
        "explanation": "SRAM retains data without refresh cycles as long as power is supplied, unlike DRAM which requires constant refreshing."
    },
    {
        "id": 62,
        "type": "multiple_choice",
        "question": "Which memory uses capacitors to store data?",
        "options": [
            "SRAM",
            "DRAM",
            "ROM",
            "Cache"
        ],
        "correct_answer": 1,
        "explanation": "DRAM stores each bit using a tiny capacitor and a transistor. The presence or absence of charge in the capacitor represents the bit value."
    },
    {
        "id": 63,
        "type": "multiple_choice",
        "question": "DDR stands for:",
        "options": [
            "Double Data Rate",
            "Digital Data Rate",
            "Dynamic Data Register",
            "Dual Disk Register"
        ],
        "correct_answer": 0,
        "explanation": "DDR (Double Data Rate) memory transfers data on both the rising and falling edges of the clock signal, effectively doubling the data transfer rate."
    },
    {
        "id": 64,
        "type": "multiple_choice",
        "question": "DDR4 provides:",
        "options": [
            "Lower speed than DDR3",
            "Higher data transfer rate than DDR3",
            "No performance improvement",
            "Less memory capacity"
        ],
        "correct_answer": 1,
        "explanation": "DDR4 offers higher data transfer rates, lower power consumption, and increased module density compared to DDR3."
    },
    {
        "id": 65,
        "type": "multiple_choice",
        "question": "DDR4 operates at:",
        "options": [
            "Lower voltage than DDR3",
            "Higher voltage than DDR3",
            "Equal voltage",
            "Random voltage"
        ],
        "correct_answer": 0,
        "explanation": "DDR4 typically operates at 1.2V compared to DDR3's 1.5V, resulting in better power efficiency."
    },
    {
        "id": 66,
        "type": "multiple_choice",
        "question": "DDR4 typically supports:",
        "options": [
            "Smaller memory capacity",
            "Larger memory modules",
            "No improvement",
            "Only cache storage"
        ],
        "correct_answer": 1,
        "explanation": "DDR4 supports larger capacity modules (up to 64GB per module compared to DDR3's 16GB limit) and higher overall system memory capacity."
    },
    {
        "id": 67,
        "type": "multiple_choice",
        "question": "Which memory type is newer?",
        "options": [
            "DDR2",
            "DDR3",
            "DDR4",
            "SDRAM"
        ],
        "correct_answer": 2,
        "explanation": "DDR4 is the newer generation compared to DDR2, DDR3, and original SDRAM (which predates DDR)."
    },
    {
        "id": 68,
        "type": "multiple_choice",
        "question": "EPROM stands for:",
        "options": [
            "Erasable Programmable Read Only Memory",
            "Electronic Programmable RAM",
            "Extended Programmable ROM",
            "External Program ROM"
        ],
        "correct_answer": 0,
        "explanation": "EPROM (Erasable Programmable Read-Only Memory) is a type of ROM that can be erased by exposure to ultraviolet light and reprogrammed."
    },
    {
        "id": 69,
        "type": "multiple_choice",
        "question": "EPROM is erased using:",
        "options": [
            "Electrical signals",
            "Magnetic fields",
            "Ultraviolet light",
            "Heat"
        ],
        "correct_answer": 2,
        "explanation": "EPROM chips have a quartz window that allows ultraviolet light to erase the stored data by discharging the floating gates."
    },
    {
        "id": 70,
        "type": "multiple_choice",
        "question": "EEPROM stands for:",
        "options": [
            "Electrically Erasable Programmable Read Only Memory",
            "Extended Erasable Program Memory",
            "Electronic External Program ROM",
            "Erased Electrical Program Memory"
        ],
        "correct_answer": 0,
        "explanation": "EEPROM (Electrically Erasable Programmable Read-Only Memory) can be erased and reprogrammed using electrical signals without removing it from the circuit."
    },
    {
        "id": 71,
        "type": "multiple_choice",
        "question": "EEPROM can be erased using:",
        "options": [
            "Ultraviolet light",
            "Electrical signals",
            "Magnetic fields",
            "Mechanical switches"
        ],
        "correct_answer": 1,
        "explanation": "EEPROM uses electrical voltages to erase and reprogram data, allowing in-circuit modification without special erasing equipment."
    },
    {
        "id": 72,
        "type": "multiple_choice",
        "question": "Flash memory is a type of:",
        "options": [
            "Magnetic memory",
            "EEPROM memory",
            "Optical storage",
            "Mechanical storage"
        ],
        "correct_answer": 1,
        "explanation": "Flash memory is a type of EEPROM that allows multiple memory locations to be erased or written in one programming operation."
    },
    {
        "id": 73,
        "type": "multiple_choice",
        "question": "Flash memory is commonly used in:",
        "options": [
            "USB drives and SSDs",
            "Printers",
            "Optical disks",
            "Magnetic tape"
        ],
        "correct_answer": 0,
        "explanation": "Flash memory is the primary storage medium in USB drives, solid-state drives (SSDs), memory cards, and mobile devices."
    },
    {
        "id": 74,
        "type": "multiple_choice",
        "question": "The main difference between EEPROM and Flash is:",
        "options": [
            "Flash erases data in blocks",
            "EEPROM erases in blocks",
            "Flash uses magnetic storage",
            "EEPROM cannot be rewritten"
        ],
        "correct_answer": 0,
        "explanation": "Flash memory erases data in larger blocks (typically kilobytes) while traditional EEPROM can erase individual bytes, making Flash faster for bulk operations but less flexible for byte-level updates."
    },
    {
        "id": 75,
        "type": "multiple_choice",
        "question": "A Solid State Drive (SSD) stores data using:",
        "options": [
            "Magnetic disks",
            "Flash memory chips",
            "Optical lasers",
            "Mechanical tapes"
        ],
        "correct_answer": 1,
        "explanation": "SSDs use NAND flash memory chips to store data persistently with no moving parts."
    },
    {
        "id": 76,
        "type": "multiple_choice",
        "question": "A magnetic drive stores data using:",
        "options": [
            "Flash memory",
            "Semiconductor chips",
            "Magnetized spinning disks",
            "Optical sensors"
        ],
        "correct_answer": 2,
        "explanation": "Magnetic hard disk drives (HDDs) store data by magnetizing thin films on rotating platters using read/write heads."
    },
    {
        "id": 77,
        "type": "multiple_choice",
        "question": "Compared to HDDs, SSDs generally provide:",
        "options": [
            "Slower performance",
            "Faster data access",
            "More mechanical parts",
            "Lower reliability"
        ],
        "correct_answer": 1,
        "explanation": "SSDs provide significantly faster data access, higher read/write speeds, and lower latency than HDDs due to no mechanical seek time."
    },
    {
        "id": 78,
        "type": "multiple_choice",
        "question": "Which storage device has moving mechanical parts?",
        "options": [
            "SSD",
            "Magnetic hard disk",
            "Flash drive",
            "Cache memory"
        ],
        "correct_answer": 1,
        "explanation": "Magnetic hard disks contain spinning platters and moving actuator arms with read/write heads, making them mechanical devices."
    },
    {
        "id": 79,
        "type": "multiple_choice",
        "question": "Which storage type consumes less power?",
        "options": [
            "Magnetic disk",
            "SSD",
            "Optical disk",
            "Tape storage"
        ],
        "correct_answer": 1,
        "explanation": "SSDs consume significantly less power than HDDs because they have no moving parts to spin or move, improving battery life in portable devices."
    },
    {
        "id": 80,
        "type": "multiple_choice",
        "question": "Using a glass substrate in magnetic disks improves:",
        "options": [
            "Mechanical fragility",
            "Surface smoothness and stability",
            "Electrical conductivity",
            "Heat generation"
        ],
        "correct_answer": 1,
        "explanation": "Glass substrates provide a smoother, more stable surface than aluminum, allowing for higher data density and more reliable operation."
    },
    {
        "id": 81,
        "type": "multiple_choice",
        "question": "One advantage of glass substrate disks is:",
        "options": [
            "Better resistance to shock and temperature",
            "Increased noise",
            "Slower disk rotation",
            "Reduced durability"
        ],
        "correct_answer": 0,
        "explanation": "Glass substrates are more rigid and resistant to temperature changes and mechanical shock compared to aluminum substrates."
    },
    {
        "id": 82,
        "type": "multiple_choice",
        "question": "RAID stands for:",
        "options": [
            "Redundant Array of Independent Disks",
            "Random Access Integrated Disk",
            "Rapid Access Input Disk",
            "Remote Access Integrated Drive"
        ],
        "correct_answer": 0,
        "explanation": "RAID (Redundant Array of Independent Disks) combines multiple physical disk drives into a single logical unit for data redundancy and/or performance improvement."
    },
    {
        "id": 83,
        "type": "multiple_choice",
        "question": "Redundancy in RAID is mainly achieved using:",
        "options": [
            "Data replication or parity",
            "Disk formatting",
            "Increased processor speed",
            "Cache memory"
        ],
        "correct_answer": 0,
        "explanation": "RAID achieves redundancy through either mirroring (complete data replication across disks) or parity (error-calculated data that can reconstruct lost information)."
    },
    {
        "id": 84,
        "type": "multiple_choice",
        "question": "Which statement correctly describes RAID 0?",
        "options": [
            "RAID 0 stores duplicate copies of data on two disks so one can replace the other if it fails.",
            "RAID 0 divides data into blocks and stripes it across multiple disks to improve performance, but it provides no redundancy or fault tolerance, meaning if one disk fails all the data is lost.",
            "RAID 0 stores parity information on a separate disk to recover lost data.",
            "RAID 0 stores two copies of data and parity information together."
        ],
        "correct_answer": 1,
        "explanation": "RAID 0 uses striping to improve performance but offers no redundancy. Failure of any disk results in complete data loss for the entire array."
    },
    {
        "id": 85,
        "type": "multiple_choice",
        "question": "Which statement correctly explains RAID 1?",
        "options": [
            "RAID 1 splits data across disks without protection.",
            "RAID 1 uses parity information stored on a single disk.",
            "RAID 1 mirrors data by storing identical copies of the same data on two or more disks so that if one disk fails the system can continue operating using the duplicate copy.",
            "RAID 1 distributes parity across several disks."
        ],
        "correct_answer": 2,
        "explanation": "RAID 1 provides redundancy through mirroring. Data written to one disk is simultaneously written to another disk, creating an exact copy for fault tolerance."
    },
    {
        "id": 86,
        "type": "multiple_choice",
        "question": "Which statement best defines RAID 2?",
        "options": [
            "RAID 2 uses bit-level striping across multiple disks and stores error correction codes (ECC) on additional disks to detect and correct data errors.",
            "RAID 2 mirrors data across disks for redundancy.",
            "RAID 2 stores parity information across multiple disks without striping.",
            "RAID 2 splits data across disks without error correction."
        ],
        "correct_answer": 0,
        "explanation": "RAID 2 stripes data at the bit level and uses Hamming code ECC disks for error correction, though it's rarely implemented in practice."
    },
    {
        "id": 87,
        "type": "multiple_choice",
        "question": "Which description best explains RAID 3?",
        "options": [
            "RAID 3 stores duplicate copies of data on all disks.",
            "RAID 3 uses byte-level striping across several disks and stores parity information on a dedicated disk, allowing the system to reconstruct lost data if one disk fails.",
            "RAID 3 removes parity completely to improve speed.",
            "RAID 3 distributes parity across all disks."
        ],
        "correct_answer": 1,
        "explanation": "RAID 3 stripes data at the byte level across multiple disks and uses a dedicated parity disk for error recovery."
    },
    {
        "id": 88,
        "type": "multiple_choice",
        "question": "Which statement best describes RAID 4?",
        "options": [
            "RAID 4 mirrors all data across disks.",
            "RAID 4 uses block-level striping across multiple disks with one dedicated disk used to store parity information for data recovery.",
            "RAID 4 removes redundancy completely.",
            "RAID 4 stores three copies of every file."
        ],
        "correct_answer": 1,
        "explanation": "RAID 4 uses block-level striping and a dedicated parity disk, similar to RAID 3 but with block-level rather than byte-level striping."
    },
    {
        "id": 89,
        "type": "multiple_choice",
        "question": "Which option correctly explains RAID 5?",
        "options": [
            "RAID 5 mirrors data across all disks.",
            "RAID 5 stores data on one disk only.",
            "RAID 5 uses block-level striping and distributes parity information across all disks in the array, improving reliability and avoiding the single parity disk bottleneck.",
            "RAID 5 uses only error correction codes."
        ],
        "correct_answer": 2,
        "explanation": "RAID 5 stripes data and parity information across all disks, eliminating the dedicated parity disk bottleneck while maintaining single-disk fault tolerance."
    },
    {
        "id": 90,
        "type": "multiple_choice",
        "question": "Which statement best defines RAID 6?",
        "options": [
            "RAID 6 removes parity and redundancy.",
            "RAID 6 uses block-level striping with dual distributed parity, allowing the system to recover data even if two disks fail simultaneously.",
            "RAID 6 mirrors data on only one disk.",
            "RAID 6 stores data sequentially on a single disk."
        ],
        "correct_answer": 1,
        "explanation": "RAID 6 provides fault tolerance for up to two disk failures by using two independent parity calculations distributed across all disks."
    },
    {
        "id": 91,
        "type": "multiple_choice",
        "question": "What is the main purpose of external devices in a computer system?",
        "options": [
            "To increase CPU speed",
            "To provide a means of exchanging data between the external environment and the computer",
            "To replace memory modules",
            "To perform arithmetic operations"
        ],
        "correct_answer": 1,
        "explanation": "External devices (peripherals) allow the computer to interact with the outside world, receiving input and delivering output."
    },
    {
        "id": 92,
        "type": "multiple_choice",
        "question": "External devices are also commonly referred to as:",
        "options": [
            "Processors",
            "Peripheral devices",
            "Memory controllers",
            "Cache modules"
        ],
        "correct_answer": 1,
        "explanation": "External devices are most commonly called peripherals, as they are auxiliary devices that connect to and work with the computer."
    },
    {
        "id": 93,
        "type": "multiple_choice",
        "question": "Which category of external device is used for communication with users?",
        "options": [
            "Machine readable devices",
            "Communication devices",
            "Human readable devices",
            "Network processors"
        ],
        "correct_answer": 2,
        "explanation": "Human readable devices are designed to communicate information directly to or from a user, such as monitors, printers, and keyboards."
    },
    {
        "id": 94,
        "type": "multiple_choice",
        "question": "Which of the following is an example of a machine-readable device?",
        "options": [
            "Printer",
            "Keyboard",
            "Magnetic disk",
            "Monitor"
        ],
        "correct_answer": 2,
        "explanation": "Machine-readable devices are designed to communicate with other machines or systems. A magnetic disk stores data for the computer to read, not directly for a human."
    },
    {
        "id": 95,
        "type": "multiple_choice",
        "question": "Communication devices are used mainly for:",
        "options": [
            "Communicating with remote devices or systems",
            "Displaying information to the user",
            "Storing operating systems",
            "Performing arithmetic calculations"
        ],
        "correct_answer": 0,
        "explanation": "Communication devices, like network interface cards and modems, enable a computer to exchange data with other computer systems over a distance."
    },
    {
        "id": 96,
        "type": "multiple_choice",
        "question": "Which signals determine the function an external device performs such as read or write?",
        "options": [
            "Status signals",
            "Control signals",
            "Data signals",
            "Address signals"
        ],
        "correct_answer": 1,
        "explanation": "Control signals from the I/O module specify the operation the external device should perform, such as a read, write, or seek operation."
    },
    {
        "id": 97,
        "type": "multiple_choice",
        "question": "What do status signals indicate in an external device?",
        "options": [
            "The amount of stored data",
            "The condition of the device such as READY, BUSY, or ERROR",
            "The speed of the processor",
            "The number of connected devices"
        ],
        "correct_answer": 1,
        "explanation": "Status signals report the current state of the I/O device back to the I/O module, indicating whether it is ready for a new command, busy, or has encountered an error."
    },
    {
        "id": 98,
        "type": "multiple_choice",
        "question": "Data exchanged between an I/O module and an external device is transmitted in the form of:",
        "options": [
            "Electrical waves",
            "Bits",
            "Packets",
            "Characters only"
        ],
        "correct_answer": 1,
        "explanation": "At its most fundamental level, all data exchanged between a computer and any device is transmitted as a stream of bits."
    },
    {
        "id": 99,
        "type": "multiple_choice",
        "question": "The computer system's I/O architecture refers to:",
        "options": [
            "The structure of CPU instructions",
            "The interface between the computer and the outside world",
            "The design of memory modules",
            "The layout of hard disks"
        ],
        "correct_answer": 1,
        "explanation": "The I/O architecture is the totality of the hardware and software that provides the interface and manages the data flow between the computer system and the external environment."
    },
    {
        "id": 100,
        "type": "multiple_choice",
        "question": "Which of the following is considered the third key element of a computer system besides the CPU and memory?",
        "options": [
            "Network interface",
            "I/O modules",
            "Cache controller",
            "Power supply"
        ],
        "correct_answer": 1,
        "explanation": "A computer system is fundamentally composed of three key interconnected components: the Central Processing Unit (CPU), memory, and Input/Output (I/O) modules."
    },
    {
        "id": 101,
        "type": "multiple_choice",
        "question": "An I/O module mainly acts as:",
        "options": [
            "A bridge between the system bus and peripheral devices",
            "A replacement for memory",
            "A processor controller",
            "A power regulator"
        ],
        "correct_answer": 0,
        "explanation": "The I/O module is the interface that connects the internal high-speed system bus to the various external peripheral devices, handling the necessary data conversions and control signals."
    },
    {
        "id": 102,
        "type": "multiple_choice",
        "question": "Which of the following is NOT one of the major functions of an I/O module?",
        "options": [
            "Control and timing",
            "Device communication",
            "Arithmetic processing",
            "Error detection"
        ],
        "correct_answer": 2,
        "explanation": "Arithmetic processing is the primary function of the CPU's ALU (Arithmetic Logic Unit), not the I/O module. I/O modules handle control, communication, buffering, and error detection."
    },
    {
        "id": 103,
        "type": "multiple_choice",
        "question": "The function of data buffering in an I/O module is to:",
        "options": [
            "Increase processor speed",
            "Temporarily store data before sending it to the device at its required data rate",
            "Encrypt transmitted data",
            "Replace system memory"
        ],
        "correct_answer": 1,
        "explanation": "Data buffering compensates for the speed difference between the fast system bus and the slower peripheral device by temporarily storing data until the device is ready."
    },
    {
        "id": 104,
        "type": "multiple_choice",
        "question": "Error detection in an I/O module helps to:",
        "options": [
            "Increase storage capacity",
            "Detect mechanical or electrical malfunctions and data corruption",
            "Improve processor instruction speed",
            "Reduce device power consumption"
        ],
        "correct_answer": 1,
        "explanation": "I/O modules often include error detection mechanisms, such as parity bits, to identify errors that may occur during data transmission due to device malfunctions or noise."
    },
    {
        "id": 105,
        "type": "multiple_choice",
        "question": "In programmed I/O, the processor:",
        "options": [
            "Transfers data directly between memory and device without control",
            "Has continuous control over the I/O operation and waits until it is complete",
            "Never interacts with the I/O module",
            "Uses another processor to handle the operation"
        ],
        "correct_answer": 1,
        "explanation": "In programmed I/O, the CPU is in a loop, constantly checking the status of the I/O module and directly controlling every step of the data transfer, which wastes CPU time."
    },
    {
        "id": 106,
        "type": "multiple_choice",
        "question": "In interrupt-driven I/O, the processor:",
        "options": [
            "Stops all tasks permanently during I/O operations",
            "Continues executing other instructions and is interrupted when the I/O operation finishes",
            "Transfers data directly without interruption",
            "Disconnects from memory during I/O"
        ],
        "correct_answer": 1,
        "explanation": "Interrupt-driven I/O improves efficiency. The CPU issues an I/O command and continues with other work. The I/O module sends an interrupt signal to the CPU when the operation is complete."
    },
    {
        "id": 107,
        "type": "multiple_choice",
        "question": "In Direct Memory Access (DMA), data transfer occurs:",
        "options": [
            "Directly between the I/O module and main memory without continuous CPU involvement",
            "Only between the CPU and registers",
            "Between external devices and cache memory",
            "Through manual CPU control"
        ],
        "correct_answer": 0,
        "explanation": "DMA allows a specialized controller to handle data transfers directly between an I/O device and memory, freeing the CPU to perform other tasks concurrently."
    },
    {
        "id": 108,
        "type": "multiple_choice",
        "question": "Which command from the CPU tells the I/O module what operation to perform?",
        "options": [
            "Test command",
            "Control command",
            "Read command",
            "Write command"
        ],
        "correct_answer": 1,
        "explanation": "A control command is used by the CPU to instruct the I/O module to perform a specific operation, such as rewinding a tape or seeking a track on a disk."
    },
    {
        "id": 109,
        "type": "multiple_choice",
        "question": "Which CPU command checks whether the I/O device is ready, busy, or has errors?",
        "options": [
            "Write",
            "Read",
            "Test",
            "Control"
        ],
        "correct_answer": 2,
        "explanation": "The test command is used by the CPU to query the status of an I/O module and its associated devices, checking condition flags like 'ready', 'busy', or 'error'."
    },
    {
        "id": 110,
        "type": "multiple_choice",
        "question": "An I/O processor differs from a simple I/O module because it:",
        "options": [
            "Has its own specialized instruction set and can execute I/O programs independently",
            "Only sends signals to memory",
            "Replaces the CPU entirely",
            "Removes peripheral devices from the system"
        ],
        "correct_answer": 0,
        "explanation": "An I/O processor is a more sophisticated controller with its own local memory and instruction set, capable of executing entire I/O programs without direct intervention from the main CPU."
    }


        
    ]
}
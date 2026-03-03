computer_organization_quiz = {
    "course_code": "BCP 203",
    "course_name": "Computer Organization Architecture",
    "total_questions": 50,
    "questions": [
        # Multiple Choice Questions (1-25)
        
    
    {
        "id": 1,
        "type": "multiple_choice",
        "question": "A computer where both program instructions and data share the same memory and bus is based on",
        "options": [
            "Harvard architecture",
            "Von Neumann architecture",
            "Parallel architecture",
            "Distributed architecture"
        ],
        "correct_answer": 1,
        "explanation": "The Von Neumann architecture is characterized by a single shared memory space and bus for both instructions and data."
    },
    {
        "id": 2,
        "type": "multiple_choice",
        "question": "The main performance limitation in Von Neumann architecture occurs because",
        "options": [
            "memory is too large",
            "instructions are too small",
            "data and instructions share one bus",
            "there is no cache"
        ],
        "correct_answer": 2,
        "explanation": "The shared bus creates a bottleneck, often called the Von Neumann bottleneck, as instructions and data compete for the same pathway, limiting throughput."
    },
    {
        "id": 3,
        "type": "multiple_choice",
        "question": "Harvard architecture improves performance mainly because",
        "options": [
            "it removes RAM",
            "it separates data and instruction paths",
            "it increases voltage",
            "it reduces registers"
        ],
        "correct_answer": 1,
        "explanation": "By using separate memory and buses for instructions and data, the CPU can fetch both simultaneously, reducing wait times and improving performance."
    },
    {
        "id": 4,
        "type": "multiple_choice",
        "question": "Moore's Law predicts that over time",
        "options": [
            "transistor count decreases",
            "processor speed remains constant",
            "transistor count doubles about every two years",
            "memory disappears"
        ],
        "correct_answer": 2,
        "explanation": "Moore's Law is the observation that the number of transistors on a microchip doubles approximately every two years, though it's more of a trend than a physical law."
    },
    {
        "id": 5,
        "type": "multiple_choice",
        "question": "According to Amdahl's Law, if only 30 percent of a system is improved, the overall speed gain will",
        "options": [
            "be unlimited",
            "depend on the unimproved portion",
            "double automatically",
            "ignore slow components"
        ],
        "correct_answer": 1,
        "explanation": "Amdahl's Law states that the overall speedup is limited by the portion of the system that cannot be improved. The unimproved part becomes the bottleneck."
    },
    {
        "id": 6,
        "type": "multiple_choice",
        "question": "Little's Law shows that system performance depends on",
        "options": [
            "temperature and voltage",
            "number of tasks and time spent in system",
            "transistor size only",
            "clock speed only"
        ],
        "correct_answer": 1,
        "explanation": "Little's Law (L = λW) states that the average number of tasks in a system (L) is equal to the average arrival rate (λ) multiplied by the average time a task spends in the system (W)."
    },
    {
        "id": 7,
        "type": "multiple_choice",
        "question": "An embedded system is best described as a computer that",
        "options": [
            "runs many operating systems",
            "performs a dedicated function inside a larger device",
            "stores unlimited data",
            "replaces servers"
        ],
        "correct_answer": 1,
        "explanation": "Embedded systems are specialized computing systems designed for specific control functions within larger systems, often with real-time computing constraints."
    },
    {
        "id": 8,
        "type": "multiple_choice",
        "question": "ARM processors are widely used in embedded systems because they",
        "options": [
            "consume high power",
            "are designed for low power and efficiency",
            "are magnetic",
            "are mechanical"
        ],
        "correct_answer": 1,
        "explanation": "ARM processors utilize a RISC architecture known for its low power consumption and high energy efficiency, making them ideal for battery-powered and heat-sensitive embedded devices."
    },
    {
        "id": 9,
        "type": "multiple_choice",
        "question": "Registers are implemented using flip flops because flip flops",
        "options": [
            "store analog signals",
            "store binary values reliably and quickly",
            "reduce disk space",
            "generate clock pulses"
        ],
        "correct_answer": 1,
        "explanation": "Flip-flops are bistable circuits that can hold a binary state (0 or 1) indefinitely until changed, making them the fundamental building blocks for fast, reliable storage in registers."
    },
    {
        "id": 10,
        "type": "multiple_choice",
        "question": "During instruction execution, the Program Counter contains",
        "options": [
            "the result of arithmetic",
            "the next instruction address",
            "memory data",
            "parity bits"
        ],
        "correct_answer": 1,
        "explanation": "The Program Counter (PC) is a special-purpose register that holds the memory address of the next instruction to be fetched and executed."
    },
    {
        "id": 11,
        "type": "multiple_choice",
        "question": "The Instruction Register holds the instruction that is",
        "options": [
            "about to be written to disk",
            "currently being decoded or executed",
            "stored in cache permanently",
            "erased from memory"
        ],
        "correct_answer": 1,
        "explanation": "The Instruction Register (IR) stores the current instruction fetched from memory while it is being decoded and executed by the control unit."
    },
    {
        "id": 12,
        "type": "multiple_choice",
        "question": "The MAR is directly connected to the",
        "options": [
            "data bus only",
            "control bus only",
            "address bus",
            "printer"
        ],
        "correct_answer": 2,
        "explanation": "The Memory Address Register (MAR) holds the address of a memory location to be accessed. It is directly connected to the address bus, which carries this address to memory."
    },
    {
        "id": 13,
        "type": "multiple_choice",
        "question": "The MDR temporarily holds",
        "options": [
            "memory addresses",
            "data read from or written to memory",
            "control signals",
            "CPU temperature"
        ],
        "correct_answer": 1,
        "explanation": "The Memory Data Register (MDR), also called the Memory Buffer Register (MBR), acts as a temporary buffer for data being transferred to or from memory via the data bus."
    },
    {
        "id": 14,
        "type": "multiple_choice",
        "question": "The first step in the fetch decode execute cycle is",
        "options": [
            "execute",
            "fetch instruction from memory",
            "store result",
            "decode instruction"
        ],
        "correct_answer": 1,
        "explanation": "The instruction cycle begins with the fetch phase, where the CPU retrieves the next instruction from the memory address pointed to by the Program Counter."
    },
    {
        "id": 15,
        "type": "multiple_choice",
        "question": "The system bus acts as",
        "options": [
            "permanent storage",
            "communication pathway between CPU, memory, and I O",
            "backup memory",
            "arithmetic unit"
        ],
        "correct_answer": 1,
        "explanation": "The system bus is a set of parallel wires or communication pathways that connect the major components of a computer: the CPU, main memory, and I/O modules."
    },
    {
        "id": 16,
        "type": "multiple_choice",
        "question": "The data bus width determines",
        "options": [
            "how many addresses exist",
            "how many bits move at once",
            "disk rotation speed",
            "number of monitors"
        ],
        "correct_answer": 1,
        "explanation": "The width of the data bus (in bits) determines how much data can be transferred simultaneously between components in a single bus cycle."
    },
    {
        "id": 17,
        "type": "multiple_choice",
        "question": "Increasing address bus width increases",
        "options": [
            "memory capacity",
            "clock speed",
            "voltage",
            "cache size"
        ],
        "correct_answer": 0,
        "explanation": "The address bus width determines the maximum number of unique memory addresses the CPU can reference, directly limiting the system's maximum addressable memory capacity."
    },
    {
        "id": 18,
        "type": "multiple_choice",
        "question": "SRAM is faster than DRAM because SRAM",
        "options": [
            "uses capacitors",
            "requires refreshing",
            "uses flip flop circuits and no refresh",
            "is magnetic"
        ],
        "correct_answer": 2,
        "explanation": "SRAM uses flip-flops (typically 4-6 transistors per cell) to store data, which does not require constant refreshing and provides faster access times than DRAM's capacitor-based storage."
    },
    {
        "id": 19,
        "type": "multiple_choice",
        "question": "DRAM is cheaper per bit because",
        "options": [
            "its cells are simpler and smaller",
            "it uses glass",
            "it has no refresh",
            "it is external"
        ],
        "correct_answer": 0,
        "explanation": "DRAM cells consist of only one transistor and one capacitor, making them physically smaller and simpler to manufacture than SRAM cells, leading to higher density and lower cost per bit."
    },
    {
        "id": 20,
        "type": "multiple_choice",
        "question": "Cache memory improves performance by",
        "options": [
            "increasing disk size",
            "storing frequently used data close to CPU",
            "slowing memory",
            "reducing bus lines"
        ],
        "correct_answer": 1,
        "explanation": "Cache is a small, fast memory located close to the CPU that holds copies of frequently accessed data and instructions, reducing the average time to access data from main memory."
    },
    {
        "id": 21,
        "type": "multiple_choice",
        "question": "DDR4 differs from DDR3 mainly in",
        "options": [
            "having no banks",
            "using lower voltage and higher speeds",
            "using UV light",
            "being magnetic"
        ],
        "correct_answer": 1,
        "explanation": "DDR4 SDRAM provides improvements over DDR3, including higher module densities, higher data transfer rates, and lower operating voltages (typically 1.2V compared to 1.5V for DDR3)."
    },
    {
        "id": 22,
        "type": "multiple_choice",
        "question": "EPROM differs from EEPROM because EPROM",
        "options": [
            "is erased electrically",
            "is erased using ultraviolet light",
            "cannot be erased",
            "is volatile"
        ],
        "correct_answer": 1,
        "explanation": "EPROM (Erasable Programmable Read-Only Memory) chips have a quartz window and are erased by exposing the die to intense ultraviolet light, whereas EEPROM (Electrically Erasable PROM) can be erased electrically."
    },
    {
        "id": 23,
        "type": "multiple_choice",
        "question": "Flash memory improves on EEPROM by",
        "options": [
            "erasing entire blocks at once",
            "using UV light",
            "being volatile",
            "using parity disks"
        ],
        "correct_answer": 0,
        "explanation": "Flash memory is a type of EEPROM that allows data to be written or erased in blocks, which is much faster than the byte-by-byte erasure and writing of traditional EEPROM."
    },
    {
        "id": 24,
        "type": "multiple_choice",
        "question": "An SSD is faster than a magnetic drive mainly because it",
        "options": [
            "spins faster",
            "has no moving mechanical parts",
            "uses glass substrate",
            "uses parity"
        ],
        "correct_answer": 1,
        "explanation": "Solid State Drives (SSDs) use flash memory with no moving parts, allowing for near-instantaneous data access. This eliminates the mechanical seek time and rotational latency inherent in HDDs."
    },
    {
        "id": 25,
        "type": "multiple_choice",
        "question": "Magnetic hard drives store data by",
        "options": [
            "electrical charge only",
            "magnetic orientation on spinning platters",
            "laser reflection",
            "flip flops"
        ],
        "correct_answer": 1,
        "explanation": "HDDs store data by magnetizing tiny regions (domains) on the surface of spinning magnetic platters in one of two directions, representing binary 0s and 1s."
    },
    {
        "id": 26,
        "type": "multiple_choice",
        "question": "Using glass substrate in disks improves",
        "options": [
            "fragility",
            "surface smoothness and rigidity",
            "voltage",
            "refresh rate"
        ],
        "correct_answer": 1,
        "explanation": "Glass substrates for hard drive platters are smoother, more rigid, and more thermally stable than aluminum, allowing for higher data densities and more reliable performance."
    },
    {
        "id": 27,
        "type": "multiple_choice",
        "question": "RAID 0 increases performance by",
        "options": [
            "mirroring data",
            "adding parity",
            "striping data across disks without redundancy",
            "duplicating disks"
        ],
        "correct_answer": 2,
        "explanation": "RAID 0 (striping) splits data across multiple disks, allowing for parallel reads and writes which increases performance. However, it provides no fault tolerance."
    },
    {
        "id": 28,
        "type": "multiple_choice",
        "question": "RAID 1 protects data by",
        "options": [
            "striping",
            "mirroring identical copies",
            "compression",
            "caching"
        ],
        "correct_answer": 1,
        "explanation": "RAID 1 (mirroring) writes identical data to two or more drives simultaneously. If one drive fails, the data is still available from the other mirrored drive(s)."
    },
    {
        "id": 29,
        "type": "multiple_choice",
        "question": "RAID 5 achieves fault tolerance by",
        "options": [
            "no redundancy",
            "storing distributed parity across disks",
            "single disk storage",
            "UV erasing"
        ],
        "correct_answer": 1,
        "explanation": "RAID 5 stripes data and parity information across all disks in the array. If one disk fails, the missing data can be calculated from the remaining data and parity."
    },
    {
        "id": 30,
        "type": "multiple_choice",
        "question": "RAID 6 can tolerate",
        "options": [
            "zero failures",
            "one disk failure",
            "two disk failures",
            "unlimited failures"
        ],
        "correct_answer": 2,
        "explanation": "RAID 6 uses double distributed parity, allowing the array to continue functioning and rebuild data even if two disks fail simultaneously."
    },
    {
        "id": 31,
        "type": "multiple_choice",
        "question": "Internal memory is directly accessible by",
        "options": [
            "printer",
            "CPU",
            "monitor",
            "network switch"
        ],
        "correct_answer": 1,
        "explanation": "Internal memory, primarily RAM, is directly addressable and accessible by the CPU via the memory bus, allowing for fast read and write operations during program execution."
    },
    {
        "id": 32,
        "type": "multiple_choice",
        "question": "External memory is mainly used for",
        "options": [
            "temporary CPU storage",
            "long term data storage",
            "arithmetic",
            "decoding"
        ],
        "correct_answer": 1,
        "explanation": "External memory, such as HDDs and SSDs, provides non-volatile, long-term storage for data and programs, even when the power is turned off."
    },
    {
        "id": 33,
        "type": "multiple_choice",
        "question": "Virtual memory allows",
        "options": [
            "RAM to shrink",
            "programs larger than physical RAM to run",
            "cache removal",
            "no storage"
        ],
        "correct_answer": 1,
        "explanation": "Virtual memory uses a portion of the hard drive (or SSD) as an extension of physical RAM, enabling a system to run programs that require more memory than is physically available."
    },
    {
        "id": 34,
        "type": "multiple_choice",
        "question": "Disk cache reduces access time by",
        "options": [
            "deleting data",
            "storing recently accessed disk data temporarily",
            "slowing rotation",
            "compressing files"
        ],
        "correct_answer": 1,
        "explanation": "A disk cache is a small amount of fast memory (often DRAM) on the disk controller or in main memory that stores recently accessed data, anticipating future requests and avoiding slow disk accesses."
    },
    {
        "id": 35,
        "type": "multiple_choice",
        "question": "A hardwired program means control signals are generated by",
        "options": [
            "software only",
            "hardware circuits",
            "operating system",
            "disk"
        ],
        "correct_answer": 1,
        "explanation": "In a hardwired control unit, the control signals are generated directly by fixed logic circuits (gates, flip-flops, etc.) based on the current instruction and state."
    },
    {
        "id": 36,
        "type": "multiple_choice",
        "question": "DMA improves performance because it",
        "options": [
            "removes RAM",
            "allows I O to transfer data without constant CPU involvement",
            "reduces registers",
            "erases memory"
        ],
        "correct_answer": 1,
        "explanation": "Direct Memory Access (DMA) allows I/O devices to transfer data directly to or from memory without continuous intervention from the CPU, freeing the CPU to perform other tasks."
    },
    {
        "id": 37,
        "type": "multiple_choice",
        "question": "The accumulator is mainly used for",
        "options": [
            "storing addresses",
            "holding intermediate arithmetic results",
            "parity storage",
            "disk buffering"
        ],
        "correct_answer": 1,
        "explanation": "The accumulator is a register in the CPU that temporarily stores the results of arithmetic and logical operations performed by the ALU."
    },
    {
        "id": 38,
        "type": "multiple_choice",
        "question": "In DRAM, information is stored as",
        "options": [
            "magnetic field",
            "electrical charge in capacitors",
            "light",
            "mechanical position"
        ],
        "correct_answer": 1,
        "explanation": "Dynamic RAM (DRAM) stores each bit of data as an electrical charge in a tiny capacitor. The presence or absence of charge represents a 1 or 0."
    },
    {
        "id": 39,
        "type": "multiple_choice",
        "question": "The control bus carries signals such as",
        "options": [
            "read and write commands",
            "memory addresses",
            "arithmetic data",
            "transistor count"
        ],
        "correct_answer": 0,
        "explanation": "The control bus carries command and timing signals from the control unit to coordinate activities. Common signals include Memory Read, Memory Write, I/O Read, and I/O Write."
    },
    {
        "id": 40,
        "type": "multiple_choice",
        "question": "Increasing cache size generally",
        "options": [
            "increases access time drastically",
            "reduces hit rate",
            "increases hit rate and performance",
            "removes RAM"
        ],
        "correct_answer": 2,
        "explanation": "A larger cache can hold more data, increasing the probability (hit rate) that requested data is found in the cache. This generally improves performance, though with diminishing returns."
    },
    {
        "id": 41,
        "type": "multiple_choice",
        "question": "In a stored program computer, instructions are",
        "options": [
            "stored only in CPU",
            "stored in main memory with data",
            "stored in hard disk only",
            "executed directly from keyboard"
        ],
        "correct_answer": 1,
        "explanation": "The fundamental concept of the stored-program computer (Von Neumann architecture) is that both program instructions and data are stored together in main memory."
    },
    {
        "id": 42,
        "type": "multiple_choice",
        "question": "The Von Neumann bottleneck refers to",
        "options": [
            "limited disk space",
            "shared path between CPU and memory",
            "low transistor count",
            "slow monitor refresh rate"
        ],
        "correct_answer": 1,
        "explanation": "The Von Neumann bottleneck describes the limitation of throughput caused by the single shared bus between the CPU and memory, which must be used for both instruction fetches and data transfers."
    },
    {
        "id": 43,
        "type": "multiple_choice",
        "question": "If the address bus is 32 bits wide, the maximum addressable memory is",
        "options": [
            "2^16 locations",
            "2^32 locations",
            "32 bytes",
            "32 KB"
        ],
        "correct_answer": 1,
        "explanation": "A 32-bit address bus can generate 2^32 unique addresses, allowing the CPU to directly address up to 4 GiB of memory (if each address points to a byte)."
    },
    {
        "id": 44,
        "type": "multiple_choice",
        "question": "Increasing the data bus width mainly increases",
        "options": [
            "memory capacity",
            "number of I O devices",
            "amount of data transferred per cycle",
            "disk speed"
        ],
        "correct_answer": 2,
        "explanation": "A wider data bus allows more bits to be transferred in a single bus cycle, directly increasing the data transfer rate between the CPU, memory, and I/O devices."
    },
    {
        "id": 45,
        "type": "multiple_choice",
        "question": "The purpose of refresh in DRAM is to",
        "options": [
            "increase speed",
            "restore lost electrical charge",
            "reduce voltage",
            "increase parity"
        ],
        "correct_answer": 1,
        "explanation": "DRAM cells store data as charge on a capacitor, which leaks over time. The memory controller periodically reads and rewrites (refreshes) each cell to restore the charge and prevent data loss."
    },
    {
        "id": 46,
        "type": "multiple_choice",
        "question": "SRAM consumes more power than DRAM because it",
        "options": [
            "uses magnetic storage",
            "uses more transistors per cell",
            "refreshes constantly",
            "uses UV light"
        ],
        "correct_answer": 1,
        "explanation": "SRAM cells typically use 4-6 transistors to form a flip-flop, which draws continuous leakage current. In contrast, a DRAM cell uses only one transistor and one capacitor."
    },
    {
        "id": 47,
        "type": "multiple_choice",
        "question": "A key advantage of SSD over HDD is",
        "options": [
            "higher noise",
            "mechanical parts",
            "faster access time",
            "spinning disks"
        ],
        "correct_answer": 2,
        "explanation": "SSDs have no moving parts, resulting in significantly faster access times (low latency) and much higher random I/O performance compared to HDDs."
    },
    {
        "id": 48,
        "type": "multiple_choice",
        "question": "RAID redundancy ensures that",
        "options": [
            "data cannot be deleted",
            "system never fails",
            "data can be recovered after disk failure",
            "storage capacity doubles automatically"
        ],
        "correct_answer": 2,
        "explanation": "RAID (Redundant Array of Independent Disks) uses techniques like mirroring or parity to provide fault tolerance, allowing data to be reconstructed if a disk in the array fails."
    },
    {
        "id": 49,
        "type": "multiple_choice",
        "question": "RAID 3 uses",
        "options": [
            "block level striping with distributed parity",
            "byte level striping with dedicated parity disk",
            "mirroring only",
            "no redundancy"
        ],
        "correct_answer": 1,
        "explanation": "RAID 3 stripes data at the byte level across multiple data disks and uses a single, dedicated parity disk to store parity information for error recovery."
    },
    {
        "id": 50,
        "type": "multiple_choice",
        "question": "RAID 4 differs from RAID 5 because RAID 4",
        "options": [
            "uses distributed parity",
            "uses dedicated parity disk",
            "uses mirroring",
            "has no parity"
        ],
        "correct_answer": 1,
        "explanation": "RAID 4 uses block-level striping with a dedicated parity disk. RAID 5 also uses block-level striping but distributes the parity information across all disks in the array, avoiding the dedicated parity disk bottleneck."
    },
    {
        "id": 51,
        "type": "multiple_choice",
        "question": "The main role of cache memory is to reduce",
        "options": [
            "disk size",
            "memory access time",
            "voltage",
            "CPU registers"
        ],
        "correct_answer": 1,
        "explanation": "Cache memory reduces the average time (latency) for the CPU to access data and instructions by providing a small, fast storage layer close to the CPU core."
    },
    {
        "id": 52,
        "type": "multiple_choice",
        "question": "Virtual memory works by",
        "options": [
            "replacing RAM",
            "using part of secondary storage as extension of RAM",
            "deleting unused files",
            "compressing cache"
        ],
        "correct_answer": 1,
        "explanation": "Virtual memory maps virtual addresses used by a program to physical addresses in RAM or to addresses on secondary storage (like a hard drive), using the disk as an extension of RAM."
    },
    {
        "id": 53,
        "type": "multiple_choice",
        "question": "EPROM must be erased",
        "options": [
            "electrically inside the system",
            "by ultraviolet light after removing chip",
            "by magnetic field",
            "automatically"
        ],
        "correct_answer": 1,
        "explanation": "EPROM chips have a transparent quartz window. To erase the data, the chip must be removed from the circuit and exposed to intense ultraviolet light for a period of time."
    },
    {
        "id": 54,
        "type": "multiple_choice",
        "question": "EEPROM differs from Flash because EEPROM",
        "options": [
            "erases entire blocks at once",
            "erases byte by byte",
            "uses UV light",
            "is volatile"
        ],
        "correct_answer": 1,
        "explanation": "Traditional EEPROM allows erasing and writing of individual bytes, whereas Flash memory, a faster and denser type of EEPROM, operates on larger blocks of data."
    },
    {
        "id": 55,
        "type": "multiple_choice",
        "question": "During execution, after an instruction is executed, the CPU",
        "options": [
            "shuts down",
            "clears memory",
            "updates the Program Counter",
            "erases cache"
        ],
        "correct_answer": 2,
        "explanation": "After executing an instruction, the CPU typically updates the Program Counter (PC) to point to the next instruction in the sequence, unless a jump or branch occurred."
    },
    {
        "id": 56,
        "type": "multiple_choice",
        "question": "An interconnection structure allows transfer between",
        "options": [
            "CPU and CPU only",
            "CPU, memory, and I O devices",
            "monitor and keyboard only",
            "disk and printer only"
        ],
        "correct_answer": 1,
        "explanation": "The system's interconnection structure, typically one or more buses, provides the communication pathways for data and control signals to flow between the CPU, main memory, and I/O modules."
    },
    {
        "id": 57,
        "type": "multiple_choice",
        "question": "In Harvard architecture, simultaneous access to data and instructions",
        "options": [
            "is impossible",
            "slows down CPU",
            "improves performance",
            "deletes memory"
        ],
        "correct_answer": 2,
        "explanation": "Because Harvard architecture uses separate memory and buses for instructions and data, the CPU can fetch an instruction and read/write data in the same clock cycle, improving throughput."
    },
    {
        "id": 58,
        "type": "multiple_choice",
        "question": "Moore's Law mainly explains the growth of",
        "options": [
            "disk rotation speed",
            "transistor density on chips",
            "RAM voltage",
            "bus width"
        ],
        "correct_answer": 1,
        "explanation": "Moore's Law is an observation about the exponential increase in the number of transistors that can be placed on an integrated circuit, leading to improvements in performance and capability."
    },
    {
        "id": 59,
        "type": "multiple_choice",
        "question": "According to Amdahl's Law, to achieve large speed improvement you must",
        "options": [
            "improve every part equally",
            "focus on the part that consumes most execution time",
            "increase voltage",
            "reduce memory size"
        ],
        "correct_answer": 1,
        "explanation": "Amdahl's Law implies that the greatest overall speedup is achieved by improving the component or part of a task that accounts for the largest portion of the execution time."
    },
    {
        "id": 60,
        "type": "multiple_choice",
        "question": "According to Little's Law, if the average time tasks spend in a system increases and arrival rate stays constant",
        "options": [
            "number of tasks in system increases",
            "throughput decreases automatically",
            "memory doubles",
            "CPU stops"
        ],
        "correct_answer": 0,
        "explanation": "Based on Little's Law (L = λW), if the arrival rate (λ) remains constant and the average time spent (W) increases, the average number of tasks in the system (L) must also increase."
    }


        
        
    ]
}
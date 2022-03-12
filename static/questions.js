let questions = [
    {
        numb: 1,
        question: "Which of the following is a new Form element got introduced in HTML5?",
        answer: "<keygen>",
        options: [
            "&lt;keygen&gt;",
            "&lt;option&gt;",
            "&lt;legend&gt;",
            "&lt;label&gt;",
        ]
    },
    {
        numb: 2,
        question: "What is the use of webkit in CSS3?",
        answer: "webkit is used to render html and css in browsers like safari and chrome",
        options: [
            "It is a framework of CSS",
            "It is used to give a box-like appearance on the web page",
            "webkit is used to render html and css in browsers like safari and chrome",
            "Webkit is a closed source web browser engine",
        ]
    },
    {
        numb: 3,
        question: "What is the mechanism to detect operating system on the client machine in JavaScript?",
        answer: "navigator.appversion",
        options: [
            "navigate.appversion",
            "navigator.appversion",
            "appversion.navigate",
            "appversion(navigate)",
        ]
    },
    {
        numb: 4,
        question: " Variable name in PHP starts with",
        answer: "$ (Dollar)",
        options: [
            "! (Exclamation)",
            "$ (Dollar)",
            "& (Ampersand)",
            "# (Hash)",
        ]
    },
    {
        numb: 5,
        question: "What is the difference between RAS and VPN server?",
        answer: "VPN is a local connection spread over a large area, RAS is a local connection between 2 connections.",
        options: [
            "RAS is a truly local area connectionand VPN is wide are connection",
            "RAS is a wide area connection and VPN is a local area connection",
            "RAS is less secured than VPN",
            "VPN is a local connection spread over a large area, RAS is a local connection between 2 connections.",
        ]
    },
    {
        numb: 6,
        question: "Main difference between Gateway and router is...",
        answer: "Gateway works on different network architecture router works on same network architecture",
        options: [
            "Gateway works on different network architecture router works on same network architecture",
            "Gateway works on same network architecture while router works on different network architecture",
            "Gateway supports dynamic routing while router doesn't",
            "Gateway works upto 3 OSI layers while router works upto 5 OSI layers",
        ]
    },
    {
        numb: 7,
        question: "Which of the following is not a form of memory?",
        answer: "instruction opcode",
        options: [
            "Instruction cache",
            "Instruction registers",
            "translation look-a-side buffer",
            "instruction opcode",
        ]
    },
    {
        numb: 8,
        question: "What is POP server?",
        answer: "It is used for sending and receiving the mail",
        options: [
            "POP stands for Pre Office Protocol",
            "It is used to upload and fetch files over a network",
            "It is used for sending and receiving the mail",
            "None of these",
        ]
    },
    {
        numb: 9,
        question: "A circuit which is working as a NAND gate with positive level logic system will work as ______ gate with negative level logic system.",
        answer: "NOR",
        options: [
            "XOR",
            "NOR",
            "AND",
            "OR",
        ]
    },
    {
        numb: 10,
        question: "Which of the following is not a feature of microprocessor?",
        answer: "It can be used on compact system",
        options: [
            "It can be used on compact system",
            "cost of the entire system increases",
            "mainly used in personal computers",
            "It is the heart of computer system",
        ]
    },
    {
        numb: 11,
        question: "What is integrated development environment?	What is integrated development environment?",
        answer: "An IDE is a GUI-based software program. It is designed to help programmers build applications with all the needed programs and libraries.",
        options: [
            "An IDE is a CLI-based software program. It is designed to help programmers build applications with all the needed programs and libraries.",
            "IDE is a part of Java Development Kit",
            "IDE is only useful for developing UI of a softwrare",
            "An IDE is a GUI-based software program. It is designed to help programmers build applications with all the needed programs and libraries.",
        ]
    },
    {
        numb: 12,
        question: "What is the difference between AI, ML?",
        answer: "AI means ability to apply knowledge and ML means gaining knowledge",
        options: [
            "AI gives information to machine while ML uses the information to develop an intelligent system",
            "AI means ability to apply knowledge and ML means gaining knowledge",
            "Main goal of AI is obtaining accuracy",
            "ML works as a smart working computer program",
        ]
    },
    {
        numb: 13,
        question: "What is Deep Learning?",
        answer: "Deep learning is a subset of machine learning and is called deep learning because it makes use of deep neural networks.",
        options: [
            "It enables machine to mimic human behavior",
            "Deep Learning is used to analyze simple problems and find solutions for them",
            "Deep learning is a subset of machine learning and is called deep learning because it makes use of deep neural networks.",
            "None of the these",
        ]
    },
    {
        numb: 14,
        question: "Which of the following is not a difference between compiler and interpreter?",
        answer: "Both compiler and interpreter display error after compilation.",
        options: [
            "Compiled code run faster and interpreted code run slower",
            "Compiler takes entire program as input while interpreter takes single line as input",
            "Compiler display errors after compilation while interpreter display erros line by line",
            "Both compiler and interpreter display error after compilation.",
        ]
    },
    {
        numb: 15,
        question: "What is a byte stream? ",
        answer: "It is used to perform input and output for Unicode having 8 bits",
        options: [
            "It is used to perform input and output for Unicode having 8 bits",
            "It is used to perform input and output for Unicode having 32 bits",
            "It is used to perform input and output for Unicode having 16 bits",
            "It is used to perform input and output for 256 bits",
        ]
    },
    {
        numb: 16,
        question: "Which of the following is not a layer of OSI model?",
        answer: "User Interface layer",
        options: [
            "Physical layer",
            "Data link layer",
            "Transport layer",
            "User Interface layer",
        ]
    },
    {
        numb: 17,
        question: "Difference between process and thread.",
        answer: "Process is a program in execution and thread is a segment of process",
        options: [
            "Process can have only one thread",
            "Process is a program in execution and thread is a segment of process",
            "Thread is a program in execution while process describes the algorithm",
            "Both are same",
        ]
    },
    {
        numb: 18,
        question: "What is cryptography?",
        answer: "Cryptography can transform the information in a format unreadable by human and vice versa",
        options: [
            "Cryptography can only transform the information in human readable format",
            "Cryptography can only convert an information into binary codes and not in human readable format",
            "Cryptography can transform the information in a format unreadable by human and vice versa",
            "Cryptography is a part of artificial intelligence that helps machine to obtain knowledge and perform activities on its own",
        ]
    },
    {
        numb: 19,
        question: "What is extension in database?",
        answer: "Extension is the number of tuples in a database",
        options: [
            "Extension is a constant value that gives the name, structure of table and the constraints laid on it",
            "Extension is time independent",
            "Extension is the number of columns in a table",
            "Extension is the number of tuples in a database",
        ]
    },
    {
        numb: 20,
        question: "What do you mean by flat file database?",
        answer: "It is a database without programs or user access language but provides user interface management",
        options: [
            "It is a database with programs or user access language",
            "It is a database without programs or user access language but provides user interface management",
            "It has crossfile capabilities",
            "It has structures for indexing and recognizing records",
        ]
    },
];

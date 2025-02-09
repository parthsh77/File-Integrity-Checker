# File-Integrity-Checker

Prerequisites

    Python Installation:

        Ensure Python 3.x is installed on your system.

        Download and install Python from the official website: python.org.

    Operating System:

        The script works on both Linux and Windows.

    Text Editor or IDE:

        Use a text editor (e.g., Notepad++, VS Code, Sublime Text) or an IDE (e.g., PyCharm) to write and run the script.

    Basic Python Knowledge:

        Familiarity with Python basics (e.g., running scripts, understanding functions, and file handling) will help you understand and modify the code.

    File to Test:

        Have a file ready (e.g., example.txt) to test the integrity checker.

Steps to Set Up and Use the Project

    Save the Script:

        Copy the provided Python code into a file named file_integrity_checker.py.

    Run the Script:

        Open a terminal or command prompt.

        Navigate to the directory where the script is saved.

        Run the script:
        bash
        Copy

        python file_integrity_checker.py

    Generate a Hash:

        Choose option 1 to generate and save the hash of a file.

        Provide the path to the file (e.g., example.txt).

        The script will save the hash in a .hash file (e.g., example.txt.hash).

    Check File Integrity:

        Choose option 2 to check the integrity of the file.

        Provide the path to the file (e.g., example.txt).

        The script will compare the current hash with the stored hash and notify you if the file has been manipulated.

Example Workflow

    Create a test file:
    bash
    Copy

    echo "This is a test file." > example.txt

    Run the script and generate a hash:
    bash
    Copy

    python file_integrity_checker.py

        Choose option 1 and enter example.txt.

    Verify the file integrity:
    bash
    Copy

    python file_integrity_checker.py

        Choose option 2 and enter example.txt.

        The script will confirm that the file is intact.

    Modify the file and check again:
    bash
    Copy

    echo "This file has been modified." >> example.txt
    python file_integrity_checker.py

        Choose option 2 and enter example.txt.

        The script will warn that the file has been manipulated.

Optional Enhancements

    Automate Hash Generation:

        Modify the script to automatically generate hashes for all files in a directory.

    Real-Time Monitoring:

        Use the watchdog library to monitor files in real-time and alert if any changes are detected.

    GUI:

        Add a graphical user interface using tkinter or PyQt for easier interaction.

    Database Integration:

        Store hashes in a database (e.g., SQLite) for better management of multiple files.

Troubleshooting

    File Not Found:

        Ensure the file path is correct and the file exists.

    Permission Issues:

        Run the script with appropriate permissions to read/write files.

    Python Not Recognized:

        Ensure Python is added to your system's PATH during installation.

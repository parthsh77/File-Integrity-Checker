# File Integrity Checker

The **File Integrity Checker** is a simple and self-contained Python project designed to help you verify the integrity of files using cryptographic hashes. It is beginner-friendly and works on both Linux and Windows systems.

---

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup and Usage](#setup-and-usage)
- [Example Workflow](#example-workflow)
- [Optional Enhancements](#optional-enhancements)
- [Troubleshooting](#troubleshooting)

---

## Prerequisites

Before using the File Integrity Checker, ensure the following:

1. **Python Installation**:
   - Python 3.x must be installed on your system. Download it from the official website: [python.org](https://www.python.org/).

2. **Operating System**:
   - The script is compatible with **Linux** and **Windows**.

3. **Text Editor or IDE**:
   - Use a text editor (e.g., Notepad++, VS Code, Sublime Text) or an IDE (e.g., PyCharm) to write and run the script.

4. **Basic Python Knowledge**:
   - Familiarity with Python basics (e.g., running scripts, functions, and file handling) is recommended.

5. **File to Test**:
   - Prepare a file (e.g., `example.txt`) to test the integrity checker.

---

## Setup and Usage

1. **Save the Script**:
   - Copy the provided Python code into a file named `file_integrity_checker.py`.

2. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory where the script is saved.
   - Run the script:
     ```bash
     python file_integrity_checker.py
     ```

3. **Generate a Hash**:
   - Choose option `1` to generate and save the hash of a file.
   - Provide the path to the file (e.g., `example.txt`).
   - The script will save the hash in a `.hash` file (e.g., `example.txt.hash`).

4. **Check File Integrity**:
   - Choose option `2` to check the integrity of the file.
   - Provide the path to the file (e.g., `example.txt`).
   - The script will compare the current hash with the stored hash and notify you if the file has been manipulated.

---

## Example Workflow

1. Create a test file:
   ```bash
   echo "This is a test file." > example.txt

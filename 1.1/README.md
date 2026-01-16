# Python Practice Project

This is a basic Python project containing simple scripts for learning and demonstration purposes.

## Project Overview

This project contains basic Python scripts that demonstrate fundamental programming concepts:
- Simple output statements
- User input handling
- Basic arithmetic operations

## Files in This Project

### Python Scripts

- **hello.py**: A simple "Hello World" program that prints a greeting message to the console.
- **add.py**: An interactive script that prompts the user to enter two numbers and calculates their sum.

### Configuration Files

- **requirements.txt**: Contains all the Python package dependencies needed for this project, primarily focused on IPython and its dependencies for enhanced interactive development.

### Virtual Environment

- **cf-python-base/**: A Python virtual environment directory containing all installed packages and dependencies isolated from the system Python installation.

## Setup Instructions

### Prerequisites

- Python 3.x installed on your system
- pip (Python package installer)

### Installation

1. **Clone or download this project** to your local machine.

2. **Activate the virtual environment**:

   On Windows (PowerShell):
   ```powershell
   .\cf-python-base\Scripts\Activate.ps1
   ```

   On Windows (Command Prompt):
   ```cmd
   cf-python-base\Scripts\activate.bat
   ```

   On macOS/Linux:
   ```bash
   source cf-python-base/bin/activate
   ```

3. **Install dependencies** (if needed):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running hello.py

```bash
python hello.py
```

**Expected Output:**
```
Hello World!
```

### Running add.py

```bash
python add.py
```

**Example Interaction:**
```
Enter the first number: 5
Enter the second number: 3
The sum is: 8
```

## Dependencies

This project uses the following main packages:

- **ipython** (9.9.0): Enhanced interactive Python shell
- **jedi** (0.19.2): Autocompletion and static analysis library
- **pygments** (2.19.2): Syntax highlighting
- **prompt_toolkit** (3.0.52): Library for building interactive command-line applications

For a complete list of dependencies, see [requirements.txt](requirements.txt).

## Project Structure

```
Task1/
├── hello.py              # Simple Hello World script
├── add.py                # Addition calculator script
├── requirements.txt      # Project dependencies
├── README.md            # This file
└── cf-python-base/      # Virtual environment directory
    ├── Include/
    ├── Lib/
    ├── Scripts/
    └── share/
```

## Learning Objectives

This project demonstrates:

1. **Basic Python syntax**: Using print statements and variables
2. **User input**: Accepting and processing user input with `input()`
3. **Type conversion**: Converting string input to integers with `int()`
4. **Arithmetic operations**: Performing basic mathematical calculations
5. **Virtual environments**: Managing project dependencies in isolation 

## Notes

- Always activate the virtual environment before running the scripts to ensure all dependencies are available.
- The virtual environment (cf-python-base) should not be committed to version control in production projects. It's included here for educational purposes.

## Troubleshooting

### Virtual Environment Activation Issues

If you encounter an error activating the virtual environment on Windows PowerShell:
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Module Not Found Errors

If you receive module import errors, ensure the virtual environment is activated and all dependencies are installed:
```bash
pip install -r requirements.txt
```

## License

This is an educational project created for learning purposes.

## Author

Career Foundry Specialization Project - Task 1

---

*Last updated: January 2026*

## ..........................................................PROJECT 1............................................................................................


# Interactive Personal Data Collector
A simple, interactive Python command-line application that collects basic user information, analyzes data types, tracks internal memory allocation, and calculates an approximate birth year.

📝 Project Overview
This project is an introductory Python script designed to demonstrate how Python handles user input, dynamically assigns data types, and references objects in system memory. It is a practical exercise in understanding fundamental programming concepts.

✨ Key Features
Interactive User Input: Collects different types of data (text, whole numbers, and decimals) directly from the user.

Data Type Inspection: Automatically identifies and prints whether a variable is a string (str), integer (int), or float (float).

Memory Address Tracking: Uses Python's built-in id() function to display the exact system memory address where each piece of data is stored.

Dynamic Calculations: Uses basic arithmetic to calculate the user's approximate birth year based on the current year (2026).

🛠️ Concepts Demonstrated
input() Function: Reading user inputs as strings.

Type Casting: Explicitly converting data types using int() and float().

F-Strings: Clean and readable string formatting to output variables seamlessly.

Object Identity: Understanding how Python assigns unique identity numbers (id) to variables in memory.

🚀 How to Run the Script
Prerequisites
Make sure you have Python 3.x installed on your computer.

Step-by-Step Execution
Open VS Code (or any text editor).

Create a new file named data_collector.py and paste your Python code inside it.

Open your terminal in VS Code (`Ctrl + ``).

Run the script using the following command:

python data_collector.py


---

## 💻 Sample Output Preview

When you run the script, the interaction will look like this:

text
Welcome To the Interactive Personal Data Collector!.......
Enter your name: Nidhesh
Enter your age: 20
Enter your height in meters: 1.75
Enter your favorite number: 7

Thanks you! Here is the information we collected:...... 
................................................................
Name: Nidhesh (Type: <class 'str'>, Memory Address: 1402345678912)
Age: 20 (Type: <class 'int'>, Memory Address: 1402345678944)
Height: 1.75 (Type: <class 'float'>, Memory Address: 1402345678976)
Favorite Number: 7 (Type: <class 'int'>, Memory Address: 1402345678992)

Your birth year is approximately :2006 (based on your age of 20)
................................................................
Thank you for using the Interactive Personal Data Collector! Have a great day!

'''
## .................................................................PROJECT 2...................................................................................



# Interactive Personal Data Collector

A simple, interactive Python command-line application that collects basic user information, analyzes data types, tracks internal memory allocation, and calculates an approximate birth year.

---

## 📝 Project Overview
This project is an introductory Python script designed to demonstrate how Python handles user input, dynamically assigns data types, and references objects in system memory. It serves as a practical exercise in understanding fundamental programming and system concepts.

## ✨ Key Features
* **Interactive User Input:** Collects different types of data (text, whole numbers, and decimals) directly from the user through the terminal.
* **Data Type Inspection:** Automatically identifies and prints whether a variable is a string (`str`), integer (`int`), or float (`float`).
* **Memory Address Tracking:** Uses Python's built-in `id()` function to expose the exact system memory address where each piece of data is referenced.
* **Dynamic Calculations:** Uses basic arithmetic to determine the user's approximate birth year relative to the current calendar year.

## 🛠️ Concepts Demonstrated
* **`input()` Function:** Reading interactive user input cleanly as default strings.
* **Type Casting:** Explicitly changing data representations using `int()` and `float()`.
* **F-Strings:** Applying clean, inline pythonic string formatting to output text and structural values seamlessly.
* **Object Identity:** Inspecting how the Python runtime assigns unique tracking identity metrics (`id`) to variables in physical memory.

---

## 🚀 How to Run the Script

### Prerequisites
Make sure you have **Python 3.x** installed on your computer.

### Step-by-Step Execution
1. Open **VS Code** (or any text editor of your choice).
2. Create a new file named `data_collector.py` and paste the script code inside it.
3. Open your integrated terminal in VS Code (`Ctrl + \``).
4. Run the script using the following command:
   ```bash
   python data_collector.py

 ## .....................................................................PROJECT 3 ................................................................

 Here is the plain text version of the README file that you can easily copy and paste into a README.txt file or directly into your project notes:

## DATA ANALYZER AND TRANSFORMATION PROGRAM
A menu-driven Python CLI application designed to process datasets and perform various operations like statistical summaries, mathematical calculations, sequence generation, sorting, and demonstrating core Python concepts like *args, kwargs, and function docstrings (doc).

# FEATURES & MENU OPTIONS
Input Data: Store a list of integers entered via comma-separated values.

Display Data Summary: View statistics like total count, sum, max, min, and data type using math_op().

Calculate Factorial: Compute the factorial of a number using recursive function fact().

Filter Data by Threshold: Filter elements smaller than a specified threshold using list comprehension in lam().

Sort Data: Sort stored data in Ascending or Descending order using sortt().

Fibonacci Sequence: Generate a Fibonacci sequence up to N terms using febo().

Display Unique Values: Find unique elements in the dataset using unique().

Display Duplicate Values: Identify repeating elements in the dataset using duplicate().

Enter and Display *args Data: Pass flexible positional arguments into displayawrgs().

Enter and Display kwargs Data: Pass key-value dictionary pairs into displaykwrgs().

Exit Program: Exit the application cleanly.

# HOW FUNCTIONS WORK
Docstrings (doc): Every custom function includes a documentation string (""" ... """) describing its purpose, which is automatically printed when the option is run.

Menu Loop: Uses a while True loop to keep the program open until Option 11 is selected.

Interactive Pause: Uses input("\nPress Enter to return to the main menu...") after each operation so output remains clearly visible in the terminal before re-rendering the menu.

HOW TO RUN
Make sure you have Python 3 installed.

Open your terminal in VS Code and run:
python Functinal_treat.py

Follow the on-screen menu prompts to navigate through options.

Interactive Personal Data Collector
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

```text
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

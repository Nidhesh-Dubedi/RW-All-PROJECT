def math_op(n):
    """This function gives basic statistics like total length, sum, max, min, and data type."""
    if not n:
        print("No data available! Please enter data first using Option 1.")
        return
    print("--------------------------------")
    print(f"-- Total length of data is: {len(n)}")
    print(f"-- Sum of all Values in data is: {sum(n)}")
    print(f"Maximum value in the data is: {max(n)}")
    print(f"Minimum value in the data is: {min(n)}")
    print(f"The data type of the given data is: {type(n)}")
    print("--------------------------------")


def average(n):
    """This function calculates the average/mean of the dataset."""
    if not n:
        print("No data available!")
        return
    total = 0
    print("THE LEN OF DATA IS: ", len(n))
    for i in n:
        total += i
    avg = total / len(n)
    print("--------------------------------")
    print(f"The average of data is: {avg}")
    print("--------------------------------")


def duplicate(n):
    """This function finds and displays repeated/duplicate values from the dataset."""
    l = []
    dup = []
    for i in n:
        if i not in l:
            l.append(i)
        elif i not in dup:
            dup.append(i)
    print("--------------------------------")
    print(f"The duplicates are: {dup}")
    print("--------------------------------")


def unique(n):
    """This function extracts and displays all unique values in the dataset."""
    l = []
    for i in n:
        if i not in l:
            l.append(i)
    print("--------------------------------")        
    print(f"The Unique values are: {l}")
    print("--------------------------------")


def displayawrgs(*n):
    """This function accepts positional arguments using *args and displays them."""
    print("--------------------------------") 
    print(f"The data you entered is: {n}")
    print("--------------------------------")


def displaykwrgs(**dic):
    """This function accepts key-value pairs using **kwargs and displays them."""
    for key, value in dic.items():
        print("--------------------------------")
        print(f"The data is {key}: {value}")
        print("--------------------------------")


def fact(n):
    """This function recursively calculates the factorial of a given integer."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


def febo(n):
    """This function generates and displays a Fibonacci sequence up to n terms."""
    seq = []
    a = 0
    b = 1
    while len(seq) < n:
        seq.append(a)
        a, b = b, a + b
    print("--------------------------------")    
    print(seq)
    print("--------------------------------")


def sortt(n, option):
    """This function sorts the dataset in Ascending (1) or Descending (2) order."""
    if option == 1:
        s = sorted(n, reverse=False)
    elif option == 2:
        s = sorted(n, reverse=True)
    else:
        print("Invalid option, choose 1 or 2")
        return None
    print("--------------------------------")
    print(f"The Sorted values according to your choice: {s}")
    print("--------------------------------")


def lam(n, threshold):
    """This function filters the dataset to return items smaller than a threshold value."""
    l = [i for i in n if i < threshold]
    print("--------------------------------")
    print(l)
    print("--------------------------------")


valuee = []

MENU = """
============================================================
Welcome to the Data Analyzer and Transformation Program......
MAIN MENU........
============================================================
Enter your Choice from given Collection:
1. Input Data
2. Display Data Summary (Built-in functions)
3. Calculate Factorial
4. Filter Data by Threshold
5. Sort Data
6. Display Dataset Statistics (Fibonacci Sequence)
7. Display Unique Values
8. Display Duplicate Values
9. Enter and Display *Args Data
10. Enter and Display **Kwargs Data
11. Exit Program
============================================================
"""

while True:
    print(MENU)
    user = int(input("Please Enter Your Choice here: "))
    
    if user == 1:
        data_str = input("Enter numbers separated by commas (e.g., 1, 2, 3, 4, 5 or [1,2,3]): ")
        cleaned_str = data_str.replace("[", "").replace("]", "")
        valuee = [int(i.strip()) for i in cleaned_str.split(",") if i.strip()]
        print("Data is Stored successfully:", valuee)

    elif user == 2:
        print("Docstring:", math_op.__doc__)
        print("Data Summary:...........")
        math_op(valuee)

    elif user == 3:
        print("Docstring:", fact.__doc__)
        data = int(input("Enter the Number to Calculate its Factorial: "))
        result = fact(data)
        print("--------------------------------")
        print(f"The Factorial of {data} is {result}")
        print("--------------------------------")

    elif user == 4:
        print("Docstring:", lam.__doc__)
        data = int(input("Enter a threshold value to filter data greater than this value: "))
        print("Here is your Filtered data:")
        lam(valuee, data)

    elif user == 5:
        print("Docstring:", sortt.__doc__)
        print("Choose the following option from below:")
        print("1. Ascending")
        print("2. Descending")
        option = int(input("Enter your Choice: "))
        sortt(valuee, option)

    elif user == 6:
        print("Docstring:", febo.__doc__)
        num = int(input("Enter the Number to Calculate the Fibonacci: "))
        febo(num)

    elif user == 7:
        print("Docstring:", unique.__doc__)
        print("Here are unique values in the given dataset:")
        unique(valuee)

    elif user == 8:
        print("Docstring:", duplicate.__doc__)
        print("Here are duplicate values in the given dataset:")
        duplicate(valuee)

    elif user == 9:
        print("Docstring:", displayawrgs.__doc__)
        data = input("Enter values separated by commas (e.g. 10,20,30): ")
        args_list = [i.strip() for i in data.split(",")]
        displayawrgs(*args_list)

    elif user == 10:
        print("Docstring:", displaykwrgs.__doc__)
        data = input("Enter key=value pairs separated by commas (e.g. name=Nidhesh, age=23): ")
        dic = {}
        for item in data.split(","):
            if "=" in item:
                k, v = item.split("=")
                dic[k.strip()] = v.strip()
        displaykwrgs(**dic)

    elif user == 11:
        print("Thank you for using Data Analyzer and Transformer Program. Have a Good Day!!")
        break

    else:
        print("Invalid choice, please try again.")
        
    input("\nPress Enter to return to the main menu...")
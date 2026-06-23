print("Welcome To the Interactive Personal Data Collector!.......")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
fav_no = int(input("Enter your favorite number: "))

print("Thanks you! Here is the information we collected:...... ")
print("................................................................")
print(f"Name: {name} (Type: {type(name)},Memory Address: {id(name)})")
print(f"Age: {age} (Type: {type(age)},Memory Address: {id(age)})")
print(f"Height: {height} (Type: {type(height)},Memory Address: {id(height)})")
print(f"Favorite Number: {fav_no} (Type: {type(fav_no)},Memory Address: {id(fav_no)})")

print(f"Your birth year is approximately :{2026-age} (based on your age of {age})")
print("................................................................")
print("Thank you for using the Interactive Personal Data Collector! Have a great day!")
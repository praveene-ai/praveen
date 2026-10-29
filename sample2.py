# 1 file write
with open("students.txt", "w") as file:
    file.write("Praveen\n")
    file.write("Kumar\n")

print("File saved successfully")

# 2 file 
with open("students.txt", "r") as file:
    data = file.read()

print(data)

# 3 marks statement
with open("marks.txt", "w") as file:
    file.write("Maths: 90\n")

with open("marks.txt", "w") as file:
    file.write("Python: 95\n")

# append mode

with open("marks.txt", "a") as file:
    file.write("SQL: 85\n")   

# write() — save one string    
 
with open("riders.txt", "w") as file:
    file.write("Meena\n")
    file.write("Karthik\n") 

# writelines()

names = ["Meena\n", "Karthik\n", "Sneha\n"]

with open("riders.txt", "w") as file:
    file.writelines(names)    

# readlines()
with open("riders.txt", "r") as file:
    lines = file.readlines()

print(lines)


# Create a path
from pathlib import Path

p = Path("data") / "students.txt"

print(p)
print(p.name)
print(p.suffix)
print(p.parent)
print(p.exists())


# Save and read a file using pathlib

from pathlib import Path

p = Path("notes.txt")

p.write_text("Learn Python\nPractice SQL\n")

data = p.read_text()

print(data)


# CSV file
import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["name", "mark"]
    )

    writer.writeheader()

    writer.writerow({"name": "Praveen", "mark": 85})
    writer.writerow({"name": "Kumar", "mark": 90})
    writer.writerow({"name": "Meena", "mark": 95})

# read csv file

import csv

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)


# json 
        
{
  "name": "CabGo",
  "open": True,
  "cities": ["Chennai", "Madurai"]
}        


# save json file 


import json

shop = {
    "name": "CabGo",
    "open": True,
    "cities": ["Chennai", "Madurai"]
}

with open("shop.json", "w") as file:
    json.dump(shop, file, indent=2)

print("JSON file created successfully")


# handle the error with try except

try:
    with open("missing.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found")

print("Program continues")


# part 1: Write names to names.txt

names = ["Arun", "Priya", "Rahul", "Divya", "Karthik"]

with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

# part 2: Read names with line numbers

with open("names.txt", "r") as file:
    for number, line in enumerate(file, start=1):
        print(number, line.strip())

# part 3: create csv file

students = [
    {"name": "Arun", "marks": 75},
    {"name": "Priya", "marks": 55},
    {"name": "Rahul", "marks": 90},
    {"name": "Divya", "marks": 60},
    {"name": "Karthik", "marks": 82}
]

with open("students.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["name", "marks"]
    )

    writer.writeheader()
    writer.writerows(students) 

# part 4: CSV and print marks above 60  

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if int(row["marks"]) > 60:
            print(row["name"], row["marks"])       

# Part 5 : Save the same students to JSON     

with open("students.json", "w") as file:
    json.dump(students, file, indent=2)   




# Part 6: Read students from JSON

with open("students.json", "r") as file:
    data = json.load(file)

for student in data:
    print(student["name"], student["marks"])


# Part 7: — Handle a missing file 

try:
    with open("missing.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Error: File not found")

    import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [1000, 1500, 1200, 2000]

plt.plot(months, sales, label="Monthly Sales")

plt.title("Monthly Sales Report")
plt.xlabel("Month")
plt.ylabel("Sales Amount")

plt.legend()

plt.savefig("sales.png")
plt.show()
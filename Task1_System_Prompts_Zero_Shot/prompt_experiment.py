
import csv

with open("data/results.csv", "r", newline="") as file:
    reader = csv.reader(file)

    rows = list(reader)

print("Prompt Experiment Results")
print()

for row in rows[1:]:
    print("Prompt:", row[0])
    print("Category Accuracy:", row[1], "%")
    print("Priority Accuracy:", row[2], "%")
    print("Complete Accuracy:", row[3], "%")
    print()

names = ["Arun", "Priya", "Rahul", "Divya", "Karthik"]

with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")


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
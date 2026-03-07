import csv
import matplotlib.pyplot as plt

print("------ SMART EXPENSE ANALYZER ------")

total_expense = 0
transaction_count = 0
category_totals = {}

with open("expenses.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        category = row[1]
        amount = int(row[2])

        total_expense += amount

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount


print("\nTotal Expense: ₹", total_expense)

print("\nCategory-wise Spending:")

for category, amount in category_totals.items():
    print(category, "→ ₹", amount)


# Highest spending 
highest_c = max(category_totals, key=category_totals.get)
highest_amount = category_totals[highest_c]

print("\nHighest Spending:", highest_c)
print("Amount: ₹", highest_amount)



labels = category_totals.keys()
values = category_totals.values()

plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("Expense Distribution by Category")

plt.savefig("expense_chart.png")

plt.show()
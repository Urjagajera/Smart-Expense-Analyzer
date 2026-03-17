import csv
import matplotlib.pyplot as plt


def load_data(file_name):
    data = []
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            next(reader)  # skip header

            for row in reader:
                try:
                    data.append({
                        "date": row[0],
                        "category": row[1],
                        "amount": int(row[2]),
                        "description": row[3]
                    })
                except ValueError:
                    continue

    except FileNotFoundError:
        print("❌ File not found. Please check the file name.")
        return []

    return data


def calculate_totals(data):
    total = 0
    category_totals = {}

    for entry in data:
        amount = entry["amount"]
        category = entry["category"]

        total += amount

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    return total, category_totals


def find_highest_category(category_totals):
    highest_category = max(category_totals, key=category_totals.get)
    highest_amount = category_totals[highest_category]
    return highest_category, highest_amount


def calculate_average(total, count):
    return total / count if count > 0 else 0


def generate_chart(category_totals):
    labels = list(category_totals.keys())
    values = list(category_totals.values())

    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title("Expense Distribution by Category")
    plt.savefig("expense_chart.png")
    plt.close()


def save_summary(total, category_totals, highest_category, highest_amount, average):
    with open("summary.txt", "w", encoding="utf-8") as file:
        file.write("------ EXPENSE SUMMARY ------\n\n")
        file.write(f"Total Expense: ₹{total}\n\n")

        file.write("Category-wise Spending:\n")
        for category, amount in category_totals.items():
            file.write(f"{category}: ₹{amount}\n")

        file.write(f"\nHighest Spending Category: {highest_category} (₹{highest_amount})\n")
        file.write(f"Average Expense: ₹{round(average, 2)}\n")


def display_results(total, category_totals, highest_category, highest_amount, average):
    print("\n------ SMART EXPENSE ANALYZER ------\n")
    print(f"Total Expense: ₹{total}\n")

    print("Category-wise Spending:")
    for category, amount in category_totals.items():
        print(f"{category} → ₹{amount}")

    print(f"\nHighest Spending Category: {highest_category} (₹{highest_amount})")
    print(f"Average Expense: ₹{round(average, 2)}")


def main():
    file_name = input("Enter CSV file name (example: expenses.csv): ")

    data = load_data(file_name)

    if not data:
        return

    total, category_totals = calculate_totals(data)
    highest_category, highest_amount = find_highest_category(category_totals)
    average = calculate_average(total, len(data))

    generate_chart(category_totals)
    save_summary(total, category_totals, highest_category, highest_amount, average)
    display_results(total, category_totals, highest_category, highest_amount, average)


if __name__ == "__main__":
    main()
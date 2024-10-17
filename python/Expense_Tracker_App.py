import json
from datetime import datetime

# Initialize a sample data structure for expenses
expenses = []

def add_expense(category, amount, description):
    expense = {
        "category": category,
        "amount": amount,
        "description": description,
        "date": str(datetime.now())
    }
    expenses.append(expense)
    print("Expense added successfully!")

def view_expenses():
    print("\nYour Expenses:")
    for expense in expenses:
        print(f"{expense['date']} - {expense['category']}: {expense['amount']} - {expense['description']}")

def generate_report():
    categories = {}
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        categories[category] = categories.get(category, 0) + amount

    print("\nExpense Report:")
    for category, total in categories.items():
        print(f"{category}: {total}")

# Main application loop
while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Generate Report")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        category = input("Enter category (food, travel, etc.): ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        add_expense(category, amount, description)

    elif choice == '2':
        view_expenses()

    elif choice == '3':
        generate_report()

    elif choice == '4':
        break

    else:
        print("Invalid choice, try again.")

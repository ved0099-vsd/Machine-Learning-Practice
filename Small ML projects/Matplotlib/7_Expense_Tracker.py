
import matplotlib.pyplot as plt

def main():
    categories = ["Food", "Travel", "Shopping", "Bills", "Other"]
    expenses = [2000, 1000, 1500, 2500, 500]

    # Display expenses
    print("Expense Report")
    print("--------------------")

    for i in range(len(categories)):
        print(categories[i], ":", expenses[i])

    print("--------------------")
    print("Total Expenses:", sum(expenses))

    # Create a bar chart
    plt.bar(categories, expenses)
    plt.title("Monthly Expense Tracker")
    plt.xlabel("Categories")
    plt.ylabel("Amount (Rs.)")

    plt.savefig("expense_chart.png")
    plt.show()

if __name__ == "__main__":
    main()
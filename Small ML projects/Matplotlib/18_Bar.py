import matplotlib.pyplot as plt

def main():
    categories = ["Food", "Travel", "Shopping", "Bills", "Other"]
    expenses = [2000, 1000, 1500, 2500, 500]

    plt.pie(expenses, labels=categories, autopct = "%1.1f%%")

    plt.title("Monthly Expenses")

    plt.show()

if __name__ == "__main__":
    main()
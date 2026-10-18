
import matplotlib.pyplot as plt

def main():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    sales = [12000, 15000, 11000, 18000, 22000, 25000]
    expenses = [8000, 9000, 7500, 12000, 14000, 16000]

    # Calculate profit
    profit = []

    for i in range(len(sales)):
        profit.append(sales[i] - expenses[i])

    # 1. Monthly Sales Line Graph
    plt.figure(figsize=(8, 5))
    plt.plot(months, sales, marker="o", label="Sales")
    plt.title("Monthly Sales Analysis")
    plt.xlabel("Month")
    plt.ylabel("Sales (Rs.)")
    plt.grid()
    plt.legend()
    plt.savefig("monthly_sales.png")
    plt.show()

    # 2. Sales vs Expenses Bar Chart
    plt.figure(figsize=(8, 5))
    plt.bar(months, sales, label="Sales")
    plt.bar(months, expenses, label="Expenses")
    plt.title("Sales vs Expenses")
    plt.xlabel("Month")
    plt.ylabel("Amount (Rs.)")
    plt.legend()
    plt.savefig("sales_vs_expenses.png")
    plt.show()

    # 3. Monthly Profit Bar Chart
    plt.figure(figsize=(8, 5))
    plt.bar(months, profit)
    plt.title("Monthly Profit")
    plt.xlabel("Month")
    plt.ylabel("Profit (Rs.)")
    plt.grid(axis="y")
    plt.savefig("monthly_profit.png")
    plt.show()

    # 4. Print Summary
    print("Total Sales:", sum(sales))
    print("Total Expenses:", sum(expenses))
    print("Total Profit:", sum(profit))
    print("Highest Sales:", max(sales))
    print("Lowest Sales:", min(sales))

if __name__ == "__main__":
    main()
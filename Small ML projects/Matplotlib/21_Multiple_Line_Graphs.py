import matplotlib.pyplot as plt

def main():
    Months = ["Jan", "Feb", "Mar", "Apr", "May"]

    Sales_2024 = [10000, 12000, 15000, 13000, 18000]
    Sales_2025 = [12000, 14000, 16000, 17000, 22000]

    plt.plot(Months, Sales_2024, label = "Sales 2024")
    plt.plot(Months, Sales_2025, label = "Sales 2025")

    plt.title("Sales Comparison")
    plt.xlabel("Months")
    plt.ylabel("Sales in Rupees")

    plt.legend() #plt.legend() displays the labels so you can identify each line.
    plt.show()

if __name__ == "__main__":
    main()
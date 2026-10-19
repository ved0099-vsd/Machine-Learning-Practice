import matplotlib.pyplot as plt

def main():
    months = ["Jan", "Feb", "Mar", "Apr", "May"]
    sales = [10000, 15000, 12000, 18000, 22000]

    plt.plot(months,sales)

    plt.title("Monthly sales")
    plt.xlabel("Months")
    plt.ylabel("Sales")

    plt.grid(True)

    plt.show()

if __name__ == "__main__":
    main()
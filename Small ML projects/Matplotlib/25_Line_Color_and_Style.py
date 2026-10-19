import matplotlib.pyplot as plt

def main():
    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    temperature = [30, 32, 29, 34, 33]

    plt.plot(days,temperature, color = "Red", linestyle = "--", marker = "o")

    plt.title("Weekly Temperature")
    plt.xlabel("Days")
    plt.ylabel("Temperature")

    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
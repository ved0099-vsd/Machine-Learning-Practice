import matplotlib.pyplot as plt

def main():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    temperature = [30, 32, 29, 34, 33]

    plt.plot(days, temperature)

    plt.title("Weekly Temperature")
    plt.xlabel("Days")
    plt.ylabel("Temperature")

    plt.show()

if __name__ == "__main__":
    main()

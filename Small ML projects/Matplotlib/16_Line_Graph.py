import matplotlib.pyplot as plt

def main():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday","Sunday"]
    temperature = [30, 32, 29, 34, 33, 35, 32]

    plt.plot(days,temperature)

    plt.title("Weekly Temperature Analysis")
    plt.xlabel("Days")
    plt.ylabel(" 0^c (Temperature)")
    plt.show()




if __name__ == "__main__":
    main()
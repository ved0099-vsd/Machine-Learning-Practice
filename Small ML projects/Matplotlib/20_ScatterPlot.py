import matplotlib.pyplot as plt

def main():
    hours = [1, 2, 3, 4, 5, 6, 7]
    marks = [35, 40, 50, 55, 65, 75, 85]

    plt.scatter(hours, marks)

    plt.title("Study hours vs Exam Marks")
    plt.xlabel("Hours")
    plt.ylabel("Marks")

    plt.show()


if __name__ == "__main__":
    main()
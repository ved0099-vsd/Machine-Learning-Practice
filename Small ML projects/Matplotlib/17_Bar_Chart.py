import matplotlib.pyplot as plt

def main():
    students = ["Amit", "Rahul", "Sneha", "Priya", "Rohan"]
    marks = [75, 60, 90, 85, 70]

    plt.bar(students,marks)

    plt.title("Students marks")
    plt.xlabel("Studnets")
    plt.ylabel("Marks")

    plt.show()

if __name__ == "__main__":
    main()
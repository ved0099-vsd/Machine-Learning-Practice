import matplotlib.pyplot as plt

def main():
    students = ["Amit", "Rahul", "Sneha", "Priya"]
    marks = [75, 60, 90, 85]

    plt.bar(students, marks, color = "Brown")

    for i in range(len(students)):
        plt.text(i, marks[i], str(marks[i]),ha="center")

# i — horizontal position of the bar.
# marks[i] — vertical position, based on the student's marks.
# str(marks[i]) — converts the mark into text so it can be displayed.
# ha="center" — centers the text horizontally.

    plt.title("Student Marks")
    plt.xlabel("Students")
    plt.ylabel("MArks")

    plt.show()

if __name__ == "__main__":
    main()

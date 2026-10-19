import matplotlib.pyplot as plt

def main():
    Subjects = ["Python", "Java", "Maths", "AI", "DBMS"]
    Marks = [85, 70, 90, 80, 75]

    plt.bar(Subjects, Marks, color = "Green")

    plt.title("Subject wise marks")
    plt.xlabel("Subjecyts")
    plt.ylabel("Marks")

    plt.savefig("Students_marks.png")
# plt.savefig("student_marks.png") saves the current graph as an image.
    plt.show()

if __name__ == "__main__":
    main()
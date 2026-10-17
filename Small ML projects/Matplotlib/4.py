
import matplotlib.pyplot as plt

def main():
    students = ["Amit", "Rahul", "Sneha", "Ved", "Anjali"]
    marks = [85, 72, 91, 88, 95]

    # 1. Bar Chart
    plt.figure(figsize=(8, 5))
    plt.bar(students, marks)
    plt.title("Student Marks - Bar Chart")
    plt.xlabel("Students")
    plt.ylabel("Marks")
    plt.grid(axis="y")
    plt.savefig("bar_chart.png")
    plt.show()

    # 2. Line Graph
    plt.figure(figsize=(8, 5))
    plt.plot(students, marks, marker="o")
    plt.title("Student Performance - Line Graph")
    plt.xlabel("Students")
    plt.ylabel("Marks")
    plt.grid()
    plt.savefig("line_graph.png")
    plt.show()

    # 3. Pie Chart
    plt.figure(figsize=(7, 7))
    plt.pie(marks, labels=students, autopct="%1.1f%%")
    plt.title("Student Marks Distribution")
    plt.savefig("pie_chart.png")
    plt.show()

if __name__ == "__main__":
    main()

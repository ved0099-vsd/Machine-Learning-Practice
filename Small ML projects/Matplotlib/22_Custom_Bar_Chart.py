import matplotlib.pyplot as plt

def main():
    Students = ["Amit", "Rahul", "Sneha", "Priya", "Rohan"]
    Marks = [75, 60, 90, 85, 70]

    plt.bar(Students, Marks, color = "Orange") #color="skyblue" changes the bar color.


    for i in range(len(Students)):
        plt.text(i, Marks[i], Marks[i], ha = "center")
#plt.text() places text on the graph.
# marks[i] gets the mark at index i.
# ha="center" centers the text horizontally.

    plt.title("Students MArks")
    plt.xlabel("Students")
    plt.ylabel("Marks")

    plt.show()

if __name__ == "__main__":
    main()
import matplotlib.pyplot as plt

def main():
    students = ["Amit", "Rahul", "Sneha", "Priya"]
    marks = [75, 60, 90, 85]

    colors = ["Red","yellow","green","blue"]
    
    plt.bar(students,marks,color = colors)

    plt.title("Students Marks")
    plt.xlabel("Students")
    plt.ylabel("Marks")

    plt.show()





if __name__ == "__main__":
    main()
import matplotlib.pyplot as plt

def main():

    marks = [45, 55, 60, 62, 65, 70, 72, 75, 80, 85, 90, 95]

    plt.hist(marks, bins = 5)

    plt.title("Students Marks Distribution")
    plt.xlabel("Marks")
    plt.ylabel("No. of students")

    plt.show()
    

if __name__ == "__main__":
    main()
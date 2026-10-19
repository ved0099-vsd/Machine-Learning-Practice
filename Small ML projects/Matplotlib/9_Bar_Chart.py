import matplotlib.pyplot as plt

def main():
    Students = ["Ved","Aayush","Soumi","Adit","Raj"]
    Marks = [89,98,87,76,56]

    plt.bar(Students,Marks)
    plt.title("Students Marks")
    plt.xlabel("Students")
    plt.ylabel("Marks")
    plt.grid(axis="y") #adds horizontal grid lines.
    plt.show()

if __name__ == "__main__":
    main()
import matplotlib.pyplot as plt

def main():
    Students = ["Ved","Soumi","Adi","Neha","Raj","Aayush"]
    Marks = [99,67,69,99,89,89]

    plt.bar(Students, Marks)

    plt.title("Student Marks")
    plt.xlabel("Students")
    plt.ylabel("Marks")

    plt.show()

if __name__ == "__main__":
    main()
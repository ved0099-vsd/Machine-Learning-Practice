import matplotlib.pyplot as plt

def main():

    Students = ["Ved","Adi","Soumi","Raj","Aayush"]
    Marks = [89,99,69,67,78]

    plt.plot(Students,Marks,marker="o")
    plt.title("My first graph")
    plt.xlabel("Students")
    plt.ylabel("Marks")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()

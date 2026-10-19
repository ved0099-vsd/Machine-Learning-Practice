import matplotlib.pyplot as plt

def main():
    Marks = [87,65,90,87,85,67,78,71,64]

    plt.hist(Marks, bins=7, edgecolor = "Red")
    # bins= divides the data into five intervals
    # edgecolor="black" outlines the bars.
    
    plt.title("Marks Distribution")
    plt.xlabel("Marks")
    plt.ylabel("Number of students")
    plt.show()

if __name__ == "__main__":
    main()
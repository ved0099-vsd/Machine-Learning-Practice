import matplotlib.pyplot as plt

def main():
    x = [1, 2, 3, 4, 5]
    y = [10, 20, 15, 25, 30]

    plt.plot(x,y)           #Creates a line graph

    plt.title("My First graph")
    plt.xlabel("X Values")
    plt.ylabel("Y Values")

    plt.show()

if __name__ == "__main__":
    main()
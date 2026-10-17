import matplotlib.pyplot as plt

def main():
    x = [1,2,3,4,5,6]
    y = [5,10,20,15,99,69]

    plt.plot(x,y)

    plt.title("Matplotlib.pyplot")
    plt.xlabel("X Values")
    plt.ylabel("Y Values")

    plt.show()




if __name__ == "__main__":
    main()
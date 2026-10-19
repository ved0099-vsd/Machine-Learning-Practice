import matplotlib.pyplot as plt

def main():
    Categories = ["Food","Travel","Shopping","Bills"]
    Expenses = [2000,1000,2000,800]

    plt.pie(Expenses, labels=Categories, autopct="%1.1f%%")
    #autopct="%1.1f%%" displays each slice's percentage to one decimal place.
    
    plt.title("Expenses Distribution")
    plt.show()

if __name__ == "__main__":
    main()
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def main():
    Data = {
        "Student": ["Ved","Adi","Somi","Raj","Aayush"],
        "Marks" : [87,67,90,56, 63]
    }

    df = pd.DataFrame(Data)

    sns.barplot(data=df, x = "Student", y = "Marks")

    plt.title("Student", y = "Marks")

    plt.title("Student Marks")
    plt.show()

if __name__ == "__main__":
    main()
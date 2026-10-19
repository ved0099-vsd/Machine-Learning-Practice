import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def main():
    Data = {
        "Marks" : [35,40,45,50,55,60,65,70,75,100]
    }

    df = pd.DataFrame(Data)

    sns.boxplot(data=df, y="Marks")
# sns.boxplot() creates a box plot.
# data=df tells Seaborn to use your DataFrame.
# y="Marks" tells it to display the Marks column vertically.

    plt.title("Box plot of student marks")
    plt.show()

if __name__ == "__main__":
    main()
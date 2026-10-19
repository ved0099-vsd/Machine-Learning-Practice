import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def main():
    Data = {
        "Hours" : [1,2,3,4,5],
        "Marks" : [35,45,55,75,85]
    }

    df = pd.DataFrame(Data)

    sns.scatterplot(data=df, x="Hours", y="Marks")

    plt.title("Show Hours vs Marks")
    plt.show()

if __name__ == "__main__":
    main()
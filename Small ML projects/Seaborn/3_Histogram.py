import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def main():
    Data = {
        "Marks" : [35,45,55,60,65,70,75,80,85,90]
    }

    df = pd.DataFrame(Data)

    sns.histplot(data=df, x="Marks")

    plt.title("Distribution of marks")
    plt.show()

if __name__ == "__main__":
    main()
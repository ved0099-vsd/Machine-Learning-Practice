import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def main():
    Data = {
        "Hours": [1,2,3,4,5],
        "Marks" : [35,45,55,65,85],
        "Attendance" : [50,60,70,80,90]
    }

    df = pd.DataFrame(Data)

    sns.pairplot(df)

    sns.pairplot(df)

    plt.show()

if __name__ == "__main__":
    main()

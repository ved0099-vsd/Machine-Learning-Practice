import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def main():
    Data = {
        "Hours" : [1,2,3,4,5],
        "Marks" : [35,45,55,5,85],
        "Attendance" : [50,60,70,80,90]        
    }

    df = pd.DataFrame(Data)

    correlation = df.corr()
# .corr() calculates the correlation between numerical columns.

    sns.heatmap(correlation, annot=True)
# correlation provides the calculated values.
# annot=True displays the numerical values inside the coloured cells.

    plt.title("Correlation Heatmap")
    plt.show()

if __name__ == "__main__":
    main()
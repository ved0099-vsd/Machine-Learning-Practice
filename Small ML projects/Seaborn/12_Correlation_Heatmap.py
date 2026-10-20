
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def main():
    data = {
        "Hours": [1, 2, 3, 4, 5, 6],
        "Marks": [35, 40, 50, 60, 75, 90],
        "Attendance": [50, 55, 65, 70, 85, 95]
    }

    df = pd.DataFrame(data)

    correlation = df.corr()

    sns.heatmap(correlation, annot=True, cmap="coolwarm", vmin=-1, vmax=1)

    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

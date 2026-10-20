
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def main():
    data = {
        "Hours": [1, 2, 3, 4, 5, 6, 7],
        "Marks": [35, 40, 50, 60, 70, 80, 90]
    }

    df = pd.DataFrame(data)

    sns.scatterplot(data=df, x="Hours", y="Marks", s=100)

    plt.title("Study Hours vs Marks")
    plt.xlabel("Study Hours")
    plt.ylabel("Marks")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

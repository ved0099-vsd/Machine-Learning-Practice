
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def main():
    data = {
        "Marks": [
            35, 40, 45, 50, 55, 60, 60, 65,
            70, 70, 75, 80, 85, 90, 95
        ]
    }

    df = pd.DataFrame(data)

    sns.histplot(data=df, x="Marks", bins=5, color="skyblue", edgecolor="black")

    plt.title("Distribution of Student Marks")
    plt.xlabel("Marks")
    plt.ylabel("Number of Students")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def main():
    data = {
        "Sport" : [
            "Cricket","Football","Cricket",
            "Cricket", "Football","Tennis",
            "Football", "Cricket"
        ]
    }

    df = pd.DataFrame(data)

    sns.countplot(data=df, x = "Sport")

#sns.countplot() creates a count plot.
# data=df tells Seaborn which table to use.
# x="Sport" tells it which column to count.

    plt.title("Number of students per sport")
    plt.show()

if __name__ == "__main__":
    main()
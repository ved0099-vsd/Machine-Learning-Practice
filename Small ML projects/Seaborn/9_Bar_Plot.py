
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def main():
    data = {
        "Student": ["Amit", "Rahul", "Sneha", "Priya", "Rohan"],
        "Marks": [75, 60, 90, 85, 70]
    }

    df = pd.DataFrame(data)

    sns.barplot(data=df, x="Student", y="Marks", hue="Student", palette="Set2", legend=False)

    plt.title("Student Marks")
    plt.xlabel("Students")
    plt.ylabel("Marks")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

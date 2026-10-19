import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def main():
    Data = {
        "Student" : ["Amit","Rahul","Sneha","Priya","Rohan"],
        "Marks" : [75,60,90,85,70]
    }

    df = pd.DataFrame(Data)

    sns.barplot(data=df, x = "Student", y="Marks", hue="Student", palette = "Set2", legend=False)
# A palette is a collection of colours. "Set2" tells Seaborn which colour palette to use.
# hue="Student" assigns colours according to the student category.
# legend=False hides the legend because each student already has a name on the horizontal axis.

    plt.title("Student Marks")
    plt.show()

if __name__ == "__main__":
    main()
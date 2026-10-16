import pandas as pd

def main():
    df = pd.read_csv("Students.csv")

    print("Q1. Display the dataset")
    print(df)

    Border = "-"  *40
    print(Border)

    print("Q2. Filter students")
    print(df[df["Marks"] > 80])

    print(Border)

    print("Q3. Find top students")
    print(df.sort_values(by="Marks", ascending=False).head(3))

    print(Border)

    print("4.Print the average, highest, and lowest marks.")
    print(df["Marks"].max())
    print(df["Marks"].mean())
    print(df["Marks"].min())

    print(Border)

    print("5.Count the number of students from each city.")
    print(df["City"].value_counts())

    print(Border)

    print("6.Save students scoring above 80 to `Top_Students.csv`, without the index.")
    top_students = (df[df["Marks"] > 80])
    top_students.to_csv("Top_Students.csv", index=False)
    print("FIle saved successfully")

    print(Border)

    print("7.Read `Top_Students.csv` back into Pandas and print it.")
    df = pd.read_csv("Top_Students.csv")

    print(df)

if __name__ == "__main__":
    main()
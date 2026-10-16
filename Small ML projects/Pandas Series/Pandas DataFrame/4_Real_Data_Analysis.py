import pandas as pd

def main():
    df = pd.read_csv("Students.csv")
    print(df)

    Border = "-" * 40
    print(Border)

    print("1.Display students who scored more than 80 marks.")
    print(df[df["Marks"] > 80])

    print(Border)

    print("2.Display students who live in Pune.")
    print(df[df["City"] == "Pune"])

    print(Border)

    print("3.Display students who scored more than 80 AND are older than 20.")
    print(df[(df["Marks"] > 80) & (df["Age"] > 20)])
    
    print(Border)

    print("4.Display the top 3 students by Marks, highest first.")
    print(df.sort_values(by="Marks", ascending=False).head(3))

    print(Border)

    print("5.Count how many students are from Pune.")
    print((len(df[df["City"] == "Pune"])))

    print(Border)

    print("6.Find the highest, lowest, and average Marks.")
    print(df["Marks"].max())
    print(df["Marks"].min())
    print(df["Marks"].mean())

    print(Border)

    print("7.Display only Name and City.")
    print(df[["Name", "City"]])

    print(Border)

    print("8.Count how many students belong to each city using value_counts().")
    print(df["City"].value_counts())




if __name__ == "__main__":
    main()
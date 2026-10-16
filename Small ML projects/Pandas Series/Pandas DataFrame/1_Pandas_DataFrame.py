import pandas as pd

def main():
    Data = {
        "Name": ["Ved","Adi","Raj","Soumi","Aayush"],
        "Age" : [22,23,22,23,22],
        "Marks":[89,87,86,85,76],
        "City": ["Pune","Kotraj","Latur","Satara","Mulshi"]
    }

    df = pd.DataFrame(Data)
    print(df)

    Border = "-" * 40
    print(Border)

    print("1.Display first 5 rows")
    print(df.head(5))

    print(Border)

    print("2.Display the number of rows and columns using shape.")
    print(df.shape)

    print(Border)

    print("3.Display all column names using columns.")
    print(df.columns)

    print(Border)

    print("4.Display only the Name column.")
    print(df.Name)

    print(Border)

    print("5.Display the Name and Marks columns.")
    print(df[["Name", "Marks"]])

    print(Border)

    print("6.Display students whose marks are greater than 80.")
    print(df[df["Marks"] > 80])

    print(Border)

    print("7.Display students who live in Pune.")
    print(df[df["City"] == "Pune"])

    print(Border)

    print("8.Sort students by Marks in descending order.")
    print(df.sort_values(by="Marks", ascending=False))

    print(Border)

    print("10.Display the first three rows using iloc.")
    print(df.iloc[0:3])




if __name__ == "__main__":
    main()
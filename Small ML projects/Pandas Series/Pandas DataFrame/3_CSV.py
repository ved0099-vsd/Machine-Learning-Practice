import pandas as pd

def main():
    df = pd.read_csv("Students.csv")
    print(df)

    Border = "-" * 40
    print(Border)

    print("Display the first three rows using head().")
    print(df.head(3))

    print(Border)

    print("2.Display the last two rows using tail().")
    print(df.tail(2))

    print(Border)

    print("3.Display the number of rows and columns using shape.")
    print(df.shape)

    print(Border)

    print("4.Display summary statistics using describe().")
    print(df.describe())

    print(Border)

    print("5.Save the DataFrame to a new CSV file named Students_Output.csv using to_csv(), without saving the index.")
    print(df.to_csv("Students_Output"))

if __name__ == "__main__":
    main()
import pandas as pd

def main():
    sobj = pd.Series([11,32,45,67],index = ["C","C++","Python","Java"])
    print(sobj)

    print(sobj["Python"])


if __name__ == "__main__":
    main()
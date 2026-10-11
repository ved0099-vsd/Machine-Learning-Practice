import pandas as pd

def main():
    Data = [11,12,13,14]
    print(Data)

    sobj = pd.Series(Data)
    print(sobj)
    
if __name__ == "__main__":
    main()
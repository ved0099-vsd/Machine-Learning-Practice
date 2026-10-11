import pandas as po

def main():
    sobj = po.Series([27000,89000,99999,45678],index = ["amit","ved","adi","Somi"])
    print(sobj)
    print(sobj["ved"])

if __name__ == "__main__":
    main()
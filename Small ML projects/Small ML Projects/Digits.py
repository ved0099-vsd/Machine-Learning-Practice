from sklearn import tree
from sklearn.datasets import load_digits

def main():
    Dataset = load_digits()
    print("Digits dataset case Study")

    print("Number of samples are  :",len(Dataset.target))

    print("Independent Variables are :",Dataset.feature_names)
    print("length of Indepoendent Vatiables is : ",len(Dataset.feature_names))

    print("Dependent Variables are  :",Dataset.target_names)
    print("Length of Dependent Variables is :", len(Dataset.target_names))

    print("-" * 50)

    for i in range(10):
        print("ID %d, Features %s, Labels %s" %(i,Dataset.data[i],Dataset.target[i]))

if __name__ == "__main__":
    main()
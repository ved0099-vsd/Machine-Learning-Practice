from sklearn import tree
from sklearn.datasets import load_breast_cancer

def main():

    print("Breast Cancer Case Study")

    Dataset = load_breast_cancer()

    print("Number of samples : ",len(Dataset.target))

    print("Independent Varibales are :",Dataset.feature_names)
    print("length of Independent variables is :",len(Dataset.feature_names))

    print("Dependent Variables are : ",Dataset.target_names)
    print("Lenght of Dependent variables is : ",len(Dataset.target_names))

    print("-" * 40)

    for i in range(5):
        print("ID %d, features %s, Label %s" %(i,Dataset.data[i],Dataset.target[i]))

if __name__ == "__main__":
    main()
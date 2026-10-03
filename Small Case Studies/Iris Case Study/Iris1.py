from sklearn.datasets import load_iris #built-in Function

def main():
    print("-" * 40)
    print("Iris Classification Case Study")
    print("-" * 40)

    Dataset = load_iris()

    #MetaData of the Dataset
    print("Independent Variables are :")
    print(Dataset.feature_names)

    print("Dependent variables are : ")
    print(Dataset.target_names)

if __name__ == "__main__":
    main()
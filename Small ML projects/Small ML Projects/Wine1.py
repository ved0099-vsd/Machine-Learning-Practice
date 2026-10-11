#Question 1 — Wine Dataset 🍷

#Use the load_wine() dataset.

#Write a program that prints:

#Number of samples
#Feature names
#Number of features
#Target names
#Number of classes
#First 5 records with:
#ID
#Features
#Label

from sklearn import tree
from sklearn.datasets import load_wine

def main():
    
    print("Wine classification case study")
    
    Dataset = load_wine()

    print("Number of samples = ",len(Dataset.target))

    print("Independent Variables are :",Dataset.feature_names)
    print("Length of InDependent Variables are :",len(Dataset.feature_names))

    print("Dependent variables are : ",Dataset.target_names)
    print("Lenght of Dependent variables are : ",len(Dataset.target_names))

    print("-" * 50)

    for i in range(5):
        print("ID %d, features %s, Label %s" %(i,Dataset.data[i], Dataset.target[i]))

if __name__ == "__main__":
    main()

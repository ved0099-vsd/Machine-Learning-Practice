#Given the pixel information of a handwritten image, predict which digit it represents.

from sklearn.datasets import load_digits

def main():
    print("-" * 40)
    print("Digits Classification Case Study")
    print("-" * 40)

    Dataset = load_digits()

    print("Number of samples :", len(Dataset.target)) #No. of samples = 1797

#    Target names are :
#    [0 1 2 3 4 5 6 7 8 9]
    print("Target names are :")
    print(Dataset.target_names)

    print("Shape of data : ", Dataset.data.shape) #Dataset.data = 8 × 8 pixels =64

    print("-" * 50)

    for i in range(len(Dataset.target)):
        print("ID %d, features %s, Label %s" % (i, Dataset.data[i], Dataset.target[i]))

if __name__ == "__main__":
    main()
from sklearn.datasets import load_iris

def main():
    print("-" * 40)
    print("Iris Classification case study")
    print("-" * 40)

    Dataset = load_iris()

    for i in range(len(Dataset.target)):
        print("ID %d, features %s, label %s" % (i,Dataset.data[i], Dataset.target[i]))
# %d → integer → i
# %s → features → Dataset.data[i]
# %s → label → Dataset.target[i]

if __name__ == "__main__":
    main()
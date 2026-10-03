from sklearn import tree

def main():
    print("Loan Approval Case Study")

    Independent = [
    [4,15],
    [4,18],
    [6,20],
    [6,25],
    [8,35],
    [8,40],
    [12,60],
    [12,70]
]
    Dependent = [1,1,1,1,2,2,2,2]

    Model = tree.DecisionTreeClassifier()
    Model = Model.fit(Independent,Dependent)

    result = Model.predict([[6,22],[12,65]])
    print("Result is :",result)

if __name__ == "__main__":
    main()
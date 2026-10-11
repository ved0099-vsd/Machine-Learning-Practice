from sklearn import tree

def main():
    print("Loan Approval Case Study")

    Independent = [
    [25000,550],
    [30000,580],
    [40000,650],
    [50000,700],
    [60000,750],
    [70000,800],
    [35000,620],
    [80000,820]
]

    Dependent = [0,0,1,1,1,1,1,1]

    model = tree.DecisionTreeClassifier()
    model = model.fit(Independent,Dependent)

    Result = model.predict([[45000,680],[25000,540]])
    print("Result : ",Result)

if __name__ == "__main__":
    main()
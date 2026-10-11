from sklearn import tree

def main():
    print("Student Result Classification")

    Independent = [
    [2,60],
    [3,65],
    [4,70],
    [5,75],
    [6,80],
    [7,85],
    [8,90],
    [1,50]
]
    Dependent = [0,0,1,1,1,1,1,0]

    model = tree.DecisionTreeClassifier() #DTC
    model = model.fit(Independent,Dependent) #fit

    Result = model.predict([[6,80],[2,55]])
    print("Result is :",Result)

if __name__ == "__main__":
    main()
from sklearn import tree

def main():
    print("Car Classification Case Study")

    Independent = [
    [1000,6],
    [1200,7],
    [1000,5],
    [1500,10],
    [1600,12],
    [2000,18],
    [2200,20],
    [1200,8]
]
    Dependent = [1,1,1,2,2,2,2,1]

    model = tree.DecisionTreeClassifier()
    model = model.fit(Independent,Dependent)

    Result = model.predict([[1100,7],[2000,19]])
    print("Result is : ",Result)

if __name__ == "__main__":
    main()
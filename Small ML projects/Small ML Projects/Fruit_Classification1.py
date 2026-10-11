from sklearn import tree

def main():
    print("Fruit Classification Case Study")

    Independent = [[150,1],[160,1],[170,1],[180,0],[190,0],[200,0],[155,1],[185,0]]
    Dependent = [1,1,1,2,2,2,1,2]

    Model = tree.DecisionTreeClassifier() #DTC
    Model = Model.fit(Independent,Dependent) #FIT

    Result = Model.predict([[164,1],[189,0]]) #Predict
    print("Result is :",Result)


if __name__ == "__main__":
    main()
    

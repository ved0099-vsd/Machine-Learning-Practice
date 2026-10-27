from sklearn.linear_model import LogisticRegression

def main():
    # = Features: Study Hours
    X = [[1],[2],[3],[4],[5],[6],[7],[8]]

    # 0 - fail, 1 - pass
    y = [0,0,0,0,1,1,1,1]

    # Create the model
    model = LogisticRegression()

    # train the model
    model.fit(X,y)

    #Predict for new students
    new_students = [[2],[5],[8]]

    prediction = model.predict(new_students)

    print("Predictions results are:", prediction) 




if __name__ == "__main__":
    main()
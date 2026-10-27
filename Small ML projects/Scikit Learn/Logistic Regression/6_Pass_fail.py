from sklearn.linear_model import LogisticRegression

def main():
    # Feature: Python Practice Hours
    X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]

    # 0 = Fail, 1 = Pass
    y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

    model = LogisticRegression()

    model.fit(X,y)

    new_students = [[2], [5], [8]]

    prediction = model.predict(new_students)

    print("Prediction results are :")
    print(prediction)

if __name__ == "__main__":
    main()
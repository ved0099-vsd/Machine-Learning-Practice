
from sklearn.linear_model import LogisticRegression

def main():
    # Features: [Study Hours, Assignments Completed]
    X = [
        [1, 1],
        [2, 1],
        [3, 2],
        [4, 3],
        [5, 4],
        [6, 5],
        [7, 6],
        [8, 7]
    ]

    # 0 = Fail, 1 = Pass
    y = [0, 0, 0, 0, 1, 1, 1, 1]

    # Create the model
    model = LogisticRegression()

    # Train the model
    model.fit(X, y)

    # Predict for new students
    new_students = [[2, 1], [5, 4], [8, 7]]
    prediction = model.predict(new_students)

    print("Student Data:", new_students)
    print("Predicted Results:", prediction)

if __name__ == "__main__":
    main()

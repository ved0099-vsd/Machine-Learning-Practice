from sklearn.svm import SVC

def main():

    # Feature: Years of Experience
    X = [[1], [2], [3], [4], [7], [8], [9], [10]]

    # 0 = Low Salary, 1 = High Salary
    y = [0, 0, 0, 0, 1, 1, 1, 1]

    # Create SVM model
    model = SVC(kernel="linear")

    # Train model
    model.fit(X, y)

    # Predict new employees
    new_employees = [[2], [6], [9]]

    prediction = model.predict(new_employees)

    print("Experience:", new_employees)
    print("Salary Category:", prediction)

if __name__ == "__main__":
    main()
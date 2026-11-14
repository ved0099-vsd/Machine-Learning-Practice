# SVM - Loan Approval Prediction

from sklearn.svm import SVC

def main():

    # Features: Annual Income (in lakhs), Credit Score
    X = [
        [2, 450],
        [3, 480],
        [4, 500],
        [5, 520],
        [7, 650],
        [8, 680],
        [10, 720],
        [12, 780],
        [15, 800],
        [18, 850]
    ]

    # 0 = Rejected, 1 = Approved
    y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

    # Create SVM model
    model = SVC(kernel="linear")

    # Train model
    model.fit(X, y)

    # New loan applications
    new_applicants = [
        [3, 470],
        [6, 600],
        [12, 750]
    ]

    # Make predictions
    prediction = model.predict(new_applicants)

    print("Loan Applications:", new_applicants)
    print("Loan Predictions:", prediction)

    for i in range(len(prediction)):
        if prediction[i] == 1:
            print("Applicant", i + 1, ": Loan Approved")
        else:
            print("Applicant", i + 1, ": Loan Rejected")


if __name__ == "__main__":
    main()
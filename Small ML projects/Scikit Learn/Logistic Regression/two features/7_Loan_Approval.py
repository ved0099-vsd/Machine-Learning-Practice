from sklearn.linear_model import LogisticRegression

def main():
    # Features: [Credit Score, Monthly Income in Thousands]
    X = [
        [300, 15], [350, 18], [400, 20], [450, 25],
        [500, 30], [600, 40], [700, 50], [750, 60]
    ]

    # 0 = Rejected, 1 = Approved
    y = [0, 0, 0, 0, 1, 1, 1, 1]

    model = LogisticRegression()

    model.fit(X,y)

    new_applicants =     new_applicants = [[380, 20], [550, 35], [720, 55]]

    pred = model.predict(new_applicants)

    print("New applicants :",new_applicants)

    print("Predicted Reults :",pred)

if __name__ == "__main__":
    main()
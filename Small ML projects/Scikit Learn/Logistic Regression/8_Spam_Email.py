from sklearn.linear_model import LogisticRegression

def main():
    # Feature: Number of Suspicious Words
    X = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]

    # 0 = Not Spam, 1 = Spam
    y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

    model = LogisticRegression()

    model.fit(X,y)

    new_emails = [[1], [5], [8]]

    prediction = model.predict(new_emails)

    print("Predicted Spam Emails Results are :",prediction)

if __name__ == "__main__":
    main()
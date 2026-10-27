from sklearn.linear_model import LogisticRegression

def main():
    # Features: [Number of Links, Suspicious Words]
    X = [
        [0, 0], [0, 1], [1, 0], [1, 1],
        [2, 3], [3, 4], [4, 5], [5, 6]
    ]

    # 0 = Not Spam, 1 = Spam
    y = [0, 0, 0, 0, 1, 1, 1, 1]

    model = LogisticRegression()

    model.fit(X,y)

    new_emails = [[0, 2], [2, 4], [5, 5]]

    pred = model.predict(new_emails)

    print("new emails are :", new_emails)
    print("Predicted results : ", pred)
    
if __name__ == "__main__":
    main()
#Naive Bayes is a Machine Learning algorithm used for classification. It predicts which category something belongs to by calculating probabilities.

from sklearn.naive_bayes import GaussianNB

def main():
    # Feature: Number of suspicious words
    X = [[0], [1], [2], [3], [4], [5], [6], [7]]

    # 0 = Not Spam, 1 = Spam
    y = [0, 0, 0, 0, 1, 1, 1, 1]

    # Create the model
    model = GaussianNB()

    # Train the model
    model.fit(X, y)

    # Predict for new emails
    new_emails = [[1], [4], [7]]
    prediction = model.predict(new_emails)

    print("Email Data:", new_emails)
    print("Spam Predictions:", prediction)

if __name__ == "__main__":
    main()
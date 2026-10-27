from sklearn.linear_model import LogisticRegression

def main():
    # Feature: Credit Score
    X = [[300], [350], [400], [450], [500],
         [550], [600], [650], [700], [750]]

    # 0 = Rejected, 1 = Approved
    y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

    model = LogisticRegression()

    model.fit(X,y)

    new_applicants = [[420], [580], [720]]

    pred = model.predict(new_applicants)

    print("Predicted Results are :",pred)

if __name__ == "__main__":
    main()
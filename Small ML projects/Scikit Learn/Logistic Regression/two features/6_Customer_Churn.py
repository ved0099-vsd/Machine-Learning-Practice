from sklearn.linear_model import LogisticRegression

def main():
    # Features: [Monthly Bill, Complaints]
    X = [
        [200, 0], [250, 1], [300, 1], [350, 2],
        [400, 3], [450, 4], [500, 5], [550, 6]
    ]

    # 0 = Stays, 1 = Leaves
    y = [0, 0, 0, 0, 1, 1, 1, 1]

    model = LogisticRegression()

    model.fit(X,y)

    new_customer = [[230, 0], [380, 3], [520, 6]]

    pred = model.predict(new_customer)

    print("new Data: ",new_customer)
    print("Predicted results :",pred)

if __name__ == "__main__":
    main()
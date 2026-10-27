from sklearn.linear_model import LogisticRegression

def main():
        # Features: [Years of Experience, Performance Score]
    X = [
        [1, 40], [2, 45], [3, 50], [4, 55],
        [5, 65], [6, 70], [7, 80], [8, 90]
    ]

    # 0 = Not Promoted, 1 = Promoted
    y = [0, 0, 0, 0, 1, 1, 1, 1]


    model = LogisticRegression()

    model.fit(X,y)

    new_employees = [[2, 48], [5, 62], [8, 88]]

    pred = model.predict(new_employees)

    print("new data : ", new_employees)

    print("Predicted data :", pred)

if __name__ == "__main__":
    main()


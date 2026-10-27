from sklearn.linear_model import LogisticRegression

def main():
    # Feature: Monthly Income (in thousands)
    X = [[10], [15], [20], [25], [30],
         [35], [40], [45], [50], [55]]

    # 0 = Not Purchased, 1 = Purchased
    y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

    model = LogisticRegression()

    model.fit(X,y)

    new_customers = [[18], [33], [48]]

    prediction = model.predict(new_customers)

    print("Predicted results are : ")
    print(prediction)

if __name__ == "__main__":
    main()
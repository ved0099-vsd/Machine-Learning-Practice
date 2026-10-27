from sklearn.linear_model import LogisticRegression

def main():
    # Feature: Machine Temperature in Celsius
    X = [[30], [35], [40], [45], [50],
         [55], [60], [65], [70], [75]]

    # 0 = Normal, 1 = Fault
    y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

    model = LogisticRegression()

    model.fit(X,y)

    new_temp = [[38], [53], [68]]

    prediction = model.predict(new_temp)

    print("Predicted Results are : ",prediction)

if __name__ == "__main__":
    main()
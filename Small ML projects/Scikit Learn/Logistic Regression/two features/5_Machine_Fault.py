from sklearn.linear_model import LogisticRegression

def main():
    # Features: [Temperature, Vibration Level]
    X = [
        [30, 1], [35, 2], [40, 2], [45, 3],
        [50, 5], [55, 6], [60, 7], [65, 8]
    ]

    # 0 = Normal, 1 = Fault
    y = [0, 0, 0, 0, 1, 1, 1, 1]

    model = LogisticRegression()

    model.fit(X,y)

    new_machines = [[38, 2], [48, 4], [62, 7]]

    pred = model.predict(new_machines)

    print("new data :",new_machines)

    print("Predicted Results : ", pred)
    
if __name__ == "__main__":
    main()
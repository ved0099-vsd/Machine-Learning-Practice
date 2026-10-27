from sklearn.linear_model import LogisticRegression

def main():
    # Features: [Exam Score, Attendance]
    X = [
        [35, 50], [40, 55], [45, 60], [48, 65],
        [55, 70], [65, 75], [75, 85], [90, 95]
    ]

    # 0 = No Scholarship, 1 = Scholarship
    y = [0, 0, 0, 0, 1, 1, 1, 1]

    model = LogisticRegression()

    model.fit(X,y)

    new_Students = [[42, 58], [60, 72], [85, 90]]

    pred = model.predict(new_Students)

    print("new students data: ",new_Students )

    print("predicted Results: ", pred)
    
if __name__ == "__main__":
    main()
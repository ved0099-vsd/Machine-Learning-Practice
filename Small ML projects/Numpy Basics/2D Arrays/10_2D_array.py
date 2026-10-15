
import numpy as np

def main():
    Marks = np.array([
        [72, 86, 94],
        [63, 79, 58],
        [95, 67, 83],
        [54, 89, 76]
    ])

    # Q1. Display the mark 79
    print("Q1. Display the mark 79:")
    print(Marks[1, 1])

    # Q2. Display the last two columns of all students
    print("\nQ2. Last two columns:")
    print(Marks[:, 1:3])

    # Q3. Calculate total marks of each student
    print("\nQ3. Total marks of each student:")
    print(np.sum(Marks, axis=1))

    # Q4. Calculate average marks in each subject
    print("\nQ4. Average marks in each subject:")
    print(np.mean(Marks, axis=0))

    # Q5. Display all marks greater than 80
    print("\nQ5. Marks greater than 80:")
    print(Marks[Marks > 80])

    # Q6. Count marks below 70
    print("\nQ6. Number of marks below 70:")
    print(np.sum(Marks < 70))

    # Q7. Sort the second student's marks in descending order
    print("\nQ7. Second student's marks in descending order:")
    print(np.sort(Marks[1])[::-1])

    # Q8. Find minimum and maximum marks
    print("\nQ8. Minimum mark:")
    print(np.min(Marks))

    print("Maximum mark:")
    print(np.max(Marks))

    # Q9. Display shape, size, and number of dimensions
    print("\nQ9. Shape:")
    print(Marks.shape)

    print("Size:")
    print(Marks.size)

    print("Number of dimensions:")
    print(Marks.ndim)

    # Q10. Reshape into 2 rows and 6 columns
    print("\nQ10. Reshaped array (2 rows, 6 columns):")
    print(Marks.reshape(2, 6))


if __name__ == "__main__":
    main()

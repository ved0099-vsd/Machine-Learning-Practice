months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12000, 15000, 11000, 18000, 22000, 25000]
expenses = [8000, 9000, 7500, 12000, 14000, 16000]

Profit = []

for i in range(len(sales)):
    Profit.append(sales[i] - expenses[i])

#len(sales) counts the sales values. There are 6.
#range(6) gives indexes 0, 1, 2, 3, 4, 5.
#sales[i] - expenses[i] calculates the profit for each month.
#profit.append() adds each calculated profit to the profit list.


print(Profit)
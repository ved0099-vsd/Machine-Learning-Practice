Sales = [12000,15000,11000,18000,22000,25000]
Expenses = [8000,9000,7500,12000,14000,16000]

Profit = []

for i in range(len(Sales)):   #Generates the indexes of the sales list
    Profit.append(Sales[i] - Expenses[i])
#   sales[i] : Gets the sales value at index i
#   expenses[i]: Gets the expense value at index i

print("Total Sales :", sum(Sales))
print("Total Expenses :", sum(Expenses))
print("Total Profit: ",sum(Profit))
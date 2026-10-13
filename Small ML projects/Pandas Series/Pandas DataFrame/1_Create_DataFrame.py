import pandas as pd

Data = {
    "Name":["Ved","Soumya","Adi"], #Dict
    "Age":[22,23,22],
    "Marks":[99,89,69]
}

df = pd.DataFrame(Data)

print(df)
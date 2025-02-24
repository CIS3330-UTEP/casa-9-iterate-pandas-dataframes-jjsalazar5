import pandas as pd
df = pd.read_csv("big-mac-full-index.csv")

#method 4
print("\nInteracting using interrows():")
for index, row in df.iterrows():  
    print(f"Index: {index}: {row.to_dict()}")


#method 6
print("\nIterating using apply():")
def process_row(row):
    print(f"Processed row: {row.to_dict()}")
df.apply(process_row, axis=1)


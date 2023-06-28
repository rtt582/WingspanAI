import pandas as pd

# grab data as dataframe
df = pd.read_excel(r"data\wingspan-card-lists-20201118.xlsx", sheet_name="Core")
df.to_json(r"data\\birds.json", orient="index")
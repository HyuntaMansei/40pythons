import pandas
import pandas as pd

df = pd.DataFrame([])

print(df)

df.to_excel('namelist.xlsx', header=False, index=False)
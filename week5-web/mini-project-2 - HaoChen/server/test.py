import pandas as pd

df = pd.read_json("client_rate.json")
df_dict = df.to_dict()
print(df_dict["client1"]['rate'])
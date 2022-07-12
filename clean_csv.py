import pandas as pd

df = pd.read_csv("cakung_links.csv")
print("Current length of csv file: {}".format(len(df)))
df = df.drop_duplicates()
print("Length of csv file after dropping duplicates: {}".format(len(df)))
df.to_csv("kelapa gading_links_0.csv", index=False)

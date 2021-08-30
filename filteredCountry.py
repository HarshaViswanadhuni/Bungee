import pandas as pd
df = pd.read_csv(r"D:\Bungee\internship-test-master\input\main.csv", header=0)
df1 = df[df['COUNTRY'].str.contains("USA")]
df1.to_csv(r"D:\Bungee\internship-test-master\output\filteredCountry.csv" , index=False)

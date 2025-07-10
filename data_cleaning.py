import pandas as pd

data = pd.read_csv(open("data/combined_driver_data.csv",'rb'),delimiter=",")
print(len(data))

data = data[
            (data["QualyTime"].notna()) &
             (data["AvgFPTime"].notna()) &
             (data['GridPos']).notna() &
             (data['FinishPos'].notna())].reset_index(drop=True)

data.loc[data["Team"] == 'Alfa Romeo',"Team"] = "Kick Sauber"
data.loc[data["Team"] == 'AlphaTauri',"Team"] = "Racing Bulls"
data.loc[data["Team"] == 'RB',"Team"] = "Racing Bulls"


print(len(data))
data.to_csv("data/combined_driver_data_cleaned.csv", index=False)



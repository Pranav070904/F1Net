import pandas as pd
import glob

# Step 1: Load all CSVs
file_paths = ["data/Driver_race_data_2022.csv", "data/Driver_race_data_2023.csv", "data/Driver_race_data_2024.csv", "data/Driver_race_data_2025.csv"]
dataframes = [pd.read_csv(path) for path in file_paths]

# Step 2: Combine them
combined_df = pd.concat(dataframes, ignore_index=True)

# Step 3: Save to a new CSV
combined_df.to_csv("data/combined_driver_data.csv", index=False)

print("✅ Combined dataset saved as 'combined_driver_data.csv'")

import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt


df = pd.read_csv("RESULTS_NSTEVENS_TotalUnitCount=384583_2025-01-16.csv")

# Split the data into chunks of 36 rows and pivot into columns
chunks = [df[i:i+36] for i in range(0, len(df), 36)]
pivot_data = {}

for chunk in chunks:
    df_chunk = pd.DataFrame(chunk, columns=["Prev.Length","Match.Score","Tile.Size","Prev.Type", "Browse.Time"])
    column_name = f"{df_chunk['Tile.Size'].iloc[0]}_{df_chunk['Match.Score'].iloc[0]}_{df_chunk['Prev.Length'].iloc[0]}_{df_chunk['Prev.Type'].iloc[0]}"
    pivot_data[column_name] = df_chunk["Browse.Time"].tolist()

# Create the final pivoted DataFrame
df_pivoted = pd.DataFrame(pivot_data)

print(df_pivoted)

# # Plot
# plt.figure(figsize=(10, 6))
# sns.histplot(df['Browse.Time'], bins=50, kde=True)
# plt.title('Distribution of Browse Times')
# plt.xlabel('Browse Time')
# plt.ylabel('Frequency')
# plt.show()
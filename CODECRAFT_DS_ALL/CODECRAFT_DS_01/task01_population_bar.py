import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the main population data
df = pd.read_csv(r"C:\Users\dell\Desktop\codecraft_internship_tasks\task01_population\API_SP.POP.TOTL_DS2_en_csv_v2_19373.csv", skiprows=4)

# Filter only necessary columns
df_filtered = df[['Country Name', 'Country Code', '2022']]

# Drop rows with NaN values in 2022 column
df_filtered = df_filtered.dropna(subset=['2022'])

# Sort by population in 2022 and take top 10
top_10 = df_filtered.sort_values(by='2022', ascending=False).head(10)

# Plotting
plt.figure(figsize=(10, 6))
sns.barplot(x='2022', y='Country Name', data=top_10, palette='viridis')
plt.title("Top 10 Most Populated Countries (2022)")
plt.xlabel("Population")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

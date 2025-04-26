import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the population data
df = pd.read_csv(r"C:\Users\dell\Desktop\codecraft_internship_tasks\task01_population\API_SP.POP.TOTL_DS2_en_csv_v2_19373.csv", skiprows=4)

# Get population values for 2022 and remove missing ones
pop_2022 = df['2022'].dropna()

# Plot histogram of population distribution
plt.figure(figsize=(10, 6))
sns.histplot(pop_2022, bins=30, kde=True, color='skyblue')
plt.title("Distribution of Population Across Countries (2022)")
plt.xlabel("Population")
plt.ylabel("Number of Countries")
plt.tight_layout()
plt.show()

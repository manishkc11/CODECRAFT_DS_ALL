import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r"C:\Users\dell\Desktop\codecraft_internship_tasks\task5_dataset\RTA Dataset.csv")

# Clean up column names
df.columns = df.columns.str.strip()

# Extract Hour from Time column
df['Hour'] = pd.to_datetime(df['Time'], errors='coerce').dt.hour

# Drop rows where Hour is missing
df = df.dropna(subset=['Hour'])
df['Hour'] = df['Hour'].astype(int)

# ----------------------------------
# Plot 1: Number of Accidents by Hour
plt.figure(figsize=(10, 5))
sns.countplot(x='Hour', data=df, palette='Set2')  # Use a stable palette
plt.title('Number of Accidents by Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Accident Count')
plt.tight_layout()
plt.savefig("task05_accidents_by_hour.png")  # Save locally
plt.close()

# ----------------------------------
# Plot 2: Accidents by Weather Conditions
plt.figure(figsize=(10, 5))
sns.countplot(y='Weather_conditions', data=df, order=df['Weather_conditions'].value_counts().index, palette='Blues_r')
plt.title('Accidents by Weather Conditions')
plt.xlabel('Accident Count')
plt.ylabel('Weather Condition')
plt.tight_layout()
plt.savefig("task05_weather_conditions.png")
plt.close()

# ----------------------------------
# Plot 3: Distribution of Accident Severity
plt.figure(figsize=(8, 5))
sns.countplot(x='Accident_severity', data=df, palette='Set1')
plt.title('Distribution of Accident Severity')
plt.xlabel('Accident Severity')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig("task05_accident_severity.png")
plt.close()

# ----------------------------------
# Plot 4: Accidents by Road Surface Condition
plt.figure(figsize=(10, 5))
sns.countplot(y='Road_surface_conditions', data=df, order=df['Road_surface_conditions'].value_counts().index, palette='mako')
plt.title('Accidents by Road Surface Conditions')
plt.xlabel('Accident Count')
plt.ylabel('Road Surface Condition')
plt.tight_layout()
plt.savefig("task05_road_surface_conditions.png")
plt.close()

# ----------------------------------
# Plot 5: Top 10 Causes of Accidents
top_causes = df['Cause_of_accident'].value_counts().nlargest(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_causes.values, y=top_causes.index, palette='viridis')
plt.title('Top 10 Causes of Accidents')
plt.xlabel('Number of Accidents')
plt.ylabel('Cause of Accident')
plt.tight_layout()
plt.savefig("task05_top_causes.png")
plt.close()

print("✅ Task 5 Completed Successfully! All graphs saved.")

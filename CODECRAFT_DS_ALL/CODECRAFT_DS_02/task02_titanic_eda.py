# task02_titanic_eda.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r"C:\Users\dell\Desktop\codecraft_internship_tasks\task02_titanic_eda\train.csv")

# Basic data info
print("Dataset Info:\n")
print(df.info())
print("\nMissing Values:\n")
print(df.isnull().sum())

# Fill missing age values with median
df['Age'] = df['Age'].fillna(df['Age'].median())


# Drop rows with missing Embarked
df.dropna(subset=['Embarked'], inplace=True)

# Visualization 1: Survival Count
sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("task02_survival_count.png")
plt.clf()

# Visualization 2: Survival by Sex
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Survival Count by Gender")
plt.xlabel("Sex")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("task02_survival_by_gender.png")
plt.clf()

# Visualization 3: Age Distribution
sns.histplot(df['Age'], bins=20, kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.tight_layout()
plt.savefig("task02_age_distribution.png")
plt.clf()

# Visualization 4: Survival by Pclass
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title("Survival by Passenger Class")
plt.xlabel("Pclass")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("task02_survival_by_pclass.png")

print("\nEDA completed. Plots saved.")

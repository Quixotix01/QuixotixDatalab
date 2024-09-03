# Marvel vs DC Data Analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '/content/marvel_vs_dc.csv'  # Change the path if needed
df = pd.read_csv(file_path, encoding='ISO-8859-1')
df.head()

# Check for missing values
print(df.isnull().sum())

# Data types
print(df.dtypes)

# Data Cleaning
df.columns = df.columns.str.strip()  # Strip any whitespace from column names
df['Gross Worldwide'] = pd.to_numeric(df['Gross Worldwide'], errors='coerce')
df['Budget'] = pd.to_numeric(df['Budget'], errors='coerce')
df['Release Date'] = pd.to_datetime(df['Release'], errors='coerce')
df['Opening Weekend USA'] = pd.to_numeric(df['Opening Weekend USA'], errors='coerce')
df['Minutes'] = pd.to_numeric(df['Minutes'], errors='coerce')
df.dropna(inplace=True)  # Drop rows with missing values
df.head()

# Convert 'Minutes' column to numeric by stripping out non-numeric characters
df['Minutes'] = df['Minutes'].str.extract('(\d+)').astype(float)

df.head()

# Analysis 1: Average Rating and Metascore Comparison
avg_rating = df.groupby('Company')['Rate'].mean().reset_index()
avg_metascore = df.groupby('Company')['Metascore'].mean().reset_index()
print(avg_rating)
print(avg_metascore)

# Visualization: Average Rating and Metascore
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
color = ['#2B7BBB', '#e23636']
sns.barplot(x='Company', y='Rate', data=avg_rating, palette=color)
plt.title('Average Rating: Marvel vs. DC')

plt.subplot(1, 2, 2)
sns.barplot(x='Company', y='Metascore', data=avg_metascore, palette=color)
plt.title('Average Metascore: Marvel vs. DC')

plt.tight_layout()
plt.show()

# Analysis 2: Top-Grossing Movies
top_grossing_usa = df.nlargest(10, 'Gross USA')[['Original Title', 'Company', 'Gross USA']]
top_grossing_worldwide = df.nlargest(10, 'Gross Worldwide')[['Original Title', 'Company', 'Gross Worldwide']]
print(top_grossing_usa)
print(top_grossing_worldwide)

# Visualization: Top 10 Grossing Movies in USA and Worldwide
plt.figure(figsize=(14, 7))
color = {'Marvel': '#e23636', 'DC': '#2B7BBB'}
sns.barplot(x='Gross USA', y='Original Title', hue='Company', data=top_grossing_usa, palette=color)
plt.title('Top 10 Grossing Movies (USA)')
plt.show()

plt.figure(figsize=(14, 7))
sns.barplot(x='Gross Worldwide', y='Original Title', hue='Company', data=top_grossing_worldwide, palette=color)
plt.title('Top 10 Grossing Movies (Worldwide)')
plt.show()

# Analysis 3: Budget vs Gross Revenue (ROI Analysis)
df['ROI'] = (df['Gross Worldwide'] - df['Budget']) / df['Budget']
budget_vs_roi = df.groupby('Company')['ROI'].mean().reset_index()
print(budget_vs_roi)

# Visualization: Budget vs Gross Worldwide
plt.figure(figsize=(10, 6))
color = {'Marvel': '#e23636', 'DC': '#2B7BBB'}
sns.scatterplot(x='Budget', y='Gross Worldwide', hue='Company', data=df, palette=color)
plt.title('Budget vs Gross Worldwide: Marvel vs. DC')
plt.xscale('log')  # Log scale for better visualization
plt.yscale('log')
plt.show()

# Analysis 4: Trends Over the Years
trends = df.groupby(['Release', 'Company']).agg({
    'Rate': 'mean',
    'Metascore': 'mean',
    'Gross Worldwide': 'sum'
}).reset_index()
trends['Release'] = pd.to_datetime(trends['Release'])
trends['Year'] = trends['Release'].dt.year
print(trends)

# Visualization: Trends Over Time
plt.figure(figsize=(14, 7))
color = {'Marvel': '#e23636', 'DC': '#2B7BBB'}
sns.lineplot(x='Release', y='Rate', hue='Company', data=trends, marker='o', palette=color)
plt.title('Average Rating Over Time')
plt.show()

plt.figure(figsize=(14, 7))
sns.lineplot(x='Release', y='Gross Worldwide', hue='Company', data=trends, marker='o' , palette=color)
plt.title('Gross Worldwide Over Time')
plt.show()

# Analysis 5: Opening Weekend Performance
opening_weekend_performance = df.groupby('Company')['Opening Weekend USA'].mean().reset_index()
print(opening_weekend_performance)

# Visualization: Opening Weekend Performance
plt.figure(figsize=(10, 6))
color = {'Marvel': '#e23636', 'DC': '#2B7BBB'}
sns.barplot(x='Company', y='Opening Weekend USA', data=opening_weekend_performance, palette=color)
plt.title('Average Opening Weekend Performance: Marvel vs. DC')
plt.show()

# Analysis 6: Runtime Comparison
runtime_comparison = df.groupby('Company')['Minutes'].mean().reset_index()
print(runtime_comparison)

# Visualization: Average Runtime
plt.figure(figsize=(10, 6))
color = {'Marvel': '#e23636', 'DC': '#2B7BBB'}
sns.barplot(x='Company', y='Minutes', data=runtime_comparison, palette=color)
plt.title('Average Runtime: Marvel vs. DC')
plt.show()

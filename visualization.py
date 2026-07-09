import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. DATA LOAD
df = pd.read_csv('books_dataset.csv')

# 2. GRAPH 1: PRICE DISTRIBUTION
plt.figure(figsize=(10,6))
sns.histplot(df['Price'], bins=20, kde=True)
plt.title('Book Price Distribution')
plt.xlabel('Price in £')
plt.savefig('price_distribution.png')

# 3. GRAPH 2: RATING COUNT
plt.figure(figsize=(8,5))
sns.countplot(x='Rating', data=df, palette='viridis')
plt.title('Number of Books by Rating')
plt.savefig('rating_count.png')

# 4. GRAPH 3: TOP 10 EXPENSIVE BOOKS
top10 = df.nlargest(10, 'Price')
plt.figure(figsize=(12,6))
sns.barplot(x='Price', y='Title', data=top10)
plt.title('Top 10 Most Expensive Books')
plt.savefig('top10_expensive.png')

print("All graphs saved!")
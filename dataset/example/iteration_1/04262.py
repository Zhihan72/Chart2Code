import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# We are illustrating the popularity and monthly revenue of different genres of books in a fictional bookstore chain named "Bibliophile's Haven" across two of its largest branches: Downtown and Uptown. The data is for the year 2023.

# Define book genres
genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Sci-Fi', 'Romance', 'Biography', 'Fantasy', 'Self-Help', 'Children']

# Popularity Scores (Higher is more popular)
popularity_downtown = [85, 70, 65, 50, 90, 40, 75, 60, 55]
popularity_uptown = [80, 65, 60, 55, 85, 45, 70, 50, 60]

# Monthly Revenue (in $1000s)
monthly_revenue_downtown = [13, 8, 6, 5, 15, 4, 10, 7, 6]
monthly_revenue_uptown = [12, 7, 5, 6, 14, 4, 9, 5, 7]

# Set up the figure
fig, axes = plt.subplots(2, 2, figsize=(18, 12))

# Bar Chart for Popularity (Downtown Branch)
axes[0, 0].bar(genres, popularity_downtown, color='skyblue', edgecolor='grey')
axes[0, 0].set_title('Book Genre Popularity in Downtown Branch', fontsize=14, weight='bold')
axes[0, 0].set_ylabel('Popularity Score', fontsize=12)
axes[0, 0].set_xticklabels(genres, rotation=45, ha='right')
axes[0, 0].grid(axis='y', linestyle='--', alpha=0.7)

# Bar Chart for Popularity (Uptown Branch)
axes[0, 1].bar(genres, popularity_uptown, color='lightgreen', edgecolor='grey')
axes[0, 1].set_title('Book Genre Popularity in Uptown Branch', fontsize=14, weight='bold')
axes[0, 1].set_ylabel('Popularity Score', fontsize=12)
axes[0, 1].set_xticklabels(genres, rotation=45, ha='right')
axes[0, 1].grid(axis='y', linestyle='--', alpha=0.7)

# Bar Chart for Monthly Revenue (Downtown Branch)
axes[1, 0].bar(genres, monthly_revenue_downtown, color='skyblue', edgecolor='grey')
axes[1, 0].set_title('Monthly Revenue by Genre in Downtown Branch', fontsize=14, weight='bold')
axes[1, 0].set_ylabel('Revenue ($1000s)', fontsize=12)
axes[1, 0].set_xticklabels(genres, rotation=45, ha='right')
axes[1, 0].grid(axis='y', linestyle='--', alpha=0.7)

# Bar Chart for Monthly Revenue (Uptown Branch)
axes[1, 1].bar(genres, monthly_revenue_uptown, color='lightgreen', edgecolor='grey')
axes[1, 1].set_title('Monthly Revenue by Genre in Uptown Branch', fontsize=14, weight='bold')
axes[1, 1].set_ylabel('Revenue ($1000s)', fontsize=12)
axes[1, 1].set_xticklabels(genres, rotation=45, ha='right')
axes[1, 1].grid(axis='y', linestyle='--', alpha=0.7)

# Set a global title and adjust layout
plt.suptitle("Popularity and Monthly Revenue of Book Genres in Bibliophile's Haven Branches (2023)", fontsize=16, weight='bold', y=0.98)
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Display the plot
plt.show()
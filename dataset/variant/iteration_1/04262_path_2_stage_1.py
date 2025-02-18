import matplotlib.pyplot as plt

# Define book genres and corresponding data
genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Sci-Fi', 'Romance', 'Biography', 'Fantasy', 'Self-Help', 'Children']

# Popularity Scores and Monthly Revenue
popularity_downtown = [85, 70, 65, 50, 90, 40, 75, 60, 55]
popularity_uptown = [80, 65, 60, 55, 85, 45, 70, 50, 60]
monthly_revenue_downtown = [13, 8, 6, 5, 15, 4, 10, 7, 6]
monthly_revenue_uptown = [12, 7, 5, 6, 14, 4, 9, 5, 7]

# Sorting data for Downtown and Uptown branches
sorted_downtown_indices = sorted(range(len(popularity_downtown)), key=lambda i: popularity_downtown[i])
sorted_uptown_indices = sorted(range(len(popularity_uptown)), key=lambda i: popularity_uptown[i])

sorted_genres_downtown = [genres[i] for i in sorted_downtown_indices]
sorted_popularity_downtown = [popularity_downtown[i] for i in sorted_downtown_indices]
sorted_revenue_downtown = [monthly_revenue_downtown[i] for i in sorted_downtown_indices]

sorted_genres_uptown = [genres[i] for i in sorted_uptown_indices]
sorted_popularity_uptown = [popularity_uptown[i] for i in sorted_uptown_indices]
sorted_revenue_uptown = [monthly_revenue_uptown[i] for i in sorted_uptown_indices]

# Set up the figure
fig, axes = plt.subplots(2, 2, figsize=(18, 12))

# Bar Chart for Popularity (Downtown Branch)
axes[0, 0].bar(sorted_genres_downtown, sorted_popularity_downtown, color='skyblue', edgecolor='grey')
axes[0, 0].set_title('Book Genre Popularity in Downtown Branch', fontsize=14, weight='bold')
axes[0, 0].set_ylabel('Popularity Score', fontsize=12)
axes[0, 0].set_xticklabels(sorted_genres_downtown, rotation=45, ha='right')
axes[0, 0].grid(axis='y', linestyle='--', alpha=0.7)

# Bar Chart for Popularity (Uptown Branch)
axes[0, 1].bar(sorted_genres_uptown, sorted_popularity_uptown, color='lightgreen', edgecolor='grey')
axes[0, 1].set_title('Book Genre Popularity in Uptown Branch', fontsize=14, weight='bold')
axes[0, 1].set_ylabel('Popularity Score', fontsize=12)
axes[0, 1].set_xticklabels(sorted_genres_uptown, rotation=45, ha='right')
axes[0, 1].grid(axis='y', linestyle='--', alpha=0.7)

# Sorting data for Revenue Charts
sorted_revenue_downtown_indices = sorted(range(len(monthly_revenue_downtown)), key=lambda i: monthly_revenue_downtown[i])
sorted_revenue_uptown_indices = sorted(range(len(monthly_revenue_uptown)), key=lambda i: monthly_revenue_uptown[i])

sorted_genres_revenue_downtown = [genres[i] for i in sorted_revenue_downtown_indices]
sorted_genres_revenue_uptown = [genres[i] for i in sorted_revenue_uptown_indices]

# Bar Chart for Monthly Revenue (Downtown Branch)
axes[1, 0].bar(sorted_genres_revenue_downtown, sorted_revenue_downtown, color='skyblue', edgecolor='grey')
axes[1, 0].set_title('Monthly Revenue by Genre in Downtown Branch', fontsize=14, weight='bold')
axes[1, 0].set_ylabel('Revenue ($1000s)', fontsize=12)
axes[1, 0].set_xticklabels(sorted_genres_revenue_downtown, rotation=45, ha='right')
axes[1, 0].grid(axis='y', linestyle='--', alpha=0.7)

# Bar Chart for Monthly Revenue (Uptown Branch)
axes[1, 1].bar(sorted_genres_revenue_uptown, sorted_revenue_uptown, color='lightgreen', edgecolor='grey')
axes[1, 1].set_title('Monthly Revenue by Genre in Uptown Branch', fontsize=14, weight='bold')
axes[1, 1].set_ylabel('Revenue ($1000s)', fontsize=12)
axes[1, 1].set_xticklabels(sorted_genres_revenue_uptown, rotation=45, ha='right')
axes[1, 1].grid(axis='y', linestyle='--', alpha=0.7)

# Set a global title and adjust layout
plt.suptitle("Popularity and Monthly Revenue of Book Genres in Bibliophile's Haven Branches (2023)", fontsize=16, weight='bold', y=0.98)
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Display the plot
plt.show()
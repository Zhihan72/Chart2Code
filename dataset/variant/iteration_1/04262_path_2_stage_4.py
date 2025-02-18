import matplotlib.pyplot as plt

genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Sci-Fi', 'Romance', 'Biography', 'Fantasy', 'Self-Help', 'Children']

popularity_downtown = [70, 85, 50, 90, 40, 65, 75, 60, 55]
popularity_uptown = [60, 80, 65, 85, 45, 60, 70, 50, 55]
monthly_revenue_downtown = [8, 13, 5, 15, 4, 6, 10, 7, 6]
monthly_revenue_uptown = [5, 12, 7, 14, 4, 6, 9, 5, 7]

sorted_downtown_indices = sorted(range(len(popularity_downtown)), key=lambda i: popularity_downtown[i])
sorted_uptown_indices = sorted(range(len(popularity_uptown)), key=lambda i: popularity_uptown[i])

sorted_genres_downtown = [genres[i] for i in sorted_downtown_indices]
sorted_popularity_downtown = [popularity_downtown[i] for i in sorted_downtown_indices]
sorted_revenue_downtown = [monthly_revenue_downtown[i] for i in sorted_downtown_indices]

sorted_genres_uptown = [genres[i] for i in sorted_uptown_indices]
sorted_popularity_uptown = [popularity_uptown[i] for i in sorted_uptown_indices]
sorted_revenue_uptown = [monthly_revenue_uptown[i] for i in sorted_uptown_indices]

fig, axes = plt.subplots(2, 2, figsize=(18, 12))

# Use a single consistent color for all bars
consistent_color = 'skyblue'

axes[0, 0].bar(sorted_genres_downtown, sorted_popularity_downtown, color=consistent_color, edgecolor='red', linestyle='-.')
axes[0, 0].set_title('Book Genre Popularity in Downtown Branch', fontsize=14, weight='light')
axes[0, 0].set_ylabel('Popularity Score', fontsize=12, style='italic')
axes[0, 0].set_xticklabels(sorted_genres_downtown, rotation=45, ha='right', fontsize=10, style='oblique')
axes[0, 0].grid(axis='x', linestyle=':', alpha=0.5, color='grey')

axes[0, 1].bar(sorted_genres_uptown, sorted_popularity_uptown, color=consistent_color, edgecolor='black', linewidth=1.5)
axes[0, 1].set_title('Book Genre Popularity in Uptown Branch', fontsize=14, weight='regular')
axes[0, 1].set_ylabel('Popularity Score', fontsize=12, color='purple')
axes[0, 1].set_xticklabels(sorted_genres_uptown, rotation=45, ha='right', fontsize=9)
axes[0, 1].grid(axis='x', linestyle='-.', alpha=0.8, color='blue')

sorted_revenue_downtown_indices = sorted(range(len(monthly_revenue_downtown)), key=lambda i: monthly_revenue_downtown[i])
sorted_revenue_uptown_indices = sorted(range(len(monthly_revenue_uptown)), key=lambda i: monthly_revenue_uptown[i])

sorted_genres_revenue_downtown = [genres[i] for i in sorted_revenue_downtown_indices]
sorted_genres_revenue_uptown = [genres[i] for i in sorted_revenue_uptown_indices]

axes[1, 0].bar(sorted_genres_revenue_downtown, sorted_revenue_downtown, color=consistent_color, edgecolor='red', linestyle='--')
axes[1, 0].set_title('Monthly Revenue by Genre in Downtown Branch', fontsize=14, weight='bold', color='blue')
axes[1, 0].set_ylabel('Revenue ($1000s)', fontsize=12, style='italic', color='green')
axes[1, 0].set_xticklabels(sorted_genres_revenue_downtown, rotation=45, ha='right', fontsize=10, weight='bold')
axes[1, 0].grid(axis='x', linestyle='--', alpha=0.4, color='orange')

axes[1, 1].bar(sorted_genres_revenue_uptown, sorted_revenue_uptown, color=consistent_color, edgecolor='brown', linewidth=2, linestyle=':')
axes[1, 1].set_title('Monthly Revenue by Genre in Uptown Branch', fontsize=14, weight='light')
axes[1, 1].set_ylabel('Revenue ($1000s)', fontsize=12, color='red')
axes[1, 1].set_xticklabels(sorted_genres_revenue_uptown, rotation=45, ha='right', fontsize=9, weight='light')
axes[1, 1].grid(axis='x', linestyle='-.', alpha=0.6, color='green')

plt.suptitle("Popularity and Monthly Revenue of Book Genres in Bibliophile's Haven Branches (2023)", fontsize=16, weight='bold', y=0.98)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Defining genres and average popularity over the decade
genres = ['Fiction', 'Non-Fiction', 'Science', 'History', 'Fantasy']
avg_popularity = [
    np.mean([30, 35, 40, 45, 50, 55, 65, 70, 75, 80]),        # Fiction
    np.mean([20, 25, 22, 30, 35, 38, 40, 42, 45, 48]),        # Non-Fiction
    np.mean([10, 12, 15, 17, 20, 22, 25, 28, 30, 32]),        # Science
    np.mean([15, 18, 20, 22, 25, 26, 28, 30, 32, 35]),        # History
    np.mean([25, 28, 29, 32, 35, 38, 40, 42, 45, 50])         # Fantasy
]

# Sorting genres by their average popularity
genres_sorted_indices = np.argsort(avg_popularity)
genres_sorted = [genres[i] for i in genres_sorted_indices]
avg_popularity_sorted = [avg_popularity[i] for i in genres_sorted_indices]

# Bar chart for genres sorted by average popularity
plt.figure(figsize=(10, 6))
plt.bar(genres_sorted, avg_popularity_sorted, color='b', alpha=0.7)
plt.title('Average Book Popularity by Genre (2010-2019)', fontsize=16, fontweight='bold')
plt.xlabel('Genre', fontsize=12)
plt.ylabel('Average Books Borrowed', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the chart
plt.tight_layout()
plt.show()
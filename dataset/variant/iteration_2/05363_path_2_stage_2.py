import matplotlib.pyplot as plt
import numpy as np

# Defining genres and randomly altered average popularity over the decade
genres = ['Fiction', 'Non-Fiction', 'Science', 'History', 'Fantasy']
avg_popularity = [
    np.mean([75, 45, 40, 30, 65, 50, 80, 55, 70, 35]),        # Fiction (altered)
    np.mean([42, 25, 22, 38, 48, 20, 45, 30, 35, 40]),        # Non-Fiction (altered)
    np.mean([20, 32, 15, 30, 28, 10, 25, 22, 12, 17]),        # Science (altered)
    np.mean([28, 18, 32, 25, 30, 35, 20, 22, 15, 26]),        # History (altered)
    np.mean([35, 42, 29, 45, 25, 38, 50, 32, 40, 28])         # Fantasy (altered)
]

# Sorting genres by their altered average popularity
genres_sorted_indices = np.argsort(avg_popularity)
genres_sorted = [genres[i] for i in genres_sorted_indices]
avg_popularity_sorted = [avg_popularity[i] for i in genres_sorted_indices]

# Bar chart for genres sorted by altered average popularity
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
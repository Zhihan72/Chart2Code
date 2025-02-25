import matplotlib.pyplot as plt
import numpy as np

genres = ['Fic', 'Non-Fic', 'Sci', 'Hist', 'Fant']
avg_popularity = [
    np.mean([75, 45, 40, 30, 65, 50, 80, 55, 70, 35]),
    np.mean([42, 25, 22, 38, 48, 20, 45, 30, 35, 40]),
    np.mean([20, 32, 15, 30, 28, 10, 25, 22, 12, 17]),
    np.mean([28, 18, 32, 25, 30, 35, 20, 22, 15, 26]),
    np.mean([35, 42, 29, 45, 25, 38, 50, 32, 40, 28])
]

genres_sorted_indices = np.argsort(avg_popularity)
genres_sorted = [genres[i] for i in genres_sorted_indices]
avg_popularity_sorted = [avg_popularity[i] for i in genres_sorted_indices]

colors = ['g', 'r', 'c', 'm', 'y']

plt.figure(figsize=(10, 6))
plt.bar(genres_sorted, avg_popularity_sorted, color=colors)
plt.xlabel('Genre', fontsize=12)
plt.ylabel('Avg Borrowed', fontsize=12)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
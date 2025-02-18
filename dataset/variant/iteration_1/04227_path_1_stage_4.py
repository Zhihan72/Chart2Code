import matplotlib.pyplot as plt
import numpy as np

years = ["2018", "2019", "2020", "2021", "2022"]
genres = ["Action", "Romance", "Adventure", "Comedy"]

ratings_data = np.array([
    [7.8, 7.6, 8.0, 7.5, 7.7],  # Action
    [7.2, 7.4, 7.1, 7.3, 7.5],  # Romance
    [7.9, 8.1, 8.0, 8.2, 8.3],  # Adventure
    [7.0, 7.3, 7.5, 7.4, 7.1]   # Comedy
])

colors = ['#1E90FF', '#FFD700', '#8B008B', '#FF6347']

fig, ax = plt.subplots(figsize=(12, 8))
bar_height = 0.2
y_pos = np.arange(len(years))

for i, genre in enumerate(genres):
    ax.barh(y_pos + i * bar_height, ratings_data[i], height=bar_height, color=colors[i], label=genre)

plt.title('Cinematic Magic: Annual Average Audience Ratings (2018-2022)', fontsize=14, pad=20)
plt.ylabel('Year', fontsize=12)
plt.xlabel('Average Rating', fontsize=12)
plt.yticks(y_pos + bar_height * (len(genres) / 2 - 0.5), years)
plt.legend(title="Genres")

for i, genre in enumerate(genres):
    for j in range(len(years)):
        ax.text(ratings_data[i][j] + 0.05, y_pos[j] + i * bar_height, f'{ratings_data[i][j]:.1f}', 
                ha='left', va='center', fontsize=9, color='black')

plt.show()
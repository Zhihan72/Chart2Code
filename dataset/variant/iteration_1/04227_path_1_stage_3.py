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

fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.2
x_pos = np.arange(len(years))

for i, genre in enumerate(genres):
    ax.bar(x_pos + i * bar_width, ratings_data[i], width=bar_width, color=colors[i])

plt.title('Cinematic Magic: Annual Average Audience Ratings (2018-2022)', fontsize=14, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Rating', fontsize=12)
plt.xticks(x_pos + bar_width * (len(genres) / 2 - 0.5), years)

for i, genre in enumerate(genres):
    for j in range(len(years)):
        ax.text(x_pos[j] + i * bar_width, ratings_data[i][j] + 0.05, f'{ratings_data[i][j]:.1f}', 
                ha='center', va='bottom', fontsize=9, color='black', rotation=90)

plt.show()
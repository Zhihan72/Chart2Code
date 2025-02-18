import matplotlib.pyplot as plt
import numpy as np

years = ["Year-18", "Yr-19", "TwoZero20", "Y21", "YrTwentyTwo"]
genres = ["Act!", "Romnce", "Thriller", "Advntu", "Comdy"]

ratings_data = np.array([
    [7.8, 7.6, 8.0, 7.5, 7.7],  
    [7.2, 7.4, 7.1, 7.3, 7.5],  
    [6.5, 6.8, 6.9, 7.0, 6.7],  
    [7.9, 8.1, 8.0, 8.2, 8.3],  
    [7.0, 7.3, 7.5, 7.4, 7.1]   
])

fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.15
x_pos = np.arange(len(years))

single_color = '#1E90FF'

for i, genre in enumerate(genres):
    ax.bar(x_pos + i * bar_width, ratings_data[i], width=bar_width, color=single_color, label=genre)

plt.tight_layout()
plt.title('Movie Charisma: Ratings Over Time (2018-2022)', fontsize=14, pad=20)
plt.xlabel('Timeline', fontsize=12)
plt.ylabel('Score Average', fontsize=12)
plt.xticks(x_pos + bar_width * (len(genres) / 2 - 0.5), years)
plt.legend(title="Cinema Types", fontsize=10)

for i, genre in enumerate(genres):
    for j in range(len(years)):
        ax.text(x_pos[j] + i * bar_width, ratings_data[i][j] + 0.05, f'{ratings_data[i][j]:.1f}', 
                ha='center', va='bottom', fontsize=9, color='black', rotation=90)

fig.tight_layout()
plt.show()
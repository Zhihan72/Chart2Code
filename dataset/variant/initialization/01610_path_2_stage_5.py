import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

technology = [3, 3.5, 3.8, 4, 3.9, 4.1, 4.2, 4.4, 5, 4.8, 5.1, 5.3, 5.5, 5.6, 5.2, 5.8, 6, 6.5, 6.2, 6.8, 7, 7.3, 7.5, 7.8, 8, 8.2, 8.5, 8.3, 8.7, 9, 8.9, 9.1, 9.3, 9.5, 9.6, 10, 9.8, 10.2, 10.5, 10.8, 11, 11.3, 11.5, 11.2, 11.8, 12, 12.3, 12.5, 12.8, 13, 13.2, 13.5]
comedy = [2, 2.5, 2.8, 3, 2.9, 3.1, 3.3, 3.2, 4, 4.1, 4.3, 4.5, 4.2, 4.8, 5, 5.5, 5.2, 5.3, 5.6, 6, 6.3, 6.5, 6.2, 6.8, 7, 7.2, 7.4, 7.3, 7.8, 8, 8.3, 8.5, 8.7, 8.5, 9, 9.5, 9.8, 9.6, 10, 10.2, 10.5, 10.8, 11, 11.3, 11.5, 11.8, 12, 12.3, 12.6, 12.7, 13, 13.5]
true_crime = [1.5, 1.8, 2, 2.3, 2.1, 2.5, 2.7, 2.8, 3, 3.2, 3.5, 3.3, 3.8, 4, 4.2, 4.5, 4.3, 4.6, 5, 5.3, 5.5, 5.8, 6, 6.2, 6.5, 6.7, 7, 7.2, 7.5, 8, 8.3, 8.5, 8.2, 8.6, 9, 9.1, 9.5, 9.3, 9.8, 10, 10.3, 10.5, 11, 11.2, 11.7, 11.8, 12, 12.5, 12.7, 13, 13.3, 13.5]

data = [technology, comedy, true_crime]
genres = ['Tech', 'Com', 'Crime']

sns.set(style="darkgrid")

plt.figure(figsize=(12, 8))
box = plt.boxplot(data, patch_artist=True, labels=genres, notch=False, vert=False)

# Change color palette to 'muted'
colors = sns.color_palette("muted", len(genres))
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

for i, genre_data in enumerate(data, start=1):
    plt.scatter(genre_data, np.full_like(genre_data, i), alpha=0.6, edgecolor='none', marker='^')

means = [np.mean(genre) for genre in data]
plt.scatter(means, range(1, len(means) + 1), color='darkred', marker='x', label='Mean')

plt.setp(box['whiskers'], color='black', linestyle='-.')
plt.setp(box['caps'], color='black')
plt.setp(box['medians'], color='yellow', linewidth=2)

plt.title('Podcast Listening Trend', fontsize=16, fontweight='bold', pad=20)
plt.ylabel('Genres', fontsize=12)
plt.xlabel('Hours/Week', fontsize=12)

plt.grid(axis='y', linestyle=':', alpha=0.9)

plt.legend(['Mean'], loc='lower right')

plt.tight_layout()

plt.show()
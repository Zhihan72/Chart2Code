import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Arbitrarily rearranged data for weekly podcast listening hours for different genres over a year
technology = [3.9, 5.5, 3.8, 4, 5.3, 5.6, 3.5, 5, 3, 5.8, 5.2, 4.2, 6.5, 7.8, 6, 6.2, 9.1, 5.1, 7.3, 5.3, 7.5, 7, 4.8, 8.2, 8.3, 4.1, 7.8, 6.8, 8.5, 6.5, 7, 6.5, 5.8, 6, 10.2, 8.3, 11.5, 8.7, 11, 9.8, 12.3, 9.3, 9.5, 10.8, 8.9, 11.2, 12.5, 10.5, 10, 10.8, 13, 12.8]
comedy = [6.2, 4, 7.8, 5, 2.9, 4.2, 5.2, 4.1, 6, 2, 5.3, 4.5, 3.3, 5.5, 6.3, 7.4, 6.5, 2.5, 8.5, 7.3, 2.8, 8, 7.2, 5.3, 8, 5.5, 9.8, 3.1, 9.5, 4.8, 8.3, 5.6, 9, 10.5, 6.8, 10.2, 12.3, 12.6, 9.7, 10.8, 12.7, 10, 11.8, 13, 6.8, 11, 9]
true_crime = [8, 3.5, 2.1, 7.5, 1.5, 5.8, 5.3, 4.2, 3, 5.5, 8, 3.2, 7.2, 8.5, 6, 1.8, 7.8, 6.2, 11.2, 2.5, 6.7, 8.6, 9.3, 7, 9, 11.5, 7.5, 5.3, 5.5, 9.8, 9, 10.3, 4.3, 11.2, 4.6, 2.3, 6.2, 3.8, 7.3, 9.5, 10.5, 8.3, 12, 12.7, 9.1, 10, 10.3, 12.5, 13.5]
history = [1.3, 3.5, 7.3, 1.7, 6.5, 2, 12.5, 8, 1, 3.3, 3.7, 7.8, 6.2, 4.7, 5.5, 6.5, 8, 5.8, 2.5, 11.5, 11.7, 3, 5, 12.3, 6.2, 4, 11.2, 5.3, 10.3, 7, 12.8, 9, 7.5, 13, 11.5, 6, 8.9, 4.2, 11.5, 10.5, 12.3, 13.1, 10.8, 13.1, 9.2, 9.2, 13.5, 8.7, 10.8, 9, 13]
health_fitness = [3.5, 9.5, 2.2, 5.8, 7.2, 1.2, 2.7, 14, 8.3, 8.7, 8.7, 4.3, 11.8, 11.2, 1.5, 4.8, 4, 2.5, 10.8, 8.5, 10.5, 3.3, 10, 4.8, 9.7, 13.5, 9, 5.5, 13.8, 7, 5.3, 5.5, 7.5, 7.7, 8, 7.2, 14.8, 11, 10, 8.3, 11.5, 11.5, 9.5, 12, 13.8, 13.2, 6.3, 13.8, 11.8, 11.8, 12.3, 13.8]

# Compile data into a list
data = [technology, comedy, true_crime, history, health_fitness]
genres = ['Technology', 'Comedy', 'True Crime', 'History', 'Health & Fitness']

sns.set(style="whitegrid")
plt.figure(figsize=(12, 8))
box = plt.boxplot(data, patch_artist=True, labels=genres, notch=True, vert=True)
colors = sns.color_palette("pastel", len(genres))
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
for i, genre_data in enumerate(data, start=1):
    plt.scatter(np.full_like(genre_data, i), genre_data, alpha=0.6, edgecolor='k', linewidth=0.5)
means = [np.mean(genre) for genre in data]
plt.scatter(range(1, len(means) + 1), means, color='black', marker='o', label='Mean')
plt.setp(box['whiskers'], color='darkgray', linestyle='--')
plt.setp(box['caps'], color='darkgray')
plt.setp(box['medians'], color='black')
plt.title('Podcast Listening Evolution:\nWeekly Consumption Hours by Genre', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Podcast Genres', fontsize=12)
plt.ylabel('Listening Hours per Week', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.legend(['Data Points', 'Mean'], loc='upper left')
plt.tight_layout()
plt.show()
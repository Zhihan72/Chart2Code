import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2011, 2021)
genres = ['True Crime', 'Business', 'Technology', 'Health', 'Sports', 'Comedy']
true_crime = [5, 10, 15, 25, 35, 50, 60, 70, 85, 100]
business = [8, 12, 18, 22, 27, 35, 45, 55, 68, 80]
technology = [10, 15, 25, 30, 40, 52, 60, 75, 83, 95]
health = [6, 9, 14, 18, 27, 35, 40, 50, 65, 72]
sports = [4, 8, 12, 20, 28, 35, 42, 50, 60, 68]
comedy = [9, 14, 20, 26, 34, 40, 52, 60, 75, 88]

stacked_data = np.array([true_crime, business, technology, health, sports, comedy])

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.6
single_color = '#4682B4'

bottom = np.zeros(len(years))
for i in range(len(genres)):
    ax.bar(
        years, 
        stacked_data[i], 
        bar_width, 
        bottom=bottom, 
        color=single_color
    )
    bottom += stacked_data[i]

for i, (year, new_podcasts) in enumerate(zip(years, bottom)):
    if i % 2 == 0:
        ax.text(year, new_podcasts + 5, f'{new_podcasts}', ha='center', va='bottom', fontsize=8)

ax.set_title('Podcast Genres (2011-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('New Podcasts', fontsize=12)

ax.set_xticks(years)

plt.tight_layout()
plt.show()
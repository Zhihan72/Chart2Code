import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2011, 2021)
genres = ['True Crime', 'Business', 'Technology', 'Health']
true_crime = [5, 10, 15, 25, 35, 50, 60, 70, 85, 100]
business = [8, 12, 18, 22, 27, 35, 45, 55, 68, 80]
technology = [-10, -15, -25, -30, -40, -52, -60, -75, -83, -95]  # Simulated negative values
health = [-6, -9, -14, -18, -27, -35, -40, -50, -65, -72]       # Simulated negative values

stacked_data = np.array([true_crime, business, technology, health])

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.5
colors = ['#4682B4', '#B4464D', '#46B482', '#DDA0DD']

for i in range(len(genres)):
    ax.bar(
        years, 
        stacked_data[i], 
        bar_width, 
        color=colors[i],
        label=genres[i]
    )

ax.axhline(0, color='black', linewidth=0.8)

ax.set_title('Diverging Podcast Genres (2011-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('New Podcasts', fontsize=12)

ax.set_xticks(years)
ax.legend(loc='lower left')

plt.tight_layout()
plt.show()
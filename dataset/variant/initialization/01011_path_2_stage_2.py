import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

space_opera = np.array([30, 35, 40, 60, 80, 100, 120, 150, 180, 200, 220])
alien_encounters = np.array([20, 25, 30, 35, 45, 55, 70, 90, 110, 130, 150])
cosmic_adventure = np.array([10, 15, 20, 25, 35, 50, 70, 95, 120, 140, 160])
space_thriller = np.array([5, 10, 15, 20, 30, 40, 60, 80, 100, 120, 140])
time_travel_epic = np.array([8, 12, 18, 25, 35, 50, 75, 100, 125, 150, 175])

# New made-up genres
galactic_comedy = np.array([3, 5, 8, 10, 15, 25, 35, 50, 70, 90, 110])
stellar_mystery = np.array([4, 7, 12, 18, 25, 38, 55, 75, 95, 110, 130])

genre_data = np.vstack([
    space_opera, 
    alien_encounters, 
    cosmic_adventure, 
    space_thriller, 
    time_travel_epic,
    galactic_comedy,
    stellar_mystery
])

colors = ['#9b59b6', '#e74c3c', '#2ecc71', '#f1c40f', '#34495e', '#e67e22', '#3498db']

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(years, genre_data, labels=[
    'Space Opera', 
    'Alien Encounters', 
    'Cosmic Adventure', 
    'Space Thriller', 
    'Time Travel Epic',
    'Galactic Comedy',
    'Stellar Mystery'
], colors=colors, linewidth=1.5, linestyles='-.')

ax.set_title('Celestial Cinema: Evolution of Popular Genres\nin Space Movies (2010-2020)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Popularity Score', fontsize=12)

ax.legend(loc='lower right', fontsize=10, title='Genres', frameon=True, shadow=True, borderpad=1)

ax.grid(linestyle=':', alpha=0.4)

plt.xticks(years, rotation=90)
plt.yticks(np.arange(0, 301, 60))

ax.annotate('Rise of Time Travel Epics', xy=(2017, 150), xytext=(2011, 250),
            arrowprops=dict(facecolor='grey', arrowstyle='->', connectionstyle='arc3,rad=.3'), fontsize=10, color='red')

plt.tight_layout()

plt.show()
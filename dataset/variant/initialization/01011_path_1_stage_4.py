import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
space_opera = np.array([30, 35, 40, 60, 80, 100, 120, 150, 180, 200, 220])
# Removed 'alien_encounters' data group
cosmic_adventure = np.array([10, 15, 20, 25, 35, 50, 70, 95, 120, 140, 160])
space_thriller = np.array([5, 10, 15, 20, 30, 40, 60, 80, 100, 120, 140])
time_travel_epic = np.array([8, 12, 18, 25, 35, 50, 75, 100, 125, 150, 175])

# Update the data to exclude 'alien_encounters'
genre_data = np.vstack([
    space_opera, cosmic_adventure, 
    space_thriller, time_travel_epic
])

fig, ax = plt.subplots(figsize=(12, 8))
consistent_color = '#66b3ff'
ax.stackplot(years, genre_data, colors=[consistent_color]*4, alpha=0.8)

# Remove border
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 301, 50))

plt.tight_layout()
plt.show()
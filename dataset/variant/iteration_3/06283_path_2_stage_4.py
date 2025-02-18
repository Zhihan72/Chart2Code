import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

# Manually swapped some values within the bird categories
sparrows = np.array([200, 300, 550, 400, 700, 850, 1250, 950, 1100, 1400, 1500])
hawks = np.array([200, 100, 300, 350, 450, 400, 550, 500, 600, 750, 700])
swallows = np.array([350, 300, 400, 450, 600, 500, 800, 700, 900, 1000, 1100])
pelicans = np.array([60, 50, 70, 80, 120, 100, 160, 140, 180, 200, 250])
geese = np.array([150, 100, 200, 350, 600, 500, 800, 700, 900, 1100, 1000])

bird_migrations = np.vstack([sparrows, hawks, swallows, pelicans, geese])

fig, ax = plt.subplots(figsize=(14, 8))

# Plotting with a single color
single_color = '#66b3ff'
ax.stackplot(years, bird_migrations, colors=[single_color for _ in range(len(bird_migrations))], alpha=0.8)

plt.show()
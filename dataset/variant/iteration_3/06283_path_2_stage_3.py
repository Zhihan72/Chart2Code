import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

sparrows = np.array([200, 300, 400, 550, 700, 850, 950, 1100, 1250, 1400, 1500])
hawks = np.array([100, 200, 300, 350, 400, 450, 500, 550, 600, 700, 750])
swallows = np.array([300, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 1100])
pelicans = np.array([50, 60, 70, 80, 100, 120, 140, 160, 180, 200, 250])
geese = np.array([100, 150, 200, 350, 500, 600, 700, 800, 900, 1000, 1100])

bird_migrations = np.vstack([sparrows, hawks, swallows, pelicans, geese])

fig, ax = plt.subplots(figsize=(14, 8))

# Plotting with a single color
single_color = '#66b3ff'
ax.stackplot(years, bird_migrations, colors=[single_color for _ in range(len(bird_migrations))], alpha=0.8)

plt.show()
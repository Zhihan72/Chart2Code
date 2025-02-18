import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)
migration_africa = np.array([2, 3, 5, 8, 12, 14, 16, 18, 20, 23, 25, 28, 30, 32, 35, 39, 42, 45, 48, 52, 55])
migration_asia = np.array([5, 7, 10, 14, 18, 20, 24, 28, 35, 40, 45, 48, 54, 57, 60, 65, 70, 76, 80, 85, 90])
migration_europe = np.array([3, 4, 6, 10, 12, 13, 14, 15, 16, 18, 20, 22, 24, 25, 27, 28, 30, 32, 34, 36, 38])
migration_namerica = np.array([2, 3, 4, 5, 7, 8, 9, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26])
migration_samerica = np.array([3, 5, 7, 10, 12, 15, 18, 21, 24, 28, 30, 33, 35, 37, 40, 42, 45, 48, 51, 54, 57])

migration_data = np.vstack([migration_africa, migration_asia, migration_europe, migration_namerica, migration_samerica])

fig, ax = plt.subplots(figsize=(14, 8))

# Changed colors for the stacked area chart
ax.stackplot(years, migration_data, colors=['#8B0000', '#00CED1', '#4682B4', '#3CB371', '#FF4500'], alpha=0.8)

ax.set_xticks([])
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.show()
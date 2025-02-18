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

ax.stackplot(years, migration_data, 
             colors=['#4B0082', '#7FFF00', '#FF8C00', '#4169E1', '#DC143C'], alpha=0.8)

ax.set_title('Urban Migration\n(2000-20)', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Yr', fontsize=12, weight='bold')
ax.set_ylabel('Migrants (M)', fontsize=12, weight='bold')

ax.set_xticks(years[::2])
ax.set_xticklabels(years[::2], rotation=45)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

ax.grid(False)

plt.show()
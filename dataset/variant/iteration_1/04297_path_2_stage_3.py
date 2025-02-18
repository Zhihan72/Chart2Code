import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

deer = [12, 15, 14, 15, 18, 19, 21, 23, 24, 27, 28]
foxes = [8, 10, 9, 11, 11, 13, 12, 14, 14, 15, 16]
rabbits = [30, 26, 28, 27, 28, 30, 33, 34, 34, 37, 39]
wolves = [4, 5, 4, 5, 7, 6, 7, 6, 8, 9, 8]

populations = np.vstack([deer, foxes, rabbits, wolves])
colors = ['#8B4513', '#D2691E', '#FFD700', '#4682B4']

plt.figure(figsize=(14, 8))
plt.stackplot(years, populations, colors=colors, alpha=0.8)

plt.title('Forest Biodiversity (2010-2020)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Pop. (thousands)', fontsize=12)

plt.xticks(years, rotation=45)

plt.tight_layout()
plt.show()
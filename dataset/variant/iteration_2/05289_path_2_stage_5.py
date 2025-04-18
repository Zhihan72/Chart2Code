import matplotlib.pyplot as plt
import numpy as np

weeks = np.array(range(1, 53))
mystery_readings = np.array([25, 28, 30, 32, 29, 25, 27, 32, 35, 30, 28, 26, 33, 35, 28, 30, 32, 36, 38, 40, 32, 28, 30, 29, 27, 35, 38, 40, 45, 42, 40, 38, 35, 40, 42, 45, 48, 50, 45, 42, 40, 38, 35, 30, 32, 34, 36, 38, 35, 30, 28, 25])
fantasy_readings = np.array([18, 20, 22, 25, 23, 22, 24, 26, 29, 27, 25, 23, 20, 22, 25, 27, 28, 26, 24, 22, 20, 19, 21, 23, 25, 26, 28, 29, 27, 25, 23, 22, 24, 26, 27, 28, 30, 32, 29, 27, 25, 23, 20, 21, 23, 25, 26, 28, 29, 27, 26, 24])
science_fiction_readings = np.array([30, 28, 29, 31, 33, 32, 30, 29, 31, 35, 37, 34, 32, 30, 29, 28, 27, 29, 30, 32, 34, 36, 31, 30, 28, 27, 26, 29, 32, 34, 33, 31, 29, 30, 32, 33, 35, 36, 34, 32, 30, 29, 28, 30, 32, 31, 30, 28, 27, 25, 26, 24])
adventure_readings = np.array([22, 24, 26, 25, 27, 28, 29, 31, 33, 30, 28, 27, 25, 26, 28, 29, 30, 31, 33, 35, 36, 34, 32, 33, 35, 37, 38, 39, 40, 41, 42, 40, 38, 37, 36, 35, 33, 32, 30, 31, 33, 34, 32, 30, 29, 31, 34, 33, 32, 31, 30, 28])

fig, ax = plt.subplots(figsize=(14, 8))
consistent_color = '#1f77b4'
ax.barh(weeks - 0.45, mystery_readings, height=0.2, color=consistent_color)
ax.barh(weeks - 0.15, fantasy_readings, height=0.2, color=consistent_color)
ax.barh(weeks + 0.15, science_fiction_readings, height=0.2, color=consistent_color)
ax.barh(weeks + 0.45, adventure_readings, height=0.2, color=consistent_color)

ax.set_yticks(weeks[::4])

# Remove axis borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()
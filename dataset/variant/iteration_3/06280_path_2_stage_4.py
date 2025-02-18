import matplotlib.pyplot as plt
import numpy as np

years = np.array(range(1980, 2020, 5))
country_a_production = np.array([4, 14, 28, 49, 80, 120, 185, 243])
country_b_production = np.array([2, 12, 25, 60, 90, 140, 210, 275])
country_c_production = np.array([1, 5, 15, 35, 60, 105, 180, 240])
country_d_production = np.array([3, 10, 20, 45, 70, 100, 165, 220])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, country_a_production, marker='o', linestyle='-', linewidth=2, color='crimson')
ax.plot(years, country_b_production, marker='s', linestyle='-', linewidth=2, color='teal')
ax.plot(years, country_c_production, marker='^', linestyle='-', linewidth=2, color='goldenrod')
ax.plot(years, country_d_production, marker='x', linestyle='-', linewidth=2, color='purple')

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)
space_tourists = np.array([0.5, 1.2, 2.5, 5.0, 8.5, 12.0, 15.0, 18.5, 22.0, 28.5, 35.0])
revenue_per_tourist = 1.0
space_revenue = space_tourists * revenue_per_tourist * (1.0 + np.array([0.1, 0.15, 0.2, 0.18, 0.25, 0.22, 0.3, 0.28, 0.35, 0.33, 0.4]))

fig, ax1 = plt.subplots(figsize=(14, 9))

ax1.bar(years, space_revenue, color='#FF5733', alpha=0.75, width=0.4)
ax1.tick_params(axis='y', labelcolor='#FF5733')

ax1.grid(True, linestyle='-', alpha=0.7)

fig.tight_layout()
plt.show()
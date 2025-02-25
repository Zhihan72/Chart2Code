import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2023, 2034)

apples = [100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300]
bananas = [80, 85, 90, 95, 100, 110, 115, 120, 130, 140, 150]
cherries = [40, 50, 60, 70, 80, 90, 100, 110, 120, 125, 130]

export_data = [np.array(apples), np.array(bananas), np.array(cherries)]

colors = ['#FF5733', '#33FF57', '#3357FF']

fig, ax = plt.subplots(figsize=(12, 8))

for data, color in zip(export_data, colors):
    ax.plot(years, data, marker='o', color=color)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
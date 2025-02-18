import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
dissolved_oxygen = [7.5, 7.2, 6.9, 6.7, 6.5, 6.2, 6.0, 5.8, 5.6, 5.5, 5.2]
ph_level = [7.0, 6.9, 6.8, 6.7, 6.5, 6.4, 6.3, 6.1, 6.0, 6.0, 5.9]

fig, ax1 = plt.subplots(figsize=(14, 7))

ax1.plot(years, dissolved_oxygen, color='cyan', marker='o', linewidth=2)
ax1.plot(years, ph_level, color='orange', marker='^', linewidth=2)

ax1.set_xlabel('Yr', fontsize=12)
ax1.set_ylabel('DO / pH', fontsize=12, color='cyan')
plt.title('River Health (2010-2020)', fontsize=16, fontweight='bold')

fig.tight_layout()
plt.show()
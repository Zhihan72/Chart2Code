import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2023)

metropolis_speeds = np.array([5, 7, 10, 14, 20, 25, 30, 40, 55, 70, 85])

fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(years, metropolis_speeds, color='orange', marker='o', linestyle='-', linewidth=2)

ax.axvline(x=2019, color='brown', linestyle=':', linewidth=1)
ax.axvline(x=2021, color='brown', linestyle=':', linewidth=1)

ax.set_xticks(years)
ax.set_xticklabels([''] * len(years))

ax.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
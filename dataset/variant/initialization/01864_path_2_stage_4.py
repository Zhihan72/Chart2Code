import matplotlib.pyplot as plt
import numpy as np

decades = ['90s', '00s', '10s', '20s']
solar = [5, 15, 50, 120]
wind = [10, 25, 60, 150]
hydro = [100, 120, 150, 160]

energy_data = np.array([solar, wind, hydro])

fig, ax = plt.subplots(figsize=(12, 7))
# Manually shuffled colors for each data group
colors = ['#20B2AA', '#87CEEB', '#FFA07A']

ax.stackplot(decades, energy_data, colors=colors, alpha=0.8)

ax.set_xlabel('Dec', fontsize=12)
ax.set_ylabel('Energy (Units)', fontsize=12)

plt.tight_layout()
plt.show()
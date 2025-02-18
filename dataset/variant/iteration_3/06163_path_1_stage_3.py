import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2018, 2023)

water = np.array([50, 55, 60, 65, 70])
coffee = np.array([20, 22, 24, 28, 30])
tea = np.array([15, 16, 18, 20, 22])
soda = np.array([10, 12, 14, 16, 18])

data = np.vstack([water, coffee, tea, soda])

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(years, data, colors=['#add8e6', '#98fb98', '#8a735b', '#ffb6c1'], alpha=0.8, linestyle='-', linewidth=2)

ax.set_xticks(years)
ax.set_yticks(np.arange(0, 201, 20))
ax.set_ylim(0, 170)

ax.grid(axis='both', linestyle=':', linewidth=0.5)
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
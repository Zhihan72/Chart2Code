import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar = [10, 14, 21, 30, 38, 50, 68, 80, 92, 110, 130]
wind = [50, 58, 70, 85, 97, 110, 128, 140, 155, 170, 190]
hydro = [300, 305, 310, 312, 315, 320, 322, 325, 328, 330, 332]

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, solar, color='deepskyblue', marker='p', linestyle='-.')
ax.plot(years, wind, color='orange', marker='x', linestyle='--')
ax.plot(years, hydro, color='royalblue', marker='h', linestyle='-')

ax.set_xticks(years)
ax.set_yticks(np.arange(0, 400, 50))

ax.grid(linestyle=':', alpha=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()
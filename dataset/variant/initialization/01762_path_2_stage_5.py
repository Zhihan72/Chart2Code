import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2051, 10)
energy_sources = ['Coal', 'Natural Gas', 'Nuclear', 'Hydroelectric', 'Renewables']

coal = [35, 30, 40, 15, 20, 25]
natural_gas = [18, 15, 25, 25, 20, 20]
nuclear = [15, 14, 10, 15, 12, 10]
hydroelectric = [14, 12, 16, 10, 13, 15]
renewables = [39, 8, 15, 5, 32, 20]
data = np.vstack([coal, natural_gas, nuclear, hydroelectric, renewables])

total_energy_consumption = [8500, 10000, 8000, 9500, 10500, 9000]

fig, (ax2, ax1) = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))

single_color = '#1f77b4'
ax2.stackplot(years, data, colors=[single_color] * len(energy_sources), alpha=0.7, edgecolor='black')
ax2.set_xticks(years)
ax2.set_yticks(np.arange(0, 101, 10))
ax2.grid(True, linestyle=':', alpha=0.6)

ax1.plot(years, total_energy_consumption, marker='s', color=single_color, linestyle='--', linewidth=2)
ax1.set_xticks(years)
ax1.set_yticks(np.arange(8000, 11001, 500))
ax1.grid(True, linestyle='-.', alpha=0.5)

for spine in ax1.spines.values():
    spine.set_visible(False)
for spine in ax2.spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()
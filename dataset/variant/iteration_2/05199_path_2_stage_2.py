import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2026)

batteries = [0.5, 2, 1, 5, 3, 12, 18, 20, 28, 35, 50]
pumped_storage = [6, 7, 5, 10, 12, 14, 13, 17, 19, 21, 22]
compressed_air = [0.3, 0.2, 0.6, 0.8, 1.3, 1.4, 1.8, 2.6, 2.8, 3.3, 4.2]
flywheels = [0.12, 0.11, 0.17, 0.15, 0.24, 0.28, 0.34, 0.33, 0.45, 0.47, 0.52]

storage_data = np.array([batteries, pumped_storage, compressed_air, flywheels])

colors = ['#76C7C0', '#FFB74D', '#FF8A80', '#AED581']

fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(years, storage_data, colors=colors, alpha=0.8)

ax.set_xlim(years[0], years[-1])
ax.set_ylim(0, 90)
ax.set_xticks(years)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{int(y)} GWh'))

ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()

plt.show()
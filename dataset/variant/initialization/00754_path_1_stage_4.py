import numpy as np
import matplotlib.pyplot as plt

cities = ['New York', 'London', 'Tokyo']
years = np.array(['2018', '2019', '2020', '2021', '2022'])

data = np.array([
    [30, 25, 40, 35, 28],
    [20, 18, 22, 22, 20],
    [15, 10, 12, 16, 11],
])

bar_width = 0.25

fig, ax = plt.subplots(figsize=(10, 6))
indices = np.arange(len(years))

for idx, city in enumerate(cities):
    ax.bar(indices + idx * bar_width, data[idx], width=bar_width)

ax.set_xticks(indices + bar_width)
ax.set_xticklabels(years)

plt.tight_layout()
plt.show()
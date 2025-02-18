import matplotlib.pyplot as plt
import numpy as np

genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Science Fiction', 'Biographies', 'Children', 'Fantasy']
quarterly_checkouts = [
    [120, 80, 95, 130],
    [100, 110, 105, 90],
    [60, 70, 75, 65],
    [50, 65, 60, 70],
    [40, 45, 40, 55],
    [30, 35, 40, 60],
    [85, 90, 100, 95]
]

yearly_checkouts = [np.mean(q) for q in quarterly_checkouts]
colors = plt.cm.nipy_spectral(np.linspace(0, 1, len(genres)))

fig, ax1 = plt.subplots(figsize=(12, 8))
bars = ax1.bar(genres, yearly_checkouts, color=colors, edgecolor='black', alpha=0.7)

ax1.set_ylim(0, max(yearly_checkouts) + 20)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

ax2 = ax1.twinx()
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
for index, (genre, quarterly_data) in enumerate(zip(genres, quarterly_checkouts)):
    ax2.plot(quarters, quarterly_data, 'o-', color=colors[index], linewidth=2)

ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_color('grey')
ax2.tick_params(axis='y', colors='grey')

plt.tight_layout()
plt.show()
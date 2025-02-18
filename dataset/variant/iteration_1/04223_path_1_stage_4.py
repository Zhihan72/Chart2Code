import matplotlib.pyplot as plt
import numpy as np

# Data setup
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

# Calculate yearly averages
yearly_checkouts = [np.mean(q) for q in quarterly_checkouts]

# Sort by yearly checkouts
sorted_indices = np.argsort(yearly_checkouts)
genres_sorted = [genres[i] for i in sorted_indices]
yearly_checkouts_sorted = [yearly_checkouts[i] for i in sorted_indices]
quarterly_checkouts_sorted = [quarterly_checkouts[i] for i in sorted_indices]

# Manually shuffle colors for demonstration (without using random)
colors = plt.cm.nipy_spectral(np.linspace(0, 1, len(genres)))
shuffled_colors = [colors[2], colors[0], colors[4], colors[1], colors[5], colors[3], colors[6]]

# Plot Setup
fig, ax1 = plt.subplots(figsize=(12, 8))
bars = ax1.bar(genres_sorted, yearly_checkouts_sorted, color=shuffled_colors, edgecolor='black', alpha=0.7)

ax1.set_ylim(0, max(yearly_checkouts_sorted) + 20)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Plot the quarterly line chart
ax2 = ax1.twinx()
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
for index, (genre, quarterly_data) in enumerate(zip(genres_sorted, quarterly_checkouts_sorted)):
    ax2.plot(quarters, quarterly_data, 'o-', color=shuffled_colors[index], linewidth=2)

ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_color('grey')
ax2.tick_params(axis='y', colors='grey')

plt.tight_layout()
plt.show()
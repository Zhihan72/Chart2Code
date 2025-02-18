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

# Manually altered colors for demonstration
colors = ['#6495ED', '#FFD700', '#FF69B4', '#8A2BE2', '#7FFF00', '#FF4500', '#DA70D6']

# Plot Setup
fig, ax1 = plt.subplots(figsize=(12, 8))
bars = ax1.bar(genres_sorted, yearly_checkouts_sorted, color=colors, edgecolor='darkgrey', alpha=0.85, linewidth=3)

ax1.set_ylim(0, max(yearly_checkouts_sorted) + 20)
ax1.yaxis.grid(True, linestyle='-', linewidth=0.5, color='pink')

# Plot the quarterly line chart with different styles
ax2 = ax1.twinx()
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
marker_styles = ['o', 's', '^', 'D', 'P', '*', 'X']
line_styles = ['-', '--', '-.', ':', '-', '--', '-.']
for index, (genre, quarterly_data) in enumerate(zip(genres_sorted, quarterly_checkouts_sorted)):
    ax2.plot(quarters, quarterly_data, marker_styles[index % 7] + line_styles[index % 7], color=colors[index], linewidth=2.5)

ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_color('green')
ax2.tick_params(axis='y', colors='purple')

plt.legend(genres_sorted, loc='upper left')
plt.tight_layout()
plt.show()
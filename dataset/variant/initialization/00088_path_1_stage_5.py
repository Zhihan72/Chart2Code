import matplotlib.pyplot as plt
import numpy as np

# Data for 2050
sources = ['Solar', 'Wind', 'Hydro', 'Nuclear', 'Coal', 'Gas', 'Other Ren.']
percent_2050 = [20, 25, 15, 5, 15, 10, 10]

# Sort data for 2050
sorted_idx = np.argsort(percent_2050)
sorted_sources = [sources[i] for i in sorted_idx]
sorted_percent_2050 = [percent_2050[i] for i in sorted_idx]

# Create bar chart
fig, ax = plt.subplots(figsize=(10, 8))

# Shuffle colors
colors_shuffled = ['#1E90FF', '#FF4500', '#FFD700', '#9370DB', '#32CD32', '#A9A9A9', '#FFA07A']

# Bar chart for 2050
bars = ax.barh(sorted_sources, sorted_percent_2050, color=colors_shuffled)
ax.xaxis.grid(True, linestyle='--', color='grey', alpha=0.5)
ax.bar_label(bars, fmt='%.1f%%')
ax.set_title('2050 Energy Mix', fontsize=16, pad=20)
ax.set_xlabel('% of Total', fontsize=12)
ax.set_xlim(0, 30)
ax.set_yticklabels(sorted_sources, fontsize=11)

plt.tight_layout()
plt.show()
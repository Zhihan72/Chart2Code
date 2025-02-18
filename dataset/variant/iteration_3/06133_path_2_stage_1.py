import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])
stores = ["Store A", "Store B", "Store C", "Store D", "Store E"]

# Altered Revenue data
revenue = np.array([
    [12, 11, 13, 16, 15],  # Store A
    [9, 11, 8, 13, 12],    # Store B
    [16, 14, 17, 19, 21],  # Store C
    [14, 13, 15, 16, 17],  # Store D
    [10, 12, 9, 13, 14],   # Store E
])

# Altered Employee satisfaction scores
satisfaction_scores = np.array([
    [7.5, 7, 8, 9, 8.5],     # Store A
    [6.5, 7, 6, 7.8, 7.5],   # Store B
    [8, 8.5, 8, 9, 8.8],     # Store C
    [7, 7.5, 7, 8.5, 8],     # Store D
    [7.2, 7.5, 7, 8, 7.8],   # Store E
])

fig, ax1 = plt.subplots(figsize=(14, 8))
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF']
bar_width = 0.15

for idx, store in enumerate(stores):
    ax1.bar(years + idx*bar_width, revenue[idx], width=bar_width, color=colors[idx], alpha=0.7, label=f'{store} Revenue')

ax1.set_title('Retail Chain Performance Analysis:\nRevenue vs Employee Satisfaction (2018-2022)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Revenue (in millions)', fontsize=12)
ax1.set_xticks(years + bar_width*(len(stores)-1)/2)
ax1.set_xticklabels(years)

ax2 = ax1.twinx()
ax2.set_ylabel('Employee Satisfaction (out of 10)', fontsize=12)

for idx, store in enumerate(stores):
    ax2.plot(years, satisfaction_scores[idx], marker='o', linestyle='-', linewidth=2, color=colors[idx], label=f"{store} Satisfaction")
    for x, y in zip(years, satisfaction_scores[idx]):
        ax2.annotate(f'{y}', xy=(x, y), xytext=(0, 5), textcoords='offset points', fontsize=9, color=colors[idx], ha='center')

bars, bar_labels = ax1.get_legend_handles_labels()
lines, line_labels = ax2.get_legend_handles_labels()
ax1.legend(bars + lines, bar_labels + line_labels, title='Stores', loc='upper left', fontsize=10, frameon=True)

ax1.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])
stores = ["Store A", "Store B", "Store C", "Store D", "Store E"]

revenue = np.array([
    [15, 10, 11, 12, 14],  # Store A
    [10, 8, 13, 12, 9],    # Store B
    [20, 15, 14, 18, 16],  # Store C
    [17, 16, 15, 13, 14],  # Store D
    [14, 12, 9, 10, 13],   # Store E
])

satisfaction_scores = np.array([
    [8.5, 9, 8, 7.5, 7],   # Store A
    [7, 7.8, 6.5, 6, 7.5], # Store B
    [8.8, 9.1, 7.5, 8, 8.5], # Store C
    [8, 8.5, 6.8, 7, 7.5], # Store D
    [7.8, 7, 7.2, 8, 7.5], # Store E
])

fig, ax1 = plt.subplots(figsize=(14, 8))

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF']
bar_width = 0.15
for idx, store in enumerate(stores):
    ax1.bar(years + idx*bar_width, revenue[idx], width=bar_width, color=colors[idx], alpha=0.7)

ax1.set_title('Retail Chain Performance Analysis:\nRevenue vs Employee Satisfaction (2018-2022)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Revenue (in millions)', fontsize=12)
ax1.set_xticks(years + bar_width*(len(stores)-1)/2)
ax1.set_xticklabels(years)

ax2 = ax1.twinx()
ax2.set_ylabel('Employee Satisfaction (out of 10)', fontsize=12)

for idx in range(len(stores)):
    ax2.plot(years, satisfaction_scores[idx], marker='o', linestyle='-', linewidth=2, color=colors[idx])
    for x, y in zip(years, satisfaction_scores[idx]):
        ax2.annotate(f'{y}', xy=(x, y), xytext=(0, 5), textcoords='offset points', fontsize=9, color=colors[idx], ha='center')

plt.tight_layout()
plt.show()
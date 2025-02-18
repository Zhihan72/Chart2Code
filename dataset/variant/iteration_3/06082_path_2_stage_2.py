import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2024)
companies = ['TechCorp', 'CloudInc', 'DataSolutions', 'NetServices', 'AIInnovators']

# Manually altered some data points while preserving the original structure
storage_share = np.array([
    [41, 42, 43, 47, 51, 52, 54, 59, 65],
    [31, 29, 26, 24, 22, 19, 17, 18, 16],
    [21, 17, 18, 17, 14, 15, 12, 11, 10],
    [8, 9, 6, 7, 9, 8, 7, 7, 5],
    [2, 3, 5, 5, 4, 3, 7, 6, 4]
])

computing_share = np.array([
    [36, 36, 41, 40, 43, 46, 47, 51, 51],
    [29, 29, 25, 27, 26, 22, 22, 21, 21],
    [19, 19, 21, 18, 18, 16, 15, 17, 14],
    [11, 8, 7, 9, 7, 7, 9, 8, 6],
    [4, 9, 5, 5, 6, 8, 6, 4, 7]
])

ai_services_share = np.array([
    [46, 49, 51, 51, 54, 59, 61, 62, 64],
    [29, 24, 24, 20, 21, 19, 16, 17, 15],
    [11, 13, 11, 12, 14, 12, 14, 11, 10],
    [9, 7, 10, 9, 6, 5, 7, 5, 6],
    [6, 7, 4, 7, 5, 5, 2, 5, 5]
])

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(20, 8), sharey=True)

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

titles = ['AI Services Market Share', 'Computing Services Market Share', 'Storage Services Market Share']
market_share_data = [ai_services_share, computing_share, storage_share]

for ax, data, title in zip(axes, market_share_data, titles):
    bar_width = 0.15
    x_indexes = np.arange(len(years))
    
    for i, company in enumerate(companies):
        ax.bar(x_indexes + i * bar_width, data[i], width=bar_width, label=company if title == titles[2] else "", color=colors[i])
    
    ax.set_xlabel('Year', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x_indexes + bar_width * 2)
    ax.set_xticklabels(years)
    ax.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

axes[0].set_ylabel('Market Share (%)', fontsize=12)

handles, labels = axes[0].get_legend_handles_labels()
unique_labels = dict(zip(labels, handles))
fig.legend(unique_labels.values(), unique_labels.keys(), loc='upper center', fontsize=10, ncol=3, title='Company')

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
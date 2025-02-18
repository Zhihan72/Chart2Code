import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2024)
companies = ['TechCorp', 'CloudInc', 'DataSolutions', 'NetServices', 'AIInnovators']

storage_share = np.array([
    [40, 42, 45, 47, 50, 52, 55, 60, 62],
    [30, 28, 27, 25, 23, 20, 18, 17, 15],
    [20, 18, 17, 16, 15, 14, 13, 12, 11],
    [7, 8, 7, 8, 8, 9, 8, 6, 6],
    [3, 4, 4, 4, 4, 5, 6, 5, 6]
])

computing_share = np.array([
    [35, 37, 40, 41, 44, 45, 48, 50, 52],
    [30, 28, 26, 26, 25, 23, 21, 22, 20],
    [20, 18, 20, 19, 17, 17, 16, 16, 15],
    [10, 9, 8, 8, 8, 8, 8, 7, 7],
    [5, 8, 6, 6, 6, 7, 7, 5, 6]
])

ai_services_share = np.array([
    [45, 48, 50, 52, 55, 58, 60, 63, 65],
    [30, 25, 23, 21, 20, 18, 17, 16, 14],
    [10, 12, 12, 13, 13, 13, 13, 12, 11],
    [10, 8, 9, 8, 7, 6, 6, 6, 5],
    [5, 7, 6, 6, 5, 5, 4, 3, 5]
])

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(20, 8), sharey=True)

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# New order for titles and market share data
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
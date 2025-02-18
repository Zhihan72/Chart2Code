import matplotlib.pyplot as plt

# Days of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Manually altered minutes spent on different browsers each day in a randomized content while maintaining structure
chrome_usage = [130, 115, 120, 180, 125, 140, 160]
firefox_usage = [70, 65, 50, 60, 55, 85, 90]
edge_usage = [10, 25, 20, 35, 30, 15, 20]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

# Combine usage data for the stacked histogram
usage_data = [chrome_usage, firefox_usage, edge_usage]
colors = ['#FF5733', '#FFC300', '#C70039']
labels = ['Chrome', 'Firefox', 'Edge']

# Plot stacked histogram for all browser usage data
axes[0].bar(days, chrome_usage, color=colors[0], label=labels[0])
axes[0].bar(days, firefox_usage, bottom=chrome_usage, color=colors[1], label=labels[1])
axes[0].bar(days, edge_usage, bottom=[c+f for c, f in zip(chrome_usage, firefox_usage)], color=colors[2], label=labels[2])

axes[0].set_title("Browser Usage", fontsize=14, weight='bold')
axes[0].set_ylabel("Minutes Spent", fontsize=12)
axes[0].set_xlabel("Days of the Week", fontsize=12)
axes[0].legend()

# Remove the other empty subplots since we only need one plot
for ax in axes[1:]:
    ax.axis('off')

fig.tight_layout()
plt.show()
import matplotlib.pyplot as plt

# Days of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Minutes spent on different browsers each day
chrome_usage = [120, 130, 115, 125, 140, 180, 160]
firefox_usage = [60, 55, 70, 65, 50, 90, 85]
edge_usage = [20, 15, 10, 25, 30, 35, 20]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

titles = ["Chrome Usage", "Firefox Usage", "Edge Usage"]
usage_data = [chrome_usage, firefox_usage, edge_usage]
colors = ['#FF5733', '#FFC300', '#C70039']

for i, ax in enumerate(axes[:3]):
    ax.bar(days, usage_data[i], color=colors[i])
    ax.set_title(titles[i], fontsize=14, weight='bold')
    ax.set_ylabel("Minutes Spent", fontsize=12)
    ax.set_xlabel("Days of the Week", fontsize=12)
    
    for day, minutes in zip(days, usage_data[i]):
        ax.annotate(f'{minutes} min', xy=(day, minutes), xytext=(day, minutes + 5),
                    ha='center', fontsize=10, color='black')

for ax in axes[:3]:
    ax.set_xticks(days)
    ax.set_xticklabels(days, rotation=45, ha='right', fontsize=10)

fig.tight_layout()
plt.show()
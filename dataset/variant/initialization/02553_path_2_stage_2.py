import matplotlib.pyplot as plt

zones = ['Sunlight Zone', 'Twilight Zone', 'Midnight Zone', 'Abyssal Zone', 'Hadal Zone']
expeditions = [40, 25, 30, 10, 20] 
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(zones, expeditions, color=colors, edgecolor='black', height=0.6)

ax.set_xlabel('Number of Expeditions', fontsize=12, fontweight='bold')
ax.set_title('Decadal Exploration of Ocean Depths:\nExpedition Counts by Oceanic Zone', fontsize=14, fontweight='bold', pad=15)

for bar in ax.containers[0]:  # Accessing the bars directly in ax.containers
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height() / 2, f'{width}', va='center', fontsize=10, fontweight='bold', color='black')

ax.set_yticks(range(len(zones)))
ax.set_yticklabels(zones, fontsize=11)

plt.tight_layout()
plt.show()
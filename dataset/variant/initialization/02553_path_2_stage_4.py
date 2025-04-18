import matplotlib.pyplot as plt

zones = ['Sunlight', 'Twilight', 'Midnight', 'Abyssal', 'Hadal']
expeditions = [40, 25, 30, 10, 20] 
new_colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00']

fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(zones, expeditions, color=new_colors, edgecolor='black', height=0.6)

ax.set_xlabel('Expeditions', fontsize=12, fontweight='bold')
ax.set_title('Oceanic Zone Exploration', fontsize=14, fontweight='bold', pad=15)

for bar in ax.containers[0]:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height() / 2, f'{width}', va='center', fontsize=10, fontweight='bold', color='black')

ax.set_yticks(range(len(zones)))
ax.set_yticklabels(zones, fontsize=11)

plt.tight_layout()
plt.show()
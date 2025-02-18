import matplotlib.pyplot as plt

planetary_labels = ['Moon', 'Titan', 'Mercury', 'Earth', 'Venus']

water_content_data = [
    [0.1, 0.2, 0.1, 0.3, 0.2],
    [40.0, 41.0, 40.5, 41.5, 40.3],
    [0.1, 0.1, 0.2, 0.2, 0.1],
    [70.0, 68.0, 72.0, 71.0, 69.0],
    [0.0, 0.0, 0.1, 0.1, 0.0]
]

fig, ax = plt.subplots(figsize=(12, 8))
box = ax.boxplot(water_content_data, patch_artist=True, notch=True, vert=False, labels=planetary_labels)

colors = ['#FF6347', '#3CB371', '#FFA500', '#4682B4', '#9370DB']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.setp(box['medians'], color='green', linestyle='--')

ax.set_title("Hydration Analysis: Surface Water Levels on Celestial Objects", 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Percentage of Water", fontsize=12, style='italic')
ax.set_ylabel("Celestial Labels", fontsize=12, fontstyle='oblique')

ax.grid(True, linestyle=':', linewidth=1.5, alpha=0.7, which='major')

# Random text positions with different markers
for i, (planet, data) in enumerate(zip(planetary_labels, water_content_data)):
    max_val = max(data)
    ax.text(max_val + 3, i + 1, f'Peak: {max_val:.1f}%', va='center', fontsize=10, color='black')

plt.tight_layout()
plt.show()
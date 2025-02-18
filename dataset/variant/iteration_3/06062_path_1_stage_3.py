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
box = ax.boxplot(water_content_data, patch_artist=True, notch=False, vert=False, labels=planetary_labels)

colors = ['#FFD700', '#BA55D3', '#FFA07A', '#1E90FF', '#FF4500']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.setp(box['medians'], color='black')

ax.set_title("Hydration Analysis: Surface Water Levels on Celestial Objects", 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Percentage of Water", fontsize=12)
ax.set_ylabel("Celestial Labels", fontsize=12)

ax.grid(True, linestyle='--', alpha=0.5, which='both', linewidth=0.7)

for i, (planet, data) in enumerate(zip(planetary_labels, water_content_data)):
    max_val = max(data)
    ax.text(max_val + 3, i + 1, f'Peak: {max_val:.1f}%', va='center', fontsize=10, color=colors[i])

plt.tight_layout()
plt.show()
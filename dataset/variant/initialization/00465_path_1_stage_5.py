import matplotlib.pyplot as plt

# Randomly altered life span data
all_devices_lifespan = [3.8, 5, 4.2, 2.5, 3.3, 4, 3.5, 3.2, 4.5, 3,
                        3.1, 4.7, 4.1, 2.6, 5.1, 4.4, 4.8, 2.9, 3, 3.2,
                        3, 1.9, 2.1, 3.1, 2.2, 3.8, 1.5, 3.6, 3.7, 3.9,
                        1.8, 2, 1.4, 2, 3.5, 3.3, 1.7, 2.8, 1.6, 3.7]

fig, ax = plt.subplots(figsize=(6, 8))
ax.boxplot(all_devices_lifespan, vert=True, patch_artist=True,
           boxprops=dict(facecolor='#FFFDD0', color='blue'),  # Changed box color and border
           whiskerprops=dict(color='green', linestyle='-.'),  # Changed whisker style
           capprops=dict(color='orange', linewidth=2),         # Changed cap color and width
           medianprops=dict(color='purple', linestyle='--'))   # Changed median line style and color

# Randomly altered textual elements
titles = ['Super Gadget Life', 'Lifespan Overview', 'Longevity of Devices']
y_labels = ['Years of Service', 'Functional Period (years)', 'Uptime in Years']
x_labels = ['Devices', 'Tech Gadgets', 'All Units']

ax.set_title(titles[2], fontsize=14, weight='bold', pad=20)
ax.set_ylabel(y_labels[1], fontsize=12)
ax.set_xticklabels([x_labels[1]], fontsize=12)

# Randomly altered grid style
ax.grid(True, linestyle='-', alpha=0.3)  # Changed grid line style and transparency

plt.tight_layout()
plt.show()
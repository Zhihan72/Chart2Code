import matplotlib.pyplot as plt

all_sleep_quality_data = [
    [75, 78, 80, 82, 76, 79, 83, 85, 77, 81, 82, 79],
    [68, 70, 65, 72, 74, 66, 67, 71, 69, 73, 70, 68],
    [55, 57, 60, 58, 54, 56, 53, 59, 61, 55, 57, 60],
    [30, 32, 35, 33, 29, 31, 28, 34, 36, 30, 32, 35]
]

fig, ax = plt.subplots(figsize=(14, 8))
box = ax.boxplot(
    all_sleep_quality_data,
    patch_artist=True,
    notch=False,  # Removed notches
    vert=False,  
    widths=0.4  # Changed the width
)

single_color = 'lightgrey'
for patch in box['boxes']:
    patch.set_facecolor(single_color)

plt.setp(box['medians'], color='red', linewidth=1.5)  # Changed median line properties
plt.setp(box['whiskers'], color='green', linewidth=2, linestyle='--')  # Changed whisker style
plt.setp(box['caps'], color='purple', linewidth=2)  # Changed cap style
plt.setp(box['fliers'], marker='x', color='orange', alpha=0.7)  # Changed outlier marker and color

ax.grid(axis='y', linestyle=':', alpha=0.9)  # Altered grid orientation and style

# Drawing a border for the plot
for spine in ax.spines.values():
    spine.set_edgecolor('blue')
    spine.set_linewidth(1.5)

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt

ingr = ['Dragon', 'Unicorn', 'Mandrake', 'Elven']
potencies = [
    [50, 55, 53, 52, 51, 56, 54, 58, 52, 59],
    [75, 78, 77, 80, 79, 76, 81, 82, 83, 78],
    [40, 42, 41, 43, 39, 44, 40, 45, 42, 41],
    [90, 95, 92, 93, 91, 96, 94, 97, 93, 95]
]
avg_potencies = [54, 79, 43, 92]
colors = ['lightcoral', 'lightpink', 'lightgreen', 'lightblue']

fig, ax = plt.subplots(figsize=(12, 8))

# Change the boxplot to horizontal by setting vert=False
boxes = ax.boxplot(potencies, patch_artist=True, notch=True, vert=False, showmeans=True)

for patch, color in zip(boxes['boxes'], colors):
    patch.set_facecolor(color)

# Adjusting the average potencies line plot to align horizontally with boxplots
ax.plot(avg_potencies, range(1, len(avg_potencies) + 1), 
        marker='s', linestyle='-', color='darkred', linewidth=2)

# Set yticks for ingredient names as we changed the axis orientation
ax.set_yticks(range(1, len(ingr) + 1))
ax.set_yticklabels(ingr, fontsize=10, rotation=0, ha='right')

plt.tight_layout()
plt.show()
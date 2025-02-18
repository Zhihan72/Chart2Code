import matplotlib.pyplot as plt

workspaces = ['AI-Assist', 'Nature', 'Floating', 'Pods', 'VR Office']

break_durations = [
    [10, 22, 25, 18, 20, 15, 19, 30, 50, 45],
    [65, 58, 60, 48, 55, 70, 52, 45, 63, 50],
    [72, 85, 60, 68, 70, 65, 58, 55, 62, 80],
    [45, 40, 32, 30, 25, 55, 35, 48, 60, 42],
    [18, 15, 23, 12, 20, 19, 22, 10, 25, 18],
]

fig, ax = plt.subplots(figsize=(12, 6))

# Shuffled colors manually
colors = ['#FFD700', '#FFCC99', '#66B3FF', '#99FF99', '#FF9999']

ax.boxplot(break_durations, vert=False, patch_artist=True, labels=workspaces, notch=True, 
           medianprops=dict(linestyle='--', linewidth=2.5, color='purple'))

for patch, color in zip(ax.artists, colors):
    patch.set_facecolor(color)

ax.xaxis.grid(True, linestyle='-.', which='major', color='blue', alpha=0.5)

plt.title('Future Workspaces:\nBreaks in 2050', fontsize=14, fontweight='bold', color='midnightblue')
plt.xlabel('Break (min)', fontsize=12, fontweight='bold')
plt.ylabel('Spaces', fontsize=12, fontweight='bold')

annotations = ["Wellness", "Nature", "Immersion", "Quick", "Tiny"]
for i, annotation in enumerate(annotations):
    ax.text(max(break_durations[i]) + 3, i + 1, annotation, va='center', ha='right', fontsize=10, color='darkgreen')

plt.tight_layout()
plt.show()
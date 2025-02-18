import matplotlib.pyplot as plt

workspaces = ['Co-working Pods', 'VR Offices', 'Nature-Integrated', 'AI-Assisted', 'Floating Hubs']

break_durations = [
    [15, 20, 22, 19, 30, 45, 50, 20, 18, 25],
    [30, 25, 32, 35, 40, 60, 55, 45, 42, 48],
    [60, 55, 58, 62, 65, 80, 85, 70, 68, 72],
    [10, 12, 15, 18, 20, 22, 25, 18, 19, 23],
    [45, 50, 52, 48, 55, 65, 70, 58, 60, 63],
]

fig, ax = plt.subplots(figsize=(12, 6))
ax.boxplot(break_durations, vert=False, patch_artist=True, labels=workspaces, notch=True)

colors = ['#66B3FF', '#FFCC99', '#FFD700', '#FF9999', '#99FF99']  # Changed order of colors
for patch, color in zip(ax.artists, colors):
    patch.set_facecolor(color)

# Alter grid style
ax.xaxis.grid(True, linestyle='-.', which='major', color='blue', alpha=0.5)

plt.title('Futuristic Work Environments:\nDaily Break Durations in 2050', fontsize=14, fontweight='bold', color='midnightblue')
plt.xlabel('Break Duration (minutes)', fontsize=12, fontweight='bold')
plt.ylabel('Workspaces', fontsize=12, fontweight='bold')

# Alter annotations
annotations = ["Quick Rest", "Immersion Time", "Nature Time", "Tiny Breaks", "Wellness Time"]
for i, annotation in enumerate(annotations):
    ax.text(max(break_durations[i]) + 3, i + 1, annotation, va='center', ha='right', fontsize=10, color='darkgreen')

# Change marker of median line
medianprops = dict(linestyle='--', linewidth=2.5, color='purple')
ax.boxplot(break_durations, vert=False, patch_artist=True, labels=workspaces, notch=True, medianprops=medianprops)

plt.tight_layout()
plt.show()
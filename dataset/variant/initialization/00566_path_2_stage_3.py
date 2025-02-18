import matplotlib.pyplot as plt

workspaces = ['AI-Assisted', 'Nature-Integrated', 'Floating Hubs', 'Co-working Pods', 'VR Offices']

break_durations = [
    [10, 22, 25, 18, 20, 15, 19, 30, 50, 45],
    [65, 58, 60, 48, 55, 70, 52, 45, 63, 50],
    [72, 85, 60, 68, 70, 65, 58, 55, 62, 80],
    [45, 40, 32, 30, 25, 55, 35, 48, 60, 42],
    [18, 15, 23, 12, 20, 19, 22, 10, 25, 18],
]

fig, ax = plt.subplots(figsize=(12, 6))
ax.boxplot(break_durations, vert=False, patch_artist=True, labels=workspaces, notch=True)

colors = ['#FFCC99', '#FFD700', '#99FF99', '#66B3FF', '#FF9999']
for patch, color in zip(ax.artists, colors):
    patch.set_facecolor(color)

ax.xaxis.grid(True, linestyle='-.', which='major', color='blue', alpha=0.5)

plt.title('Futuristic Work Environments:\nDaily Break Durations in 2050', fontsize=14, fontweight='bold', color='midnightblue')
plt.xlabel('Break Duration (minutes)', fontsize=12, fontweight='bold')
plt.ylabel('Workspaces', fontsize=12, fontweight='bold')

annotations = ["Wellness Time", "Nature Time", "Immersion Time", "Quick Rest", "Tiny Breaks"]
for i, annotation in enumerate(annotations):
    ax.text(max(break_durations[i]) + 3, i + 1, annotation, va='center', ha='right', fontsize=10, color='darkgreen')

medianprops = dict(linestyle='--', linewidth=2.5, color='purple')
ax.boxplot(break_durations, vert=False, patch_artist=True, labels=workspaces, notch=True, medianprops=medianprops)

plt.tight_layout()
plt.show()
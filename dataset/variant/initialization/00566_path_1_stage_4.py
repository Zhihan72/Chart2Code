import matplotlib.pyplot as plt

workspaces = ['Co-working Pods', 'VR Offices', 'Nature-Integrated', 'AI-Assisted', 'Floating Hubs', 'Holographic Lounges', 'Digital Zen Gardens']
break_durations = [
    [15, 20, 22, 19, 30, 45, 50, 20, 18, 25],  # Co-working Pods
    [30, 25, 32, 35, 40, 60, 55, 45, 42, 48],  # VR Offices
    [60, 55, 58, 62, 65, 80, 85, 70, 68, 72],  # Nature-Integrated
    [10, 12, 15, 18, 20, 22, 25, 18, 19, 23],  # AI-Assisted
    [45, 50, 52, 48, 55, 65, 70, 58, 60, 63],  # Floating Hubs
    [25, 28, 30, 32, 29, 35, 38, 27, 31, 33],  # Holographic Lounges
    [50, 55, 58, 53, 60, 65, 70, 59, 62, 68],  # Digital Zen Gardens
]

fig, ax = plt.subplots(figsize=(14, 6))
boxprops = dict(facecolor="#FFD700", color="#FFD700", linewidth=1)
medianprops = dict(linestyle=':', linewidth=3, color='purple')
ax.boxplot(break_durations, vert=False, patch_artist=True, labels=workspaces, notch=False, boxprops=boxprops, medianprops=medianprops)

ax.xaxis.grid(True, linestyle='-', which='major', color='red', alpha=0.5)
ax.yaxis.grid(True, linestyle='-.', which='major', color='blue', alpha=0.3)

plt.title('Futuristic Work Environments:\nBreak Durations in 2050', fontsize=16, fontweight='normal', color='blue')
plt.xlabel('Break Duration (minutes)', fontsize=13, fontweight='normal')
plt.ylabel('Workspaces', fontsize=13, fontweight='normal')

annotations = ["Short", "Immersive", "Long", "Micro", "Balanced", "Moderate", "Relaxing"]
for i, annotation in enumerate(annotations):
    ax.text(max(break_durations[i]) + 3, i + 1, annotation, ha='right', va='center', fontsize=8, color='green')

plt.tight_layout()
plt.show()
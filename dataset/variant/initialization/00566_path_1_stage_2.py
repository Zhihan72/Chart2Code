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
boxprops = dict(facecolor="#66B3FF", color="#66B3FF", linewidth=2)
medianprops = dict(linestyle='-', linewidth=2.5, color='darkred')
ax.boxplot(break_durations, vert=True, patch_artist=True, labels=workspaces, notch=True, boxprops=boxprops, medianprops=medianprops)

ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

plt.title('Futuristic Work Environments:\nDaily Break Durations in 2050', fontsize=14, fontweight='bold', color='darkslategray')
plt.xlabel('Workspaces', fontsize=12, fontweight='bold')
plt.ylabel('Break Duration (minutes)', fontsize=12, fontweight='bold')

annotations = ["Short breaks", "Immersive breaks", "Long nature breaks", "Micro-breaks", 
               "Balanced breaks", "Moderate breaks", "Relaxing breaks"]
for i, annotation in enumerate(annotations):
    ax.text(i + 1, max(break_durations[i]) + 3, annotation, ha='center', va='bottom', fontsize=10, color='navy')

plt.tight_layout()
plt.show()
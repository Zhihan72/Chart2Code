import matplotlib.pyplot as plt

group_1 = [12, 14, 15, 13, 18, 16, 17, 14, 12, 15, 13, 17]
group_2 = [25, 28, 30, 27, 22, 20, 24, 29, 26, 23, 28, 26]
group_3 = [5, 6, 7, 8, 7, 6, 5, 9, 10, 8, 9, 11]

plt.figure(figsize=(8, 6))
plt.boxplot([group_1, group_2, group_3], vert=True, patch_artist=True,
            boxprops=dict(facecolor='lightblue', color='purple', linewidth=2),
            whiskerprops=dict(color='purple', linewidth=2),
            capprops=dict(color='purple', linewidth=2),
            medianprops=dict(color='darkgreen', linewidth=2, linestyle='--'),
            flierprops=dict(marker='s', color='red', markersize=8),
            notch=True)

plt.title('Star Link: Messaging Delays by Cluster', fontsize=14, fontweight='bold')
plt.ylabel('Time Delay (mins)', fontsize=12)
plt.xticks(ticks=[1, 2, 3], labels=['Alpha', 'Beta', 'Gamma'], fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='both', linestyle='-.', alpha=0.6)

plt.tight_layout()
plt.show()
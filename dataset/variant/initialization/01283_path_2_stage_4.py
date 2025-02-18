import matplotlib.pyplot as plt

# Data representing communication latency times (in minutes) for different groups
group_1 = [12, 14, 15, 13, 18, 16, 17, 14, 12, 15, 13, 17]
group_2 = [25, 28, 30, 27, 22, 20, 24, 29, 26, 23, 28, 26]
group_3 = [5, 6, 7, 8, 7, 6, 5, 9, 10, 8, 9, 11]

# Plotting a vertical box plot with shuffled colors
plt.figure(figsize=(8, 8))
plt.boxplot([group_1, group_2, group_3], vert=True, patch_artist=True,
            boxprops=dict(facecolor='orange', color='firebrick', linewidth=1.5),
            whiskerprops=dict(color='firebrick', linewidth=1.5),
            capprops=dict(color='firebrick', linewidth=1.5),
            medianprops=dict(color='navy', linewidth=2),
            flierprops=dict(marker='o', color='skyblue', markersize=6),
            notch=True)

plt.title('Star Link: Messaging Delays by Cluster', fontsize=14, fontweight='bold', pad=20)
plt.ylabel('Time Delay (mins)', fontsize=12)
plt.xticks(ticks=[1, 2, 3], labels=['Alpha', 'Beta', 'Gamma'], fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
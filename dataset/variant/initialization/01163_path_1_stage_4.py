import matplotlib.pyplot as plt

# Data for fuel consumption (liters per 100km) for selected vehicle types from 2000 to 2020
sedans = [9.5, 9.2, 8.9, 8.7, 8.5, 8.3, 8.0, 7.8, 7.6, 7.4, 7.2, 7.0, 6.8, 6.5, 6.3, 6.1, 5.9, 5.7, 5.5, 5.3, 5.0]
suvs = [14.0, 13.8, 13.5, 13.2, 12.8, 12.5, 12.2, 11.8, 11.5, 11.2, 10.8, 10.5, 10.2, 9.8, 9.5, 9.2, 8.9, 8.6, 8.3, 8.0, 7.7]

data = [sedans, suvs]
labels = ['World', 'Electric']

fig, ax = plt.subplots(figsize=(8, 6))

# Applying a single color (e.g., 'lightblue') to all data groups
color = 'lightblue'
box = ax.boxplot(data, vert=True, patch_artist=True, notch=False,
                 boxprops=dict(facecolor=color, color='navy'),
                 whiskerprops=dict(color='navy'),
                 capprops=dict(color='navy'),
                 medianprops=dict(color='darkorange', linewidth=2),
                 flierprops=dict(markerfacecolor='red', marker='o', markersize=8, linestyle='none'))

# Title and labels
ax.set_title("Chart of Energetics in Transit\n(2000CE-20th Year)", fontsize=16, fontweight='bold')
ax.set_ylabel("Energy Expenditure (Liters Every 100km)", fontsize=12)
ax.set_xticks(ticks=[1, 2])
ax.set_xticklabels(labels, fontsize=11)

ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
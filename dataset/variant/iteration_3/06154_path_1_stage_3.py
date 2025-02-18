import matplotlib.pyplot as plt

# Constructing the grouped data for screen time
screen_time_data = [
    [120, 130, 110, 115, 145, 150, 100, 105, 140, 125],  # 6-12
    [200, 220, 210, 190, 180, 230, 240, 250, 225, 235],  # 13-18
    [180, 175, 200, 220, 210, 195, 205, 210, 215, 220],  # 19-25
    [150, 160, 175, 180, 185, 160, 170, 175, 160, 190],  # 26-40
    [90, 100, 95, 85, 80, 105, 110, 95, 100, 90],        # 41-60
    [60, 70, 55, 50, 65, 60, 75, 80, 70, 55]             # 60+
]

fig, ax = plt.subplots(figsize=(14, 8))

# Create the vertical boxplot with dotted edges and cross markers for fliers
box = ax.boxplot(screen_time_data, vert=True, patch_artist=True, flierprops=dict(marker='x', color='red'))

# Customizing box colors with borders
colors = ['#ffebcd', '#ff7f50', '#7b68ee', '#32cd32', '#da70d6', '#ffa07a']
for patch, color in zip(box['boxes'], colors):
    patch.set(facecolor=color, linestyle=':', linewidth=2)

# Adding a legend with different labels
ax.legend(['6-12', '13-18', '19-25', '26-40', '41-60', '60+'], loc='upper right', fontsize=12)

# Adjusting title and labels
ax.set_title('Monthly Screen Time by Age', fontsize=18, pad=15)
ax.set_ylabel('Hours/Month', fontsize=14)
ax.set_xticklabels(['6-12', '13-18', '19-25', '26-40', '41-60', '60+'], fontsize=12)
ax.set_xlabel('Age Groups', fontsize=14)

# Add horizontal dotted grid lines
ax.xaxis.grid(True, linestyle=':', color='gray', alpha=0.5)

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
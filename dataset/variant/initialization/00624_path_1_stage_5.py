import matplotlib.pyplot as plt

# Single data group for the box plot
efficiency_data = [
    [90, 75, 78, 80, 82, 93, 95, 77, 88, 85, 68, 70, 75, 66, 60, 69, 71, 73, 72, 74, 84, 85, 92, 87, 91, 89, 86, 88, 90, 85, 
     63, 56, 62, 60, 57, 58, 61, 55, 64, 59, 75, 72, 71, 73, 76, 80, 78, 70, 77, 74]
]

fig, ax = plt.subplots(figsize=(6, 8))

# Plotting a single vertical box plot
bp = ax.boxplot(efficiency_data, vert=True, patch_artist=True, notch=False)

# Customizing the box
for patch in bp['boxes']:
    patch.set(facecolor='#FF5733', alpha=0.6)

# Customizing whiskers, caps, median lines
for whisker in bp['whiskers']:
    whisker.set(color='#2C3E50', linewidth=2)

for cap in bp['caps']:
    cap.set(color='#2C3E50', linewidth=2)

for median in bp['medians']:
    median.set(color='green', linewidth=3)

ax.set_ylabel('Efficiency Score (%)', fontsize=13)
ax.set_xticklabels(['Combined Energy Sources'], fontsize=12)

ax.set_ylim(50, 100)

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt

# Data for the box plot
solar_energy = [50, 55, 60, 65, 70, 72, 74, 76, 78, 80, 85]
data = [solar_energy]

fig, ax = plt.subplots(figsize=(8, 6))
ax.boxplot(data, vert=True, patch_artist=True,
           boxprops=dict(facecolor='lightblue', color='blue'),
           whiskerprops=dict(color='blue'),
           capprops=dict(color='blue'),
           medianprops=dict(color='red', linewidth=2),
           flierprops=dict(markerfacecolor='red', marker='o', markersize=5, linestyle='none'))

# Shortened title and labels
plt.title("Solar Efficiency", fontsize=14, fontweight='bold', pad=20)
plt.xlabel("Source", fontsize=12)
plt.ylabel("Production (GW)", fontsize=12)
plt.xticks([1], ['Solar'])

# Display the plot
plt.show()
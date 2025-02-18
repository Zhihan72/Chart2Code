import matplotlib.pyplot as plt

water_quality_data = {
    'Metropolis Alpha': [75, 80, 85, 77, 82, 79, 81, 83, 85, 84, 81, 78, 80, 79, 83, 86, 88, 89, 90, 76, 78, 79, 81, 83, 84, 80, 82, 83, 85, 87],
    'Urban Zone Beta': [65, 68, 70, 72, 74, 69, 71, 75, 77, 79, 80, 81, 75, 74, 73, 78, 76, 77, 80, 82, 81, 79, 78, 76, 75, 74, 77, 78, 79, 80],
    'Central District Gamma': [90, 92, 93, 94, 89, 87, 88, 86, 85, 84, 83, 90, 89, 88, 87, 86, 85, 84, 83, 90, 89, 88, 87, 86, 85, 83, 81, 82, 80, 79],
    'Water Source Delta': [55, 58, 60, 62, 64, 59, 61, 63, 65, 67, 66, 68, 63, 62, 61, 64, 63, 65, 66, 68, 67, 69, 70, 65, 61, 62, 63, 64, 65, 66],
    'Reservoir Epsilon': [82, 84, 85, 86, 89, 87, 88, 86, 85, 87, 90, 92, 89, 88, 86, 84, 83, 85, 87, 89, 90, 88, 87, 86, 85, 84, 83, 82, 80, 81]
}

city_names = list(water_quality_data.keys())
quality_values = list(water_quality_data.values())

fig, ax = plt.subplots(figsize=(12, 8))

boxplot = ax.boxplot(quality_values, vert=True, patch_artist=True, notch=True, labels=city_names)

new_colors = ['#8B0000', '#FFD700', '#00FA9A', '#1E90FF', '#8A2BE2']
for patch, color in zip(boxplot['boxes'], new_colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.5)

plt.setp(boxplot['whiskers'], color='gray', linestyle='--')
plt.setp(boxplot['caps'], color='gray')
plt.setp(boxplot['medians'], color='black')

ax.set_title("Aquatic Purity Assessment of Urban Water Sources\n Spanning a 30-Day Period", fontsize=16, fontweight='bold')
ax.set_ylabel("Purity Index (0-100)", fontsize=14)
ax.set_xlabel("Geographic Sectors", fontsize=14)

ax.annotate('Peak Purity Achieved', xy=(3, 94), xytext=(2.5, 96),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=12, fontweight='bold', color='black')

plt.tight_layout()
plt.show()
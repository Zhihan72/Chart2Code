import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)
coniferous_forest = [200, 220, 250, 270, 300, 320, 350, 360, 320, 305, 280, 250, 240, 230, 240, 245, 255, 270, 280, 290, 310]
deciduous_forest = [150, 160, 170, 180, 190, 200, 210, 215, 220, 230, 235, 240, 245, 250, 240, 235, 225, 220, 210, 200, 190]
mixed_forest = [100, 110, 120, 130, 140, 150, 160, 165, 170, 180, 190, 195, 200, 205, 210, 220, 225, 230, 235, 240, 245]
tropical_forest = [250, 260, 270, 280, 290, 300, 310, 320, 325, 330, 335, 340, 345, 350, 355, 360, 365, 370, 375, 380, 385]
savanna_forest = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150]

burnt_area_data = np.vstack([coniferous_forest, deciduous_forest, mixed_forest, tropical_forest, savanna_forest])

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#FF6347', '#8B4513', '#808000', '#228B22', '#FFD700']

ax.stackplot(years, burnt_area_data, labels=['Savanna', 'Mixed', 'Deciduous', 'Coniferous', 'Tropical'], colors=colors, alpha=0.8)

marker_styles = ['v', '^', 'o', 's', 'd']
line_styles = ['-', '--', '-.', ':', '-']
for forest, color, marker, line in zip(burnt_area_data, colors, marker_styles, line_styles):
    ax.plot(years, forest, color=color, marker=marker, linestyle=line, linewidth=1.5)

ax.set_title("Impact of Wildfires on Various Forest Types Over Two Decades\n(Burnt Area in Thousand Hectares)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Burnt Area (Thousands of Hectares)", fontsize=12)
ax.grid(linestyle=':', alpha=0.7)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 1601, 200))

significant_years = [2000 + np.argmax(forest) for forest in burnt_area_data]
significant_values = [max(forest) for forest in burnt_area_data]

forest_labels = ['Savanna', 'Mixed', 'Deciduous', 'Coniferous', 'Tropical']
for year, value, label, color in zip(significant_years, significant_values, forest_labels, colors):
    ax.annotate(f'{value}k Ha', xy=(year, value), xytext=(-30, 10),
                textcoords='offset points', fontsize=10,
                arrowprops=dict(facecolor=color, arrowstyle="wedge", alpha=0.5),
                bbox=dict(facecolor='white', edgecolor=color, boxstyle='round,pad=0.3'))

custom_legend = [plt.Line2D([0], [0], color=color, marker=marker, lw=2) for color, marker in zip(colors, marker_styles)]
ax.legend(custom_legend, forest_labels, loc='lower left', fontsize=10, title="Forest Types")

plt.tight_layout()
plt.show()
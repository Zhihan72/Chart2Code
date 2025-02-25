import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

# Manually altered data while keeping the same structure
coniferous_forest = [310, 290, 280, 270, 255, 245, 240, 230, 240, 250, 280, 305, 320, 360, 350, 320, 300, 270, 250, 220, 200]
deciduous_forest = [190, 200, 210, 220, 225, 235, 240, 250, 245, 240, 235, 230, 220, 215, 210, 200, 190, 180, 170, 160, 150]
mixed_forest = [245, 240, 235, 230, 225, 220, 210, 205, 200, 195, 190, 180, 170, 165, 160, 150, 140, 130, 120, 110, 100]
tropical_forest = [385, 380, 375, 370, 365, 360, 355, 350, 345, 340, 335, 330, 325, 320, 310, 300, 290, 280, 270, 260, 250]

burnt_area_data = np.vstack([coniferous_forest, deciduous_forest, mixed_forest, tropical_forest])

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#FFD700', '#FF6347', '#8B4513', '#228B22']

ax.stackplot(years, burnt_area_data, labels=['Coniferous Forest', 'Deciduous Forest', 'Mixed Forest', 'Tropical Forest'], 
             colors=colors, alpha=0.8)

marker_types = ['o', 's', 'D', '^']
line_styles = ['-', '--', '-.', ':']

for forest, color, marker, lstyle in zip(burnt_area_data, colors, marker_types, line_styles):
    ax.plot(years, forest, color=color, linewidth=1.5, linestyle=lstyle, marker=marker)

ax.set_title("Impact of Wildfires on Different Types of Forests\n(Burnt Area in Thousand Hectares)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Burnt Area (Thousands of Hectares)", fontsize=12)

ax.grid(visible=False)

plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 1601, 200))

significant_years = [2000 + np.argmax(forest) for forest in burnt_area_data]
significant_values = [max(forest) for forest in burnt_area_data]

for year, value, label, color in zip(significant_years, significant_values, ['Coniferous Forest', 'Deciduous Forest', 'Mixed Forest', 'Tropical Forest'], colors):
    ax.annotate(f'{value}k Ha', xy=(year, value), xytext=(3, 10),
                 textcoords='offset points', fontsize=10,
                 arrowprops=dict(facecolor=color, shrink=0.05),
                 bbox=dict(facecolor='white', edgecolor=color, boxstyle='round,pad=0.3'))

custom_legend = [plt.Line2D([0], [0], color=color, marker=marker, lw=4) for color, marker in zip(colors, marker_types)]
ax.legend(custom_legend, ['Coniferous Forest', 'Deciduous Forest', 'Mixed Forest', 'Tropical Forest'], loc='upper right', fontsize=10, title="Forest Types", frameon=False)

plt.tight_layout()
plt.show()
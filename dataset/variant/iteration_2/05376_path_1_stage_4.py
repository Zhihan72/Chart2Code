import matplotlib.pyplot as plt
import numpy as np

brightness = [5.6, 4.2, 7.1, 6.3, 8.4, 3.8, 5.0, 7.5]
num_planets = [3, 5, 7, 4, 10, 2, 6, 8]

star_names = [
    'Alpha Eridani', 
    'Beta Hydri', 
    'Gamma Centauri', 
    'Delta Orionis', 
    'Epsilon Pegasi', 
    'Zeta Reticuli',
    'Eta Cassiopeiae',   
    'Theta Eridani'      
]

fig, ax = plt.subplots(figsize=(10, 6))

y_positions = np.arange(len(star_names))

bars = ax.barh(y_positions, brightness, color='blue', edgecolor='black')

# Annotate the bars with star names
for i, bar in enumerate(bars):
    ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2, star_names[i], 
            va='center', ha='left', fontsize=8, color='purple')

# Map the num_planets value to colors
bar_colors = plt.cm.cool([val/10 for val in num_planets])
for bar, color in zip(bars, bar_colors):
    bar.set_color(color)

cbar = plt.colorbar(plt.cm.ScalarMappable(cmap='cool'), ax=ax, boundaries=np.linspace(1, 10, 10))
cbar.set_label('Number of Planets', color='blue')

plt.title("Galactic Star Systems\nBrightness by Star", fontsize=14, fontweight='bold')
plt.xlabel("Brightness", fontsize=11, color='darkgreen')
ax.set_yticks(y_positions)
ax.set_yticklabels(star_names)

plt.tight_layout()
plt.show()
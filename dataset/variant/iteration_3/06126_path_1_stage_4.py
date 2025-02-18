import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Data for water quality scores with manually shuffled scores
water_quality_data = {
    'A': [77, 88, 82, 79, 81, 80, 85, 89, 81, 76, 80, 79, 83, 83, 78, 86, 82, 85, 90, 75, 81, 83, 79, 84, 78, 83, 87, 84, 79, 81],
    'B': [75, 70, 72, 74, 78, 79, 77, 81, 80, 82, 68, 76, 71, 75, 77, 73, 69, 80, 65, 74, 79, 78, 82, 74, 65, 68, 76, 81, 72, 77],
    'C': [85, 88, 83, 93, 82, 80, 84, 83, 89, 89, 94, 92, 84, 83, 86, 86, 87, 90, 87, 88, 88, 87, 85, 79, 81, 90, 90, 92, 89, 86],
    'D': [66, 61, 62, 63, 62, 55, 58, 60, 70, 68, 64, 67, 65, 59, 63, 61, 66, 62, 65, 61, 64, 66, 63, 69, 63, 64, 62, 67, 68, 65],
    'E': [81, 85, 89, 88, 87, 86, 87, 86, 88, 84, 86, 87, 85, 82, 83, 80, 85, 84, 89, 90, 90, 84, 92, 88, 81, 83, 87, 86, 82, 85]
}

city_names = list(water_quality_data.keys())
quality_values = list(water_quality_data.values())

fig, ax = plt.subplots(figsize=(12, 8))
boxplot = ax.boxplot(quality_values, vert=False, patch_artist=True, notch=True, labels=city_names)

colors = ['#779ecb', '#ffb347', '#77dd77', '#ff6961', '#fdfd96']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.5)

plt.setp(boxplot['whiskers'], color='gray', linestyle='--')
plt.setp(boxplot['caps'], color='gray')
plt.setp(boxplot['medians'], color='black')

ax.set_title("Water Quality in Cities", fontsize=16, fontweight='bold')
ax.set_xlabel("Score", fontsize=14)
ax.set_ylabel("Cities", fontsize=14)

ax.xaxis.grid(True, linestyle='--', alpha=0.7)

ax.annotate('Highest Quality', xy=(94, 3), xytext=(96, 2.5),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=12, fontweight='bold', color='black')

legend_elements = [Patch(facecolor=color, label=city) for color, city in zip(colors, city_names)]
ax.legend(handles=legend_elements, title='Cities', loc='upper right')

plt.tight_layout()
plt.show()
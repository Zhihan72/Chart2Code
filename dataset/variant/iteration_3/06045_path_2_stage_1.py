import matplotlib.pyplot as plt
import numpy as np

# Monthly running distance data (in km) for each type of athlete with random alterations
amateur_distances = [45, 30, 55, 60, 35, 50, 40, 50, 45, 60, 50, 55]
semi_pro_distances = [90, 80, 70, 95, 85, 75, 80, 90, 85, 85, 95, 90]
professional_distances = [120, 115, 100, 125, 110, 120, 115, 105, 125, 110, 115, 120]
marathoner_distances = [230, 210, 220, 230, 205, 210, 220, 215, 230, 220, 220, 230]
sprinter_distances = [75, 70, 60, 85, 80, 65, 75, 85, 80, 75, 70, 80]

all_distances = [
    amateur_distances,
    semi_pro_distances,
    professional_distances,
    marathoner_distances,
    sprinter_distances
]

athlete_labels = ["Amateur", "Semi-Professional", "Professional", "Marathoner", "Sprinter"]

fig, ax = plt.subplots(figsize=(14, 9))
box = ax.boxplot(all_distances, labels=athlete_labels, patch_artist=True, notch=True, vert=True, showmeans=True)

colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#CC99FF']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

ax.set_title("Monthly Running Distances by Different Athletes:\nA One-Year Analysis", fontsize=18, fontweight='bold')
ax.set_xlabel("Types of Athletes", fontsize=14)
ax.set_ylabel("Running Distance (km)", fontsize=14)
ax.grid(axis='y', linestyle='--', alpha=0.7)

for element in ['whiskers', 'caps', 'medians', 'means']:
    plt.setp(box[element], color='black')
plt.setp(box['fliers'], marker='o', color='red', markersize=5, alpha=0.5)

labels = ["Box: Distance Range", "Line inside box: Median", "Diamond: Mean"]
handles = [plt.Line2D([0], [0], color='black', lw=2),
           plt.Line2D([0], [0], marker='D', color='yellow', markersize=10, linestyle='', markerfacecolor='yellow')]
ax.legend(handles, labels, loc='upper left', frameon=False, fontsize=12)

plt.tight_layout()
plt.show()
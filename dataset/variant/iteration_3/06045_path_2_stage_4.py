import matplotlib.pyplot as plt

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
box = ax.boxplot(all_distances, labels=athlete_labels, patch_artist=True, notch=True, vert=False, showmeans=False)

# New set of colors
colors = ['#FFA07A', '#20B2AA', '#87CEFA', '#9370DB', '#3CB371']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

ax.set_ylabel("Types of Athletes", fontsize=14)
ax.set_xlabel("Running Distance (km)", fontsize=14)

plt.tight_layout()
plt.show()
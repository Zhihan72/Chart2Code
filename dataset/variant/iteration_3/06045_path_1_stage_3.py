import matplotlib.pyplot as plt

# Monthly running distance data (in km) for each type of athlete
amateur_distances = [30, 45, 50, 60, 35, 40, 50, 55, 45, 50, 60, 55]
semi_pro_distances = [70, 80, 85, 90, 75, 80, 85, 95, 90, 85, 90, 95]
professional_distances = [100, 110, 115, 120, 105, 110, 115, 125, 120, 115, 120, 125]
marathoner_distances = [200, 210, 220, 230, 205, 210, 220, 230, 220, 215, 220, 230]
sprinter_distances = [60, 70, 75, 80, 65, 70, 75, 85, 80, 75, 80, 85]

all_distances = [
    amateur_distances,
    semi_pro_distances,
    professional_distances,
    marathoner_distances,
    sprinter_distances
]

athlete_labels = ["Beginner", "Intermediate", "Expert", "Endurance", "Speedster"]

fig, ax = plt.subplots(figsize=(14, 9))

box = ax.boxplot(all_distances, labels=athlete_labels, patch_artist=True, notch=True, vert=True, showmeans=True)

# New set of colors
colors = ['#FF6666', '#FFB266', '#FFFF66', '#66FF66', '#66B2FF']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

ax.set_xlabel("Athlete Categories", fontsize=14)
ax.set_ylabel("Distance Covered (km)", fontsize=14)

for element in ['whiskers', 'caps', 'medians', 'means']:
    plt.setp(box[element], color='black')
plt.setp(box['fliers'], marker='o', color='red', markersize=5, alpha=0.5)

plt.tight_layout()
plt.show()
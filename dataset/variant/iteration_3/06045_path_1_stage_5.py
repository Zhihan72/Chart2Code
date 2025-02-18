import matplotlib.pyplot as plt

amateur_distances = [45, 50, 30, 55, 40, 35, 60, 50, 50, 60, 45, 55]  # Shuffled entries
semi_pro_distances = [90, 85, 70, 95, 80, 75, 85, 80, 90, 95, 85, 90]  # Shuffled entries
professional_distances = [115, 110, 120, 100, 110, 125, 115, 105, 120, 125, 120, 115]  # Shuffled entries
marathoner_distances = [210, 230, 200, 215, 220, 230, 205, 230, 220, 220, 210, 220]  # Shuffled entries
sprinter_distances = [75, 80, 65, 70, 85, 60, 80, 70, 75, 75, 85, 80]  # Shuffled entries

all_distances = [
    amateur_distances,
    semi_pro_distances,
    professional_distances,
    marathoner_distances,
    sprinter_distances
]

athlete_labels = ["Beginner", "Intermediate", "Expert", "Endurance", "Speedster"]

fig, ax = plt.subplots(figsize=(14, 9))

box = ax.boxplot(all_distances, labels=athlete_labels, patch_artist=True, notch=True, vert=False, showmeans=True)

colors = ['#FF6666', '#FFB266', '#FFFF66', '#66FF66', '#66B2FF']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

ax.set_xlabel("Distance Covered (km)", fontsize=14)
ax.set_ylabel("Athlete Categories", fontsize=14)

for element in ['whiskers', 'caps', 'medians', 'means']:
    plt.setp(box[element], color='black')
plt.setp(box['fliers'], marker='o', color='red', markersize=5, alpha=0.5)

plt.tight_layout()
plt.show()
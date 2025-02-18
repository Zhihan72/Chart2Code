import matplotlib.pyplot as plt

small_families = [150, 160, 170, 155, 165, 180, 175, 160, 170, 165, 175, 190]
large_families = [300, 310, 320, 305, 315, 350, 345, 310, 330, 325, 340, 360]
single_adults = [100, 110, 115, 105, 120, 125, 110, 120, 115, 125, 130, 135]
student_households = [200, 210, 220, 205, 215, 230, 220, 210, 220, 215, 230, 240]
elderly_couples = [80, 85, 90, 82, 88, 95, 92, 85, 90, 88, 92, 97]

water_usage_data = [small_families, large_families, single_adults, student_households, elderly_couples]

fig, ax = plt.subplots(figsize=(12, 8))

# Remove group labels by omitting the 'labels' parameter
box = ax.boxplot(water_usage_data, vert=False, patch_artist=True, notch=False, whis=[10, 90])

colors = ['mistyrose', 'lightcyan', 'honeydew', 'lavender', 'palegoldenrod']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

for whisker, cap, median, flier in zip(box['whiskers'], box['caps'], box['medians'], box['fliers']):
    whisker.set(color='slateblue', linewidth=1, linestyle='-.')
    cap.set(color='slateblue', linewidth=1)
    median.set(color='darkgreen', linewidth=3)
    flier.set(marker='s', color='darkorange', alpha=0.7)

# Remove title and axis labels
ax.xaxis.grid(True, linestyle=':', color='darkgrey', alpha=0.5)

plt.tight_layout()

plt.show()
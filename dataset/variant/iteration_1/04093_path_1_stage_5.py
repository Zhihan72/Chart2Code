import matplotlib.pyplot as plt
import numpy as np

small_families = [150, 160, 170, 155, 165, 180, 175, 160, 170, 165, 175, 190]
single_adults = [100, 110, 115, 105, 120, 125, 110, 120, 115, 125, 130, 135]
student_households = [200, 210, 220, 205, 215, 230, 220, 210, 220, 215, 230, 240]
elderly_couples = [80, 85, 90, 82, 88, 95, 92, 85, 90, 88, 92, 97]

water_usage_data = [small_families, single_adults, student_households, elderly_couples]
household_types = ['Tiny Families', 'Lonely Adults', 'Dormitories', 'Senior Pairs']

fig, ax = plt.subplots(figsize=(12, 8))

box = ax.boxplot(water_usage_data, vert=False, patch_artist=True, labels=household_types, notch=False)

single_color = 'lightblue'
for patch in box['boxes']:
    patch.set_facecolor(single_color)

for whisker, cap, median, flier in zip(box['whiskers'], box['caps'], box['medians'], box['fliers']):
    whisker.set(color='black', linewidth=1, linestyle='-.')
    cap.set(color='black', linewidth=1)
    median.set(color='firebrick', linewidth=2.5)
    flier.set(marker='s', color='blue', alpha=0.8)

ax.set_title('Water Use: A Random Overview', fontsize=14, fontweight='normal')
ax.set_xlabel('H2O Use (Gallons)', fontsize=11)
ax.set_ylabel('Groups', fontsize=11)
ax.xaxis.grid(True, linestyle=':', color='black', alpha=0.9)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()
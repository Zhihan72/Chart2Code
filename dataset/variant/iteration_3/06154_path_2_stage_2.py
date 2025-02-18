import matplotlib.pyplot as plt

age_groups = [
    'Grade Schoolers', 'Teens', 'Young Adults', 
    'Mature Millennials', 'Boomers', 'Elders'
]

screen_time_6_12 = [120, 130, 110, 115, 145, 150, 100, 105, 140, 125]
screen_time_13_18 = [200, 220, 210, 190, 180, 230, 240, 250, 225, 235]
screen_time_19_25 = [180, 175, 200, 220, 210, 195, 205, 210, 215, 220]
screen_time_26_40 = [150, 160, 175, 180, 185, 160, 170, 175, 160, 190]
screen_time_41_60 = [90, 100, 95, 85, 80, 105, 110, 95, 100, 90]
screen_time_60_plus = [60, 70, 55, 50, 65, 60, 75, 80, 70, 55]

screen_time_data = [
    screen_time_6_12, screen_time_13_18, screen_time_19_25,
    screen_time_26_40, screen_time_41_60, screen_time_60_plus
]

fig, ax = plt.subplots(figsize=(14, 8))
box = ax.boxplot(screen_time_data, vert=False, patch_artist=True, notch=True, showmeans=True)

# Applying new contrasting colors
colors = ['#ff5733', '#33ff57', '#3357ff', '#ffff33', '#ff33ff', '#33ffff']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

for mean, median in zip(box['means'], box['medians']):
    mean.set(marker='D', color='blue', markersize=5)
    median.set(color='red', linewidth=2)

ax.set_title('Varied Digital Time Across Ages', fontsize=20, fontweight='bold', pad=20)
ax.set_xlabel('Time (Hours/Month)', fontsize=15)
ax.set_yticklabels(age_groups, fontsize=13)
ax.set_ylabel('Demographic Group', fontsize=15)
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
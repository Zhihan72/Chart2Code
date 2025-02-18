import matplotlib.pyplot as plt

all_sleep_quality_data = [
    [75, 78, 80, 82, 76, 79, 83, 85, 77, 81, 82, 79],
    [68, 70, 65, 72, 74, 66, 67, 71, 69, 73, 70, 68],
    [55, 57, 60, 58, 54, 56, 53, 59, 61, 55, 57, 60],
    [45, 47, 50, 48, 44, 46, 43, 49, 51, 45, 47, 50],
    [30, 32, 35, 33, 29, 31, 28, 34, 36, 30, 32, 35]
]

fig, ax = plt.subplots(figsize=(14, 8))
box = ax.boxplot(
    all_sleep_quality_data,
    patch_artist=True,
    notch=True,
    vert=True,
    widths=0.6
)

single_color = 'skyblue'
for patch in box['boxes']:
    patch.set_facecolor(single_color)

plt.setp(box['medians'], color='darkblue', linewidth=2)
plt.setp(box['whiskers'], color='gray', linewidth=1.5, linestyle='-')
plt.setp(box['caps'], color='grey', linewidth=1.5)
plt.setp(box['fliers'], marker='o', color='black', alpha=0.5)

ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
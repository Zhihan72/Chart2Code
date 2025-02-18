import matplotlib.pyplot as plt
import numpy as np

# Altered sleep quality index data while maintaining structure
neighborhood_a_sleep_quality = [79, 77, 82, 75, 83, 78, 81, 80, 79, 85, 76, 82]
neighborhood_b_sleep_quality = [70, 69, 73, 72, 67, 66, 68, 68, 70, 74, 71, 65]
neighborhood_c_sleep_quality = [59, 57, 54, 60, 53, 55, 56, 58, 61, 57, 55, 60]
neighborhood_d_sleep_quality = [47, 51, 50, 44, 43, 45, 46, 49, 45, 50, 48, 47]
neighborhood_e_sleep_quality = [32, 30, 29, 35, 36, 34, 31, 30, 33, 32, 35, 28]

all_sleep_quality_data = [
    neighborhood_a_sleep_quality,
    neighborhood_b_sleep_quality,
    neighborhood_c_sleep_quality,
    neighborhood_d_sleep_quality,
    neighborhood_e_sleep_quality
]

neighborhood_labels = ["Neighborhood A", "Neighborhood B", "Neighborhood C", "Neighborhood D", "Neighborhood E"]

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(14, 8))
box = ax.boxplot(
    all_sleep_quality_data,
    patch_artist=True,
    notch=True,
    vert=True,
    labels=neighborhood_labels,
    widths=0.6
)

colors = ['#FF6347', '#FFD700', '#32CD32', '#87CEFA', '#EE82EE']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.setp(box['medians'], color='darkblue', linewidth=2)
plt.setp(box['whiskers'], color='gray', linewidth=1.5, linestyle='-')
plt.setp(box['caps'], color='grey', linewidth=1.5)
plt.setp(box['fliers'], marker='o', color='black', alpha=0.5)

ax.set_title("Impact of City Noise Levels on Human Sleep Quality\nA Neighborhood Analysis", fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Neighborhood", fontsize=12)
ax.set_ylabel("Sleep Quality Index", fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

for label, color in zip(neighborhood_labels, colors):
    plt.plot([], [], color=color, label=label, linewidth=10)
plt.legend(title="Neighborhoods", loc='upper right')

plt.tight_layout()
plt.show()
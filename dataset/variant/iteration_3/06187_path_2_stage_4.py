import matplotlib.pyplot as plt
import numpy as np

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
    notch=False,
    vert=False,  # Change to horizontal box plot
    labels=neighborhood_labels,
    widths=0.6
)

colors = ['#1E90FF', '#FF1493', '#32CD32', '#FFD700', '#8A2BE2']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.setp(box['medians'], color='darkred', linewidth=3)
plt.setp(box['whiskers'], color='black', linewidth=2.5, linestyle='-.')
plt.setp(box['caps'], color='black', linewidth=2.5)
plt.setp(box['fliers'], marker='s', color='red', alpha=0.7)

ax.set_title("Impact of City Noise Levels on Human Sleep Quality\nA Neighborhood Analysis", fontsize=18, weight='bold', pad=25)
ax.set_xlabel("Sleep Quality Index", fontsize=14)  # Adjust labels
ax.set_ylabel("Neighborhood", fontsize=14)
ax.grid(axis='y', linestyle=':', alpha=0.5)  # Adjust grid for horizontal orientation

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

for label, color in zip(neighborhood_labels, colors):
    plt.plot([], [], color=color, label=label, linewidth=10)
plt.legend(title="Neighborhoods", loc='lower right')

plt.tight_layout()
plt.show()
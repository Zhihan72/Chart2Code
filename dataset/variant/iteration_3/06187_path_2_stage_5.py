import matplotlib.pyplot as plt

neighborhood_a = [79, 77, 82, 75, 83, 78, 81, 80, 79, 85, 76, 82]
neighborhood_b = [70, 69, 73, 72, 67, 66, 68, 68, 70, 74, 71, 65]
neighborhood_c = [59, 57, 54, 60, 53, 55, 56, 58, 61, 57, 55, 60]
neighborhood_d = [47, 51, 50, 44, 43, 45, 46, 49, 45, 50, 48, 47]
neighborhood_e = [32, 30, 29, 35, 36, 34, 31, 30, 33, 32, 35, 28]

all_data = [neighborhood_a, neighborhood_b, neighborhood_c, neighborhood_d, neighborhood_e]

labels = ["A", "B", "C", "D", "E"]

fig, ax = plt.subplots(figsize=(14, 8))
box = ax.boxplot(
    all_data,
    patch_artist=True,
    vert=False,
    labels=labels
)

colors = ['#1E90FF', '#FF1493', '#32CD32', '#FFD700', '#8A2BE2']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.setp(box['medians'], color='darkred', linewidth=3)
plt.setp(box['whiskers'], color='black', linewidth=2.5, linestyle='-.')
plt.setp(box['caps'], color='black', linewidth=2.5)
plt.setp(box['fliers'], marker='s', color='red', alpha=0.7)

ax.set_title("Noise Impact on Sleep", fontsize=18, weight='bold', pad=25)
ax.set_xlabel("Sleep Quality", fontsize=14)
ax.set_ylabel("Area", fontsize=14)
ax.grid(axis='y', linestyle=':', alpha=0.5)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

for label, color in zip(labels, colors):
    plt.plot([], [], color=color, label=label, linewidth=10)
plt.legend(title="Areas", loc='lower right')

plt.tight_layout()
plt.show()
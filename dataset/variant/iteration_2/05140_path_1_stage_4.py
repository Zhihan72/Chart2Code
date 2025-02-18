import matplotlib.pyplot as plt

# Altered data for the box plot (manually shuffled)
apple_yield = [38, 30, 35, 40, 32, 33, 34, 31, 36, 37]  # original: [30, 35, 40, 32, 33, 36, 38, 37, 34, 31]
orange_yield = [26, 21, 28, 22, 27, 23, 26, 25, 29, 24]  # original: [25, 28, 22, 26, 29, 24, 21, 27, 23, 26]
pear_yield = [13, 17, 15, 18, 15, 16, 16, 14, 19, 12]  # original: [15, 17, 13, 18, 16, 14, 19, 12, 16, 15]
cherry_yield = [12, 13, 10, 11, 13, 14, 9, 8, 7, 10]   # original: [10, 13, 9, 11, 14, 8, 7, 10, 12, 13]

data = [apple_yield, orange_yield, pear_yield, cherry_yield]

fig, ax = plt.subplots(figsize=(10, 6))
boxplot = ax.boxplot(data, vert=False, patch_artist=True, widths=0.6, notch=True)
colors = ['#FFD700', '#FF69B4', '#FF6347', '#90EE90']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)

for whisker in boxplot['whiskers']:
    whisker.set(color='#8B8B8B', linewidth=1.5, linestyle='--')
for cap in boxplot['caps']:
    cap.set(color='#8B8B8B', linewidth=1.5)
for median in boxplot['medians']:
    median.set(color='black', linewidth=2)

ax.xaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)
plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt

apple_yield = [38, 30, 35, 40, 32, 33, 34, 31, 36, 37]
orange_yield = [26, 21, 28, 22, 27, 23, 26, 25, 29, 24]
pear_yield = [13, 17, 15, 18, 15, 16, 16, 14, 19, 12]
cherry_yield = [12, 13, 10, 11, 13, 14, 9, 8, 7, 10]

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

plt.tight_layout()
plt.show()
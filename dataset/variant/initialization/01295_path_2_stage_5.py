import matplotlib.pyplot as plt

city1 = [1.2, 1.5, 1.3, 1.4, 1.6, 1.5, 1.7, 1.8, 1.6, 1.7]
city2 = [2.1, 2.3, 2.5, 2.2, 2.4, 2.6, 2.5, 2.7, 2.8, 2.6]
city3 = [1.7, 1.6, 1.9, 1.8, 2.0, 1.9, 2.1, 2.2, 1.8, 2.0]
city4 = [0.8, 1.0, 1.1, 1.2, 1.3, 1.1, 1.0, 1.2, 1.4, 1.3]
city5 = [3.2, 3.0, 3.3, 3.5, 3.6, 3.4, 3.5, 3.6, 3.7, 3.8]
city6 = [2.9, 3.1, 2.8, 3.2, 3.0, 3.5, 3.3, 3.4, 3.6, 3.5]  # New data series

all_data = [city1, city2, city3, city4, city5, city6]

fig, ax = plt.subplots(figsize=(8, 6))

box = ax.boxplot(all_data, vert=True, patch_artist=True, notch=True,
                 boxprops=dict(color='blue'),
                 whiskerprops=dict(color='blue'),
                 capprops=dict(color='blue'),
                 flierprops=dict(marker='o', color='magenta', markersize=8, alpha=0.5),
                 medianprops=dict(color='purple', linewidth=2))

colors = ['#FFB6C1', '#87CEEB', '#FFE4B5', '#98FB98', '#FFD700', '#FF6347']

for patch, color in zip(box['boxes'], colors):
    patch.set(facecolor=color, alpha=0.7)

ax.set_xticks(range(1, len(all_data) + 1))
ax.set_xticklabels(['City 1', 'City 2', 'City 3', 'City 4', 'City 5', 'City 6'])

plt.show()
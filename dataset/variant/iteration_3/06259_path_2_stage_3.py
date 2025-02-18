import matplotlib.pyplot as plt

cities = ['New York', 'London', 'Tokyo', 'Sydney', 'Cairo']

temperatures = [
    [5, 6, 8, 7, 6, 5, 7, 8, 9, 4, 5, 5, 6, 7, 8, 5, 6, 7, 10, 6, 7, 5, 8, 9],
    [7, 8, 10, 9, 8, 8, 9, 10, 11, 8, 9, 8, 10, 9, 8, 9, 10, 11, 10, 9, 8, 10, 9, 8],
    [12, 13, 12, 15, 13, 14, 13, 14, 15, 13, 14, 15, 13, 12, 14, 16, 13, 14, 15, 13, 14, 15, 13, 14],
    [18, 20, 19, 21, 22, 18, 20, 17, 20, 21, 19, 17, 18, 19, 20, 18, 19, 17, 20, 19, 21, 17, 18, 20],
    [23, 25, 22, 24, 23, 25, 24, 23, 24, 25, 22, 24, 23, 24, 22, 25, 23, 24, 25, 23, 24, 25, 22, 23]
]

fig, ax = plt.subplots(figsize=(14, 8))
bplot = ax.boxplot(temperatures, vert=True, patch_artist=True,
                   boxprops=dict(facecolor='lavender', color='teal', linewidth=2),
                   whiskerprops=dict(color='teal', linewidth=2, linestyle='-.'),
                   capprops=dict(color='teal', linewidth=2, linestyle=':'),
                   medianprops=dict(color='darkblue', linewidth=1.5, linestyle='-'),
                   flierprops=dict(markerfacecolor='teal', marker='s', markersize=8, alpha=0.5))

ax.set_xticklabels(cities, fontsize=12)
ax.set_title('Temperature Variations Across Cities', fontsize=16, fontweight='bold')
ax.set_ylabel('Temperature (Celsius)', fontsize=14)
ax.yaxis.grid(True, linestyle=':', which='major', color='purple', alpha=0.5)

# Color variations for different data groups
colors = ['lavender', 'peachpuff', 'lightsteelblue', 'lemonchiffon', 'papayawhip']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

plt.tight_layout()
plt.show()
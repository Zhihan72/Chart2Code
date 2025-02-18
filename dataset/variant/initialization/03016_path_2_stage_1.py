import matplotlib.pyplot as plt

atlantic_depths = [2300, 2450, 2600, 2750, 2900, 3100, 3250, 3400, 3500, 3700]
pacific_depths = [3000, 3150, 3300, 3500, 3750, 4000, 4100, 4250, 4400, 4500]
indian_depths = [1500, 1600, 1700, 1850, 1950, 2100, 2250, 2350, 2450, 2550]
arctic_depths = [900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350]

data = [atlantic_depths, pacific_depths, indian_depths, arctic_depths]
oceans = ['Atlantic Ocean', 'Pacific Ocean', 'Indian Ocean', 'Arctic Ocean']

fig, ax = plt.subplots(figsize=(10, 6))

boxplot = ax.boxplot(data, vert=True, patch_artist=True, labels=oceans, notch=False)

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
markers = ['o', 's', 'D', '^']
linestyles = ['-', ':', '-.', '--']
for patch, color, marker, linestyle in zip(boxplot['boxes'], colors, markers, linestyles):
    patch.set_facecolor(color)
    patch.set_edgecolor('black')
    patch.set_linewidth(1.5)

plt.setp(boxplot['whiskers'], color='grey', linewidth=1.5, linestyle=':')
plt.setp(boxplot['caps'], color='grey', linewidth=1.5)
plt.setp(boxplot['medians'], color='black', linewidth=2)

ax.set_title('Depth Analysis of Global Deep-Sea Exploration Missions', fontsize=14, weight='bold', pad=20)
ax.set_ylabel('Depth (meters)', fontsize=12)
ax.set_xlabel('Oceans', fontsize=12)

ax.yaxis.grid(True, color='green', linestyle='-', linewidth=0.5)

plt.tight_layout()
plt.show()
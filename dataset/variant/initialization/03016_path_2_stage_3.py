import matplotlib.pyplot as plt

atlantic_depths = [2300, 2450, 2600, 2750, 2900, 3100, 3250, 3400, 3500, 3700]
pacific_depths = [3000, 3150, 3300, 3500, 3750, 4000, 4100, 4250, 4400, 4500]
indian_depths = [1500, 1600, 1700, 1850, 1950, 2100, 2250, 2350, 2450, 2550]
arctic_depths = [900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350]

data = [atlantic_depths, pacific_depths, indian_depths, arctic_depths]
oceans = ['Oceans', 'Deep Blue', 'Waters', 'Cold Sea']

fig, ax = plt.subplots(figsize=(10, 6))

boxplot = ax.boxplot(data, vert=True, patch_artist=True, labels=oceans, notch=False)

# Apply a single color for all data groups
single_color = '#66b3ff'
for patch in boxplot['boxes']:
    patch.set_facecolor(single_color)
    patch.set_edgecolor('black')
    patch.set_linewidth(1.5)

plt.setp(boxplot['whiskers'], color='grey', linewidth=1.5, linestyle=':')
plt.setp(boxplot['caps'], color='grey', linewidth=1.5)
plt.setp(boxplot['medians'], color='black', linewidth=2)

ax.set_title('Dive Missions Deep Seas Globally', fontsize=14, weight='bold', pad=20)
ax.set_ylabel('Meters', fontsize=12)
ax.set_xlabel('Seas', fontsize=12)

ax.yaxis.grid(True, color='green', linestyle='-', linewidth=0.5)

plt.tight_layout()
plt.show()
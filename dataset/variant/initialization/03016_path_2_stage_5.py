import matplotlib.pyplot as plt

pacific_depths = [3000, 3150, 3300, 3500, 3750, 4000, 4100, 4250, 4400, 4500]
indian_depths = [1500, 1600, 1700, 1850, 1950, 2100, 2250, 2350, 2450, 2550]
arctic_depths = [900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350]

data = [pacific_depths, indian_depths, arctic_depths]
oceans = ['Deep Blue', 'Waters', 'Cold Sea']

fig, ax = plt.subplots(figsize=(10, 6))

# Change vert parameter to False for horizontal boxplot
boxplot = ax.boxplot(data, vert=False, patch_artist=True, labels=oceans, notch=False)

single_color = '#66b3ff'
for patch in boxplot['boxes']:
    patch.set_facecolor(single_color)
    patch.set_edgecolor('black')
    patch.set_linewidth(1.5)

plt.setp(boxplot['whiskers'], color='grey', linewidth=1.5, linestyle=':')
plt.setp(boxplot['caps'], color='grey', linewidth=1.5)
plt.setp(boxplot['medians'], color='black', linewidth=2)

ax.set_title('Dive Missions Deep Seas Globally', fontsize=14, weight='bold', pad=20)
ax.set_xlabel('Meters', fontsize=12)  # Changed to xlabel for horizontal orientation
ax.set_ylabel('Seas', fontsize=12)    # Changed to ylabel for horizontal orientation

ax.xaxis.grid(True, color='green', linestyle='-', linewidth=0.5)  # Adjusted grid line for horizontal orientation

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt

nasa = [180, 250, 320, 150, 200, 280, 210]
esa = [220, 270, 180, 190, 240, 260, 230]
roscosmos = [150, 180, 210, 170, 140, 230, 200]
spacex = [110, 190, 270, 250, 210, 280, 200]
cnes = [90, 130, 110, 150, 160, 200, 170]

# New made-up data series for additional agencies
jaxa = [130, 210, 190, 160, 220, 200, 180]
isro = [170, 160, 200, 180, 190, 210, 230]

data = [nasa, esa, roscosmos, spacex, cnes, jaxa, isro]
agencies = ['NASA', 'ESA', 'ROSCOSMOS', 'SpaceX', 'CNES', 'JAXA', 'ISRO']

fig, ax = plt.subplots(figsize=(12, 7))

# Extend color list for added data series
box_colors = ['#99ff99', '#ffcc99', '#c2c2f0', '#ff9999', '#66b3ff', '#ffb3e6', '#8e44ad']

ax.yaxis.grid(True, linestyle='-', alpha=0.5)

bp = ax.boxplot(data, vert=True, patch_artist=True, notch=False, whis=1.5,
                boxprops=dict(linestyle='-', linewidth=1),
                capprops=dict(linestyle=':', linewidth=2),
                whiskerprops=dict(linestyle='--', linewidth=2),
                flierprops=dict(marker='o', color='red', markersize=5, alpha=0.75),
                medianprops=dict(linestyle='-', linewidth=2))

for patch, color in zip(bp['boxes'], box_colors):
    patch.set(facecolor=color)

ax.set_xticklabels(agencies, fontsize=11)
ax.set_ylabel('Days of Mission Trip', fontsize=12)
ax.set_title('Agency Mission Timeframes Comparison Last 10 Years', fontsize=14, pad=20)

for i, agency in enumerate(agencies):
    ax.plot([], [], label=agency, color=box_colors[i])
ax.legend(fontsize=10)

plt.tight_layout()
plt.show()
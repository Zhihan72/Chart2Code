import matplotlib.pyplot as plt

nasa = [180, 250, 320, 150, 200, 280, 210]
esa = [220, 270, 180, 190, 240, 260, 230]
roscosmos = [150, 180, 210, 170, 140, 230, 200]
spacex = [110, 190, 270, 250, 210, 280, 200]
cnes = [90, 130, 110, 150, 160, 200, 170]

# New made-up data for JAXA and ISRO
jaxa = [160, 210, 250, 200, 180, 240, 220]
isro = [130, 180, 160, 170, 140, 190, 175]

data = [nasa, esa, roscosmos, spacex, cnes, jaxa, isro]
agencies = ['NASA', 'ESA', 'ROS', 'SPX', 'CNES', 'JAXA', 'ISRO']

fig, ax = plt.subplots(figsize=(12, 9))

# Expanded color list for additional agencies
box_colors = ['#ffcc99', '#99ff99', '#66b3ff', '#c2c2f0', '#ff9999', '#ffb3e6', '#c2f0c2']

bp = ax.boxplot(data, vert=False, patch_artist=True, notch=True, whis=2.0, capprops=dict(color='blue', linestyle='-'))

for patch, color in zip(bp['boxes'], box_colors):
    patch.set_facecolor(color)

ax.set_yticklabels(agencies, fontsize=10)
ax.set_xlabel('Mission Days', fontsize=11, color='brown')
ax.set_title('Space Mission Durations', fontsize=13, color='purple', pad=15)

ax.xaxis.grid(True, linestyle=':', linewidth=0.5, alpha=0.5)
ax.spines['top'].set_edgecolor('none')
ax.spines['right'].set_edgecolor('none')
ax.spines['left'].set_linestyle('--')
ax.spines['bottom'].set_linestyle('--')

plt.legend(['Duration'], loc='lower right', fontsize=10, frameon=False)

plt.tight_layout()
plt.show()
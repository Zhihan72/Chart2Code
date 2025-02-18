import matplotlib.pyplot as plt

# Data: Mission durations (in days) for different space agencies
nasa = [180, 250, 320, 150, 200, 280, 210]
esa = [220, 270, 180, 190, 240, 260, 230]
roscosmos = [150, 180, 210, 170, 140, 230, 200]
spacex = [110, 190, 270, 250, 210, 280, 200]
cnes = [90, 130, 110, 150, 160, 200, 170]

# Compile data into a list
data = [nasa, esa, roscosmos, spacex, cnes]
agencies = ['NASA', 'ESA', 'ROSCOSMOS', 'SpaceX', 'CNES']

# Create horizontal box plot
fig, ax = plt.subplots(figsize=(12, 7))
box_colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Plot with custom box colors and styles
bp = ax.boxplot(data, vert=False, patch_artist=True, notch=True, whis=2.0, capprops=dict(color='blue', linestyle='-'))

# Customize each box color
for patch, color in zip(bp['boxes'], box_colors):
    patch.set_facecolor(color)

# Set y-axis labels to match the space agencies
ax.set_yticklabels(agencies, fontsize=10)
ax.set_xlabel('Mission Duration (Days)', fontsize=11, color='brown')
ax.set_title('Comparison of Space Missions Duration by Agency\nOver the Past Decade', fontsize=13, color='purple', pad=15)

# Add grid with altered style
ax.xaxis.grid(True, linestyle=':', linewidth=0.5, alpha=0.5)
ax.spines['top'].set_edgecolor('none')
ax.spines['right'].set_edgecolor('none')
ax.spines['left'].set_linestyle('--')
ax.spines['bottom'].set_linestyle('--')

# Add a simple legend
plt.legend(['Mission Duration'], loc='lower right', fontsize=10, frameon=False)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
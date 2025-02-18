import matplotlib.pyplot as plt

percentages = [25, 20, 15, 15, 10, 10, 5, 12, 8]
crop_colors = ['#FF6347', '#4682B4', '#9ACD32', '#FF69B4', '#8A2BE2', '#00CED1', '#FF4500', '#FFD700', '#7FFF00']
explode = [0.1, 0, 0, 0, 0, 0, 0, 0, 0]

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    percentages,
    colors=crop_colors,
    autopct='%1.1f%%',
    startangle=90,  # Changed start angle for variation
    explode=explode,
    shadow=False,  # Removed shadow for simplicity
    wedgeprops={'edgecolor': 'green', 'linestyle': '--'}  # Changed edge color and linestyle
)

# Moving percent labels off-wedge
for autotext in autotexts:
    autotext.set_color('blue')  # Changed text color
    autotext.set_fontsize(12)  # Adjusted font size
    autotext.set_weight('regular')  # Changed weight to regular

# Added a grid
ax.grid(True, linestyle=':', linewidth=1.2)

# Added legend with different location and style
plt.legend(wedges, ['Crop ' + str(i) for i in range(1, 10)], loc='upper right', fontsize=8)

plt.tight_layout()
plt.show()
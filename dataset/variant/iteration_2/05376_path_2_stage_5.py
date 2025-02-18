import matplotlib.pyplot as plt

star_systems = [
    [2, 3, 5.6],
    [7, 1, 4.2],
    [1, 9, 7.1],
    [6, 8, 6.3],
    [9, 5, 8.4]
]

y_coords = [data[1] for data in star_systems]
brightness = [data[2] for data in star_systems]

fig, ax = plt.subplots(figsize=(12, 8))

ax.barh(y_coords, brightness, color='green', alpha=0.8, edgecolor='orange', linestyle='-.', hatch='/')

ax.grid(True, linestyle=':', alpha=0.3)

plt.legend(['Brightness'], loc='upper right', frameon=True, fontsize='small', facecolor='ivory', edgecolor='gray')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

plt.tight_layout()
plt.show()
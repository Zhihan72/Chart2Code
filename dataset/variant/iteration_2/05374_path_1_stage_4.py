import matplotlib.pyplot as plt

wax_types = ['Soy', 'Bee', 'Para', 'Palm', 'Gel']

data = [
    [160, 150, 170, 155, 172, 162, 180, 165, 160, 175],
    [150, 140, 160, 145, 155, 148, 148, 158, 155, 150],
    [130, 142, 140, 138, 135, 150, 135, 145, 144, 148],
    [170, 180, 165, 178, 170, 160, 168, 175, 185, 165],
    [128, 135, 130, 132, 132, 120, 130, 125, 138, 128]
]

colors = ['#FF6347', '#FFD700', '#20B2AA', '#8A2BE2', '#FF4500']

fig, ax = plt.subplots(figsize=(12, 7))

bp = ax.boxplot(data, vert=False, patch_artist=True, notch=True,
                boxprops=dict(linewidth=2.0, linestyle='-.'),
                whiskerprops=dict(linewidth=2.0, linestyle='-.'),
                capprops=dict(linewidth=2.0, linestyle='-.'),
                medianprops=dict(color='blue', linewidth=2),
                flierprops=dict(marker='*', color='blue', alpha=0.7))

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

ax.set_title('Candle Weight by Wax Type', fontsize=14, pad=15)
ax.set_xlabel('Weight (g)', fontsize=11)
ax.set_ylabel('Wax', fontsize=11)
ax.set_yticklabels(wax_types, fontsize=11)

ax.grid(axis='x', linestyle=':', alpha=0.5)

plt.figtext(0.13, 0.89, "Notched boxes = 95% CI around median", fontsize=10)

plt.tight_layout()
plt.show()
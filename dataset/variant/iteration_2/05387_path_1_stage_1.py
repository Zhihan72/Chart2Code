import matplotlib.pyplot as plt
import numpy as np

solar = [450, 520, 495, 530, 600, 680, 750, 720, 640, 580, 540, 500]
wind = [350, 380, 410, 480, 520, 570, 620, 590, 530, 490, 450, 410]
hydro = [700, 690, 720, 750, 800, 850, 900, 870, 830, 790, 750, 710]
geothermal = [310, 300, 320, 330, 350, 360, 380, 370, 350, 340, 320, 310]

data = [solar, wind, hydro, geothermal]
energy_sources = ['Solar', 'Wind', 'Hydro', 'Geothermal']

fig, ax = plt.subplots(figsize=(14, 8))

bp = ax.boxplot(data, vert=False, patch_artist=True, notch=False, whis=1.5,
                boxprops=dict(facecolor='lightgray', color='black', linewidth=1.5),
                whiskerprops=dict(color='black', linewidth=1.5),
                capprops=dict(color='black', linewidth=1.5),
                medianprops=dict(color='red', linewidth=2),
                flierprops=dict(marker='o', color='black', alpha=0.5))

for patch, color in zip(bp['boxes'], ['#f9a825', '#1e88e5', '#81c784', '#ff7043']):
    patch.set_facecolor(color)

means = [np.mean(source) for source in data]
for mean, y_pos in zip(means, range(1, len(data) + 1)):
    ax.plot(mean, y_pos, 'D', markerfacecolor='cyan', markersize=8)
    ax.annotate(f'{mean:.1f} MWh', xy=(mean, y_pos), xytext=(mean + 20, y_pos),
                verticalalignment='center', fontsize=9, color='darkblue')

ax.set_yticks(np.arange(1, len(energy_sources) + 1))
ax.set_yticklabels(energy_sources, fontsize=10)

for i, source in enumerate(data):
    total_output = sum(source)
    ax.annotate(f'Total: {total_output} MWh', xy=(max(source) + 20, i + 1),
                xytext=(max(source) + 20, i + 1), fontsize=9, color='green')

plt.tight_layout()
plt.show()
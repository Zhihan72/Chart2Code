import matplotlib.pyplot as plt

wax_types = ['Beeswax', 'Paraffin Wax', 'Soy Wax', 'Gel Wax', 'Palm Wax']

soy_wax_weights = [162, 170, 150, 175, 155, 160, 165, 180, 172, 160]
beeswax_weights = [150, 140, 150, 158, 145, 148, 155, 160, 148, 155]
paraffin_weights = [135, 142, 130, 135, 145, 138, 144, 150, 140, 148]
palm_wax_weights = [170, 160, 165, 185, 178, 168, 170, 165, 175, 180]
gel_wax_weights = [130, 132, 120, 125, 138, 128, 132, 130, 135, 128]

data = [beeswax_weights, paraffin_weights, soy_wax_weights, gel_wax_weights, palm_wax_weights]

colors = ['#1E90FF', '#32CD32', '#FF69B4', '#8B0000', '#FFA500']  # New color set

fig, ax = plt.subplots(figsize=(12, 7))

bp = ax.boxplot(data, vert=True, patch_artist=True,
                boxprops=dict(linewidth=1.5),
                whiskerprops=dict(linewidth=1.5, linestyle=':'),
                capprops=dict(linewidth=1.5, color='purple'),
                medianprops=dict(color='green', linewidth=2),
                flierprops=dict(marker='x', color='red', alpha=0.7))

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

ax.set_title('Candle Weight Distribution by Wax Type', fontsize=16, pad=15)
ax.set_xlabel('Wax Types', fontsize=12)
ax.set_ylabel('Mass (g)', fontsize=12)
ax.set_xticklabels(wax_types, fontsize=10)

ax.grid(axis='y', linestyle='-', alpha=0.5)

plt.tight_layout()

plt.show()
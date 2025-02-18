import matplotlib.pyplot as plt

# Data representing monthly temperatures at five different wells
well_temps = [
    [35, 36, 38, 40, 42, 45, 43, 41, 44, 37, 36, 35],  # Well A
    [50, 52, 54, 56, 55, 57, 58, 54, 53, 51, 52, 50],  # Well B
    [28, 30, 29, 31, 33, 35, 34, 32, 31, 30, 29, 28],  # Well C
    [45, 46, 47, 48, 49, 50, 49, 48, 47, 46, 45, 44],  # Well D
    [39, 38, 37, 36, 35, 34, 36, 38, 40, 39, 38, 37]   # Well E
]

fig, ax = plt.subplots(figsize=(12, 8))

bp = ax.boxplot(well_temps, patch_artist=True, notch=False, vert=False,
                boxprops=dict(color='black', linewidth=1.5),
                medianprops=dict(color='red', linewidth=2),
                whiskerprops=dict(color='black'),
                capprops=dict(color='black'),
                flierprops=dict(marker='o', color='blue', alpha=0.5))

new_colors = ['#FF6347', '#4682B4', '#32CD32', '#FFA500', '#9370DB']
for patch, color in zip(bp['boxes'], new_colors):
    patch.set_facecolor(color)

ax.set_yticklabels([])

plt.show()
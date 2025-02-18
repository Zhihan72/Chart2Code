import matplotlib.pyplot as plt

# Manually shuffled data representing monthly temperatures at five different wells
well_temps = [
    [40, 42, 36, 44, 35, 37, 36, 41, 38, 43, 35, 45],  # Well A (shuffled)
    [54, 55, 56, 50, 51, 52, 58, 50, 53, 52, 54, 57],  # Well B (shuffled)
    [28, 31, 32, 29, 33, 34, 30, 35, 30, 29, 28, 31],  # Well C (shuffled)
    [45, 49, 47, 46, 44, 45, 48, 47, 50, 46, 49, 48],  # Well D (shuffled)
    [39, 36, 37, 35, 34, 40, 38, 39, 38, 36, 37, 38]   # Well E (shuffled)
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
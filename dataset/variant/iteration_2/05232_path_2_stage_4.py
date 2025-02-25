import matplotlib.pyplot as plt

engineering_hours = [19, 15, 24, 21, 17, 18, 20, 16, 23, 22, 21, 24, 18, 19, 20]
arts_hours = [12, 7, 10, 11, 14, 9, 13, 8, 10, 12, 9, 15, 8, 10, 11]
science_hours = [22, 21, 23, 25, 18, 19, 24, 20, 22, 21, 24, 19, 23, 22, 20]
business_hours = [8, 7, 8, 5, 9, 7, 6, 10, 6, 8, 10, 7, 9, 8, 6]
law_hours = [30, 27, 29, 28, 25, 28, 26, 29, 32, 25, 28, 27, 30, 26, 29]

data = [engineering_hours, arts_hours, science_hours, business_hours, law_hours]

fig, ax = plt.subplots(figsize=(14, 8))

box = ax.boxplot(data, vert=False, patch_artist=True, 
                 boxprops=dict(facecolor="lightgreen", color="blue", linestyle='--'),
                 whiskerprops=dict(color="magenta", linestyle='-.'),
                 capprops=dict(color="cyan"),
                 flierprops=dict(marker="s", color="red", alpha=0.7),
                 medianprops=dict(color="purple"))

colors = ['lightcoral', 'lightyellow', 'lightgray', 'lightpink', 'lightblue']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

ax.grid(True, linestyle='-', linewidth=1, alpha=0.3)

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt

populations_yellowstone = [35, 40, 45, 42, 38, 44, 47, 48, 43, 45]
populations_sundarban = [23, 25, 26, 24, 22, 23, 27, 29, 28, 30]
populations_kanha = [51, 49, 52, 54, 53, 55, 57, 56, 59, 60]

parks = ['Yellowstone', 'Sundarban', 'Kanha']
populations_data = [populations_yellowstone, populations_sundarban, populations_kanha]

plt.figure(figsize=(10, 6))
boxplot = plt.boxplot(populations_data, vert=True, patch_artist=True, notch=False,
            boxprops=dict(facecolor='lightgreen', color='darkgreen', alpha=0.6),
            capprops=dict(color='darkgreen'),
            whiskerprops=dict(color='darkgreen'),
            flierprops=dict(marker='o', color='red', alpha=0.5),
            medianprops=dict(color='gold', linewidth=2))

colors = ['#ff9999', '#66b3ff', '#99ff99']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)

plt.xticks([1, 2, 3], parks, fontsize=12)
plt.ylabel('Wildlife Numbers', fontsize=14)
plt.title('Ten-Year Trends in National Parks: Tiger Conservation Efforts', fontsize=16, weight='bold', pad=20)

plt.annotate('Growth Observed in Kanha', xy=(3, 60), xytext=(3.5, 62),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='black')

plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

plt.show()
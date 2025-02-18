import matplotlib.pyplot as plt

populations_yellowstone = [35, 40, 45, 42, 38, 44, 47, 48, 43, 45]
populations_sundarban = [23, 25, 26, 24, 22, 23, 27, 29, 28, 30]
populations_kanha = [51, 49, 52, 54, 53, 55, 57, 56, 59, 60]

# Removed Bandipur data
parks = ['Kanha', 'Yellowstone', 'Sundarban']
populations_data = [populations_yellowstone, populations_sundarban, populations_kanha]  # Reordered

plt.figure(figsize=(14, 8))
boxplot = plt.boxplot(populations_data, vert=False, patch_artist=True, notch=True,
            boxprops=dict(facecolor='lightgreen', color='darkgreen', alpha=0.6),
            capprops=dict(color='darkgreen'),
            whiskerprops=dict(color='darkgreen'),
            flierprops=dict(marker='o', color='red', alpha=0.5),
            medianprops=dict(color='gold', linewidth=2))

# Adjusted color set for three groups
colors = ['#ff9999', '#66b3ff', '#99ff99']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)

plt.yticks([1, 2, 3], parks, fontsize=12)
plt.xlabel('Wildlife Numbers', fontsize=14)
plt.title('Ten-Year Trends in National Parks: Tiger Conservation Efforts\nAnalysis Summary',
          fontsize=16, weight='bold', pad=20)

plt.annotate('Growth Observed in Kanha', xy=(60, 0.85), xytext=(62, 1),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='black')

plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

plt.show()
import matplotlib.pyplot as plt

chocolate_brands = ["CocoaHeaven", "ChocoDelight", "SweetCocoa", "DarkFantasy", "ChocoTwist"]
years = ["2015", "2016", "2017", "2018", "2019"]

chocolate_data = {
    "CocoaHeaven": [75, 80, 78, 85, 82],
    "ChocoDelight": [70, 75, 72, 78, 79],
    "SweetCocoa": [68, 72, 70, 74, 69],
    "DarkFantasy": [80, 85, 83, 88, 86],
    "ChocoTwist": [65, 67, 66, 70, 68],
}

box_data = [list(year_data) for year_data in zip(*chocolate_data.values())]

fig, ax = plt.subplots(figsize=(10, 6))

bplot = ax.boxplot(box_data, vert=False, patch_artist=True, notch=False,
                   boxprops=dict(color='brown'),
                   whiskerprops=dict(color='brown'),
                   capprops=dict(color='brown'),
                   medianprops=dict(color='darkred', linewidth=2),
                   flierprops=dict(markerfacecolor='blue', marker='o', markersize=8, linestyle='none'))

# Shuffling the colors manually for the box plots
colors = ['#4682B4', '#FFD700', '#8B0000', '#3CB371', '#FF6347']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

ax.set_yticklabels(years)
ax.set_ylabel('Year', fontsize=12)
ax.set_xlabel('Flavor Score', fontsize=12)
ax.set_title('Flavor Diversity Across Different Chocolate Brands\n(2015-2019)', fontsize=14, fontweight='bold')

ax.set_xlim(60, 90)

plt.tight_layout()
plt.show()
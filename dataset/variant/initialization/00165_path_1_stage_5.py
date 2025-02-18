import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)

regions_data = {
    'North America': (np.array([120, 125, 130, 140, 145, 150, 160, 170, 180, 195, 210]), 
                      np.array([40, 42, 43, 45, 47, 50, 53, 56, 60, 65, 70]), 
                      np.array([5, 5, 5, 6, 6, 7, 8, 9, 10, 11, 12])),
    'Europe': (np.array([150, 155, 160, 165, 170, 175, 180, 190, 200, 210, 220]), 
               np.array([50, 52, 55, 57, 60, 63, 67, 72, 77, 83, 90]), 
               np.array([8, 9, 10, 12, 14, 16, 19, 21, 24, 27, 30])),
    'Asia': (np.array([130, 132, 134, 136, 138, 140, 145, 150, 155, 162, 170]), 
             np.array([100, 105, 110, 115, 120, 125, 130, 140, 150, 160, 170]), 
             np.array([10, 11, 12, 13, 15, 17, 20, 23, 26, 30, 35])),
    'Africa': (np.array([50, 52, 54, 56, 58, 60, 62, 65, 68, 72, 76]), 
               np.array([30, 32, 34, 36, 38, 40, 42, 45, 48, 52, 55]), 
               np.array([5, 5, 6, 6, 7, 8, 8, 9, 10, 11, 12])),
    'South America': (np.array([200, 205, 210, 215, 220, 230, 240, 250, 260, 275, 290]), 
                      np.array([70, 73, 75, 78, 82, 86, 90, 95, 100, 106, 112]), 
                      np.array([12, 13, 14, 15, 16, 17, 18, 20, 22, 24, 26])),
}

left_regions = ['North America', 'Europe']
right_regions = ['Asia', 'Africa', 'South America']

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['b', 'g', 'r', 'y', 'm', 'c']
hatches = ['/', '\\', '|', '-', '+', '*']
markers = ['o', '^', 's', 'D', 'x', 'O']
indices = [0, 1, 2]

for region_idx, region in enumerate(left_regions):
    arabica, robusta, liberica = regions_data[region]
    ax.bar(years, -arabica, label=f'{region} Arabica', color=colors[region_idx], hatch=hatches[region_idx], width=0.8)
    ax.bar(years, -robusta, bottom=-arabica, label=f'{region} Robusta', color=colors[(region_idx + 1) % 5], hatch=hatches[(region_idx + 1) % 5], width=0.8)
    ax.bar(years, -liberica, bottom=-arabica-robusta, label=f'{region} Liberica', color=colors[(region_idx + 2) % 5], hatch=hatches[(region_idx + 2) % 5], width=0.8)

for region_idx, region in enumerate(right_regions):
    arabica, robusta, liberica = regions_data[region]
    ax.bar(years, arabica, label=f'{region} Arabica', color=colors[region_idx + 3], hatch=hatches[region_idx + 3], width=0.8)
    ax.bar(years, robusta, bottom=arabica, label=f'{region} Robusta', color=colors[(region_idx + 4) % 5], hatch=hatches[(region_idx + 4) % 5], width=0.8)
    ax.bar(years, liberica, bottom=arabica+robusta, label=f'{region} Liberica', color=colors[(region_idx + 5) % 5], hatch=hatches[(region_idx + 5) % 5], width=0.8)

ax.set_facecolor('lightgrey')
ax.grid(True, which='major', linestyle='--', linewidth=0.7)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_linewidth(0.5)
ax.spines['left'].set_linestyle('dotted')
ax.spines['bottom'].set_color('black')

ax.set_title("Diverging Consumption: Coffee Styles Overtime (2020-30)", fontsize=14, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Coffee Consumption (in millions of kilograms)", fontsize=12)
ax.axhline(0, color='black', linewidth=0.8)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3, title='Region & Type')

plt.xticks(years, rotation=45)
plt.tight_layout()
plt.show()
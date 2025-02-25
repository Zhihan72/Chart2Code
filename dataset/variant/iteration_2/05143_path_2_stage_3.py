import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2020)
crops = ['Wheat', 'Corn', 'Barley', 'Soybeans']

wheat_yield = [3.5, 3.7, 3.9, 4.1, 4.0]
corn_yield = [7.0, 7.3, 7.8, 8.0, 7.9]
barley_yield = [2.5, 2.7, 2.8, 3.0, 3.1]
soybean_yield = [2.0, 2.1, 2.2, 2.3, 2.4]

width = 0.2  # Width of the bars
x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(12, 8))

ax.bar(x - 1.5*width, wheat_yield, width, label='Wheat', color='#FFD700', edgecolor='black')
ax.bar(x - 0.5*width, corn_yield, width, label='Corn', color='#FF8C00', edgecolor='black')
ax.bar(x + 0.5*width, barley_yield, width, label='Barley', color='#98FB98', edgecolor='black')
ax.bar(x + 1.5*width, soybean_yield, width, label='Soybeans', color='#1E90FF', edgecolor='black')

ax.set_title("Crop Yield Experimentation Results\n(2015-2019)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Yield (tons per hectare)", fontsize=14)

ax.set_xticks(x)
ax.set_xticklabels(years, rotation=45)

ax.legend(title='Crops', loc='upper center', ncol=2, bbox_to_anchor=(0.5, 1.2), fontsize=10)

ax.yaxis.grid(True, linestyle=':', alpha=0.5)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linestyle('dashed')

for i in range(len(years)):
    heights = [wheat_yield[i], corn_yield[i], barley_yield[i], soybean_yield[i]]
    for j, height in enumerate(heights):
        ax.text(i - 1.5*width + j * width, height + 0.1, f'{height}', ha='center', va='bottom', color='black', fontsize=9)

plt.tight_layout()
plt.show()
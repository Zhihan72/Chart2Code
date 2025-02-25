import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2020)
crops = ['Wheat', 'Corn', 'Barley', 'Soybeans']

wheat_yield = [3.5, 3.7, 3.9, 4.1, 4.0]
corn_yield = [7.0, 7.3, 7.8, 8.0, 7.9]
barley_yield = [2.5, 2.7, 2.8, 3.0, 3.1]
soybean_yield = [2.0, 2.1, 2.2, 2.3, 2.4]

colors = ['#FFD700', '#ADFF2F', '#20B2AA', '#FF6347']

fig, ax = plt.subplots(figsize=(12, 8))

ax.bar(years, wheat_yield, label='Wheat', hatch='/', color=colors[0], edgecolor='black')
ax.bar(years, corn_yield, bottom=wheat_yield, label='Corn', hatch='\\', color=colors[1], edgecolor='black')
ax.bar(years, barley_yield, bottom=np.array(wheat_yield) + np.array(corn_yield), label='Barley', hatch='x', color=colors[2], edgecolor='black')
ax.bar(years, soybean_yield, bottom=np.array(wheat_yield) + np.array(corn_yield) + np.array(barley_yield), label='Soybeans', hatch='o', color=colors[3], edgecolor='black')

ax.set_title("Crop Yield Experimentation Results\n(2015-2019)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Yield (tons per hectare)", fontsize=14)

plt.xticks(years, rotation=45)

ax.legend(title='Crops', loc='upper center', ncol=2, bbox_to_anchor=(0.5, 1.2), fontsize=10)

ax.yaxis.grid(True, linestyle=':', alpha=0.5)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linestyle('dashed')

for i in range(len(years)):
    height_sum = 0
    for yield_data, hatch_pattern in zip([wheat_yield, corn_yield, barley_yield, soybean_yield], ['/','\\','x','o']):
        height_sum += yield_data[i]
        ax.text(years[i], height_sum - yield_data[i]/2, f'{yield_data[i]}', ha='center', va='center', color='black', fontsize=9)

plt.tight_layout()
plt.show()
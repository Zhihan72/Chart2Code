import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2020)
crops = ['Wheat', 'Corn', 'Barley', 'Soybeans', 'Rice', 'Sunflower']

wheat_yield = [3.5, 3.7, 3.9, 4.1, 4.0]
corn_yield = [7.0, 7.3, 7.8, 8.0, 7.9]
barley_yield = [2.5, 2.7, 2.8, 3.0, 3.1]
soybean_yield = [2.0, 2.1, 2.2, 2.3, 2.4]
rice_yield = [4.2, 4.3, 4.5, 4.6, 4.5]
sunflower_yield = [1.8, 1.9, 2.0, 2.1, 2.2]

colors = ['#FFD700', '#ADFF2F', '#20B2AA', '#FF6347', '#8A2BE2', '#FF4500']

fig, ax = plt.subplots(figsize=(12, 8))

ax.bar(years, wheat_yield, label='Wheat', color=colors[0], hatch='//')
ax.bar(years, corn_yield, bottom=wheat_yield, label='Corn', color=colors[1], hatch='\\\\')
ax.bar(years, barley_yield, bottom=np.array(wheat_yield) + np.array(corn_yield), label='Barley', color=colors[2], hatch='--')
ax.bar(years, soybean_yield, bottom=np.array(wheat_yield) + np.array(corn_yield) + np.array(barley_yield), label='Soybeans', color=colors[3], hatch='xx')
ax.bar(years, rice_yield, bottom=np.array(wheat_yield) + np.array(corn_yield) + np.array(barley_yield) + np.array(soybean_yield), label='Rice', color=colors[4], hatch='//')
ax.bar(years, sunflower_yield, bottom=np.array(wheat_yield) + np.array(corn_yield) + np.array(barley_yield) + np.array(soybean_yield) + np.array(rice_yield), label='Sunflower', color=colors[5], hatch='\\\\')

ax.set_title("Crop Yield Experimentation Results (2015-2019)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Yield (tons/ha)", fontsize=14)

ax.legend(title='Crops', loc='lower right')

ax.yaxis.grid(True, linestyle=':', alpha=0.9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

for i in range(len(years)):
    height_sum = 0
    for yield_name in [wheat_yield, corn_yield, barley_yield, soybean_yield, rice_yield, sunflower_yield]:
        height_sum += yield_name[i]
        ax.text(years[i], height_sum - yield_name[i]/2, f'{yield_name[i]}', ha='center', va='center', color='blue', fontsize=9)

plt.xticks(years, rotation=30)
plt.tight_layout()
plt.show()
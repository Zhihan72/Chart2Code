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

# Introduce variations in marker and line styles
ax.bar(years, wheat_yield, label='Wheat', color=colors[0], hatch='//')
ax.bar(years, corn_yield, bottom=wheat_yield, label='Corn', color=colors[1], hatch='\\\\')
ax.bar(years, barley_yield, bottom=np.array(wheat_yield) + np.array(corn_yield), label='Barley', color=colors[2], hatch='--')
ax.bar(years, soybean_yield, bottom=np.array(wheat_yield) + np.array(corn_yield) + np.array(barley_yield), label='Soybeans', color=colors[3], hatch='xx')

ax.set_title("Crop Yield Experimentation Results (2015-2019)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Yield (tons/ha)", fontsize=14)

# Random legend location
ax.legend(title='Crops', loc='lower right')

# Alter grid style and disable borders
ax.yaxis.grid(True, linestyle=':', alpha=0.9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add annotations to each bar
for i in range(len(years)):
    height_sum = 0
    for yield_name in [wheat_yield, corn_yield, barley_yield, soybean_yield]:
        height_sum += yield_name[i]
        ax.text(years[i], height_sum - yield_name[i]/2, f'{yield_name[i]}', ha='center', va='center', color='blue', fontsize=9)

plt.xticks(years, rotation=30)
plt.tight_layout()
plt.show()
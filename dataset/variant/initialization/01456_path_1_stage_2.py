import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2026)
brands = ['EcoChic', 'GreenThreads', 'SustainWear', 'NatureKnits', 'PureTrend']

organic_cotton = np.array([
    [5, 10, 15, 20, 25, 30],   
    [4, 8, 12, 16, 20, 24],    
    [6, 11, 17, 23, 29, 35],   
    [5, 9, 14, 18, 23, 28],    
    [3, 7, 11, 15, 19, 23]     
])

recycled_polyester = np.array([
    [3, 5, 8, 12, 15, 19],     
    [4, 7, 11, 14, 18, 21],    
    [2, 6, 9, 13, 17, 22],     
    [3, 5, 9, 13, 16, 20],     
    [4, 6, 10, 14, 18, 22]     
])

hemp = np.array([
    [2, 4, 6, 8, 10, 12],      
    [1, 3, 5, 7, 9, 11],       
    [3, 5, 8, 11, 14, 17],     
    [2, 4, 7, 10, 13, 15],     
    [1, 2, 4, 6, 8, 10]        
])

fig, ax = plt.subplots(figsize=(14, 9))

bar_width = 0.15
x_indexes = np.arange(len(years))

# Updated the color scheme
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

for i, brand in enumerate(brands):
    ax.bar(x_indexes + i * bar_width, organic_cotton[i], width=bar_width, label='Organic Cotton' if i == 0 else "", color=colors[0], hatch='/', alpha=0.7)
    ax.bar(x_indexes + i * bar_width, recycled_polyester[i], width=bar_width, bottom=organic_cotton[i], label='Recycled Polyester' if i == 0 else "", color=colors[1], hatch='\\', alpha=0.7)
    ax.bar(x_indexes + i * bar_width, hemp[i], width=bar_width, bottom=organic_cotton[i] + recycled_polyester[i], label='Hemp' if i == 0 else "", color=colors[2], hatch='.', alpha=0.7)

ax.set_xlabel('Year', fontsize=12, fontstyle='italic')
ax.set_ylabel('Material Usage (Tons)', fontsize=12, fontstyle='italic')
ax.set_title('Adoption of Eco-Friendly Materials in Fashion Brands (2020-2025)', fontsize=14, fontweight='bold', color='darkgreen', pad=20)

ax.set_xticks(x_indexes + bar_width * 2)
ax.set_xticklabels(years)

handles, labels = ax.get_legend_handles_labels()
unique_labels = dict(zip(labels, handles))
ax.legend(unique_labels.values(), unique_labels.keys(), loc='lower right', fontsize=9, title='Material Types', ncol=1)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.grid(axis='y', linestyle=':', linewidth=0.8, alpha=0.6, color='gray')

plt.tight_layout(rect=[0, 0, 1, 1])

plt.show()
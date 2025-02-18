import matplotlib.pyplot as plt
import numpy as np

countries = ['Finland', 'Norway', 'Iceland', 'Denmark', 'Netherlands', 
             'Sweden', 'Switzerland', 'Belgium', 'Canada', 'Brazil',
             'Imaginaryland', 'CoffeeTopia', 'JavaNation']
consumption_kg = [12, 9.9, 9, 8.7, 8.4, 8.2, 7.9, 6.8, 6.5, 6.1, 
                  10.5, 11.2, 9.5]

sorted_indices = np.argsort(consumption_kg)[::-1]
countries_sorted = [countries[i] for i in sorted_indices]
consumption_sorted = [consumption_kg[i] for i in sorted_indices]

fig, ax = plt.subplots(figsize=(12, 8))

# New color set
colors = ['#FF6347', '#FFD700', '#ADFF2F', '#20B2AA', '#1E90FF', 
          '#9370DB', '#FF69B4', '#FF8C00', '#B0C4DE', '#32CD32',
          '#8A2BE2', '#DC143C', '#00CED1']

bars = ax.barh(countries_sorted, consumption_sorted, color=colors, edgecolor='darkslategray')

ax.set_title('Global Caffeine Rush:\nTop Coffee Consuming Countries in 2023', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Average Annual Coffee Consumption (kg per capita)', fontsize=12)

for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width} kg', xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(3, 0), textcoords='offset points',
                ha='left', va='center', fontsize=10, color='black')

ax.xaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax.set_axisbelow(True)
ax.tick_params(axis='y', which='major', labelsize=10)

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)
plant_based = np.array([20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50])
meat = np.array([30, 28, 26, 25, 23, 21, 20, 18, 16, 15, 14])
dairy = np.array([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10])
processed_food = np.array([10, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22])
insects = np.array([20, 18, 16, 14, 13, 12, 10, 9, 8, 6, 4])
seafood = np.array([15, 16, 17, 18, 19, 20, 20, 21, 22, 23, 24])
vegan_products = np.array([5, 7, 9, 10, 11, 13, 15, 16, 18, 19, 20])

fig, ax = plt.subplots(figsize=(14, 9))

ax.stackplot(years, plant_based, meat, dairy, processed_food, insects, seafood, vegan_products,
             labels=['Vegetarian Options', 'Animal Meat', 'Cows & Goats', 'Packaged Meals',
                     'Edible Bugs', 'Seafood', 'Vegan Products'],
             colors=['#FF9896', '#98DF8A', '#C5B0D5', '#FFBB78', '#AEC7E8', '#C49C94', '#FFCCFF'], alpha=0.6)

ax.set_title("Transformation in Culinary Trends (2020-2030)", fontsize=18, fontweight='bold', pad=20,
             color='navy')
ax.set_xlabel('Timeline', fontsize=14, color='darkred')
ax.set_ylabel('Consumption Share (%)', fontsize=14, color='darkgreen')
ax.legend(loc='upper left', fontsize=10, bbox_to_anchor=(0.85, 1), facecolor='whitesmoke', edgecolor='black')
ax.grid(True, linestyle=':', linewidth=0.7, color='gray')
ax.set_xticks(np.arange(2020, 2031))
ax.tick_params(axis='x', rotation=0, color='purple', width=2)
ax.annotate('Vegan Rise', xy=(2025, 35), xytext=(2027, 70),
            arrowprops=dict(facecolor='maroon', arrowstyle='-|>', lw=1.2), fontsize=14, color='red')
ax.annotate('Falling Insect Cuisine', xy=(2028, 4), xytext=(2026, 12),
            arrowprops=dict(facecolor='darkblue', arrowstyle='->', lw=1.5), fontsize=10, color='orange')

plt.tight_layout()
plt.show()
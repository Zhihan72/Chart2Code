import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
food_categories = ["Cereals", "Fruits", "Vegetables", "Dairy"]
cereals = [280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480]
fruits = [50, 55, 60, 70, 80, 90, 100, 110, 120, 130, 140]
vegetables = [100, 105, 110, 115, 120, 130, 140, 150, 160, 170, 180]
dairy = [150, 152, 155, 157, 160, 165, 170, 175, 180, 185, 190]

food_production = np.vstack([cereals, fruits, vegetables, dairy])
colors = ['#8B0000', '#4682B4', '#FFD700', '#32CD32']

fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(years, food_production, labels=food_categories, colors=colors, alpha=0.85)

ax.set_title('Food Production Trends in Agroland\n2010-2020', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Production (Million Tonnes)', fontsize=12)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

ax.legend(title='Categories', loc='upper right', fontsize=10, frameon=True, shadow=True)
ax.grid(color='black', linestyle='-.', linewidth=1.0, axis='x', alpha=0.9)

for spine in ax.spines.values():
    spine.set_edgecolor('darkslategray')
    spine.set_linewidth(2)

plt.tight_layout()
plt.show()
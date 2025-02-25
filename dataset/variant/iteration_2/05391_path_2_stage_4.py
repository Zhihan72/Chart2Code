import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
food_categories = ["Grains", "Citrus", "Greens", "Milk"]
cereals = [300, 320, 280, 460, 480, 340, 360, 380, 400, 420, 440]
fruits = [90, 100, 55, 50, 130, 140, 120, 60, 110, 70, 80]
vegetables = [140, 105, 100, 170, 180, 160, 115, 110, 130, 150, 120]
dairy = [160, 152, 155, 190, 175, 170, 180, 150, 185, 157, 165]

food_production = np.vstack([cereals, fruits, vegetables, dairy])

fig, ax = plt.subplots(figsize=(12, 8))
single_color = '#4682B4'
ax.stackplot(years, food_production, labels=food_categories, colors=[single_color]*len(food_categories), alpha=0.85)

ax.set_title('Agroland’s Yield Path\n2010-2020', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline', fontsize=12)
ax.set_ylabel('Output (M Tonnes)', fontsize=12)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

ax.legend(title='Divisions', loc='upper right', fontsize=10, frameon=True, shadow=True)
ax.grid(color='black', linestyle='-.', linewidth=1.0, axis='x', alpha=0.9)

for spine in ax.spines.values():
    spine.set_edgecolor('darkslategray')
    spine.set_linewidth(2)

plt.tight_layout()
plt.show()
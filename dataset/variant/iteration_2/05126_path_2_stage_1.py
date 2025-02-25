import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)
plant_based = np.array([20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50])
meat = np.array([30, 28, 26, 25, 23, 21, 20, 18, 16, 15, 14])
dairy = np.array([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10])
processed_food = np.array([10, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22])
insects = np.array([20, 18, 16, 14, 13, 12, 10, 9, 8, 6, 4])

fig, ax = plt.subplots(figsize=(14, 9))

ax.stackplot(years, plant_based, meat, dairy, processed_food, insects,
             labels=['Plant-Based Foods', 'Meat', 'Dairy Products', 
                     'Processed Food', 'Insects'],
             colors=['#8DD3C7'], alpha=0.8)

ax.set_title("Evolution of Food Preferences in Gastronia (2020-2030)", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Proportion of Consumption (%)', fontsize=14)
ax.legend(loc='upper left', fontsize=12, bbox_to_anchor=(1, 1))
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_xticks(np.arange(2020, 2031))
ax.tick_params(axis='x', rotation=45)
ax.annotate('Rise of Plant-Based Foods', xy=(2025, 35), xytext=(2027, 70),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), fontsize=12, color='green')
ax.annotate('Decline in Insect Consumption', xy=(2028, 4), xytext=(2026, 20),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), fontsize=12, color='blue')

plt.tight_layout()
plt.show()
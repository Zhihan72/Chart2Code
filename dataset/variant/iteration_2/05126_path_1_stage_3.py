import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)

# Updated datasets for food categories
plant_based = np.array([20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50])
meat = np.array([30, 28, 26, 25, 23, 21, 20, 18, 16, 15, 14])
dairy = np.array([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10])
processed_food = np.array([10, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22])

fig, ax = plt.subplots(figsize=(14, 9))

# Stacked area plot
ax.stackplot(years, plant_based, meat, dairy, processed_food,
             colors=['#8DD3C7', '#FFFFB3', '#BEBADA', '#FB8072'], alpha=0.8)

ax.set_title("Food Preferences (2020-2030)", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Consumption (%)', fontsize=14)

ax.set_xticks(np.arange(2020, 2031))
ax.tick_params(axis='x', rotation=45)

# Added milestone annotation
ax.annotate('Rise of Plant-Based', xy=(2025, 35), xytext=(2027, 70),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), fontsize=12, color='green')

plt.tight_layout()
plt.show()
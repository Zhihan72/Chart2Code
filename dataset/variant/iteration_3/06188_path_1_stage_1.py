import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2025, 2036)

# Randomly altered diet preference data (manually mixed while preserving original structure)
fruits = [22, 20, 25, 27, 29, 31, 33, 35, 37, 40, 42]
vegetables = [16, 15, 18, 19, 23, 20, 24, 25, 26, 28, 30]
grains = [12, 11, 10, 13, 14, 16, 15, 17, 18, 19, 20]
dairy = [23, 24, 25, 21, 21, 22, 20, 19, 18, 17, 17]
proteins = [27, 30, 24, 25, 28, 22, 21, 20, 19, 18, 17]

plt.figure(figsize=(14, 8))
plt.stackplot(years, fruits, vegetables, grains, dairy, proteins, 
              labels=['Fruits', 'Vegetables', 'Grains', 'Dairy', 'Proteins'], 
              colors=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700'], alpha=0.8)

plt.title('Evolution of Dietary Preferences (2025-2035)\nCommunity Nutrition Trends', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12, fontweight='bold', color='darkslategray')
plt.ylabel('Diet Composition (Arbitrary Units)', fontsize=12, fontweight='bold', color='darkslategray')

plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Dietary Sources', fontsize=10)
plt.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

annotations = {
    2027: 'Increased Vegetable Consumption',
    2030: 'Popularity Boost of Fruits',
    2033: 'Dairy Consumption Decline'
}

for year, text in annotations.items():
    total_amount = sum([fruits[year-2025], vegetables[year-2025], grains[year-2025], dairy[year-2025], proteins[year-2025]])
    plt.annotate(text, xy=(year, total_amount), xytext=(year, total_amount + 5),
                 arrowprops=dict(facecolor='black', arrowstyle='->'),
                 fontsize=10, ha='center', color='darkred', backgroundcolor='white')

plt.tight_layout()
plt.show()
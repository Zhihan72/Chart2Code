import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2025, 2036)

# Diet preference data
fruits = [22, 20, 25, 27, 29, 31, 33, 35, 37, 40, 42]
vegetables = [16, 15, 18, 19, 23, 20, 24, 25, 26, 28, 30]
grains = [12, 11, 10, 13, 14, 16, 15, 17, 18, 19, 20]
dairy = [23, 24, 25, 21, 21, 22, 20, 19, 18, 17, 17]
proteins = [27, 30, 24, 25, 28, 22, 21, 20, 19, 18, 17]

plt.figure(figsize=(14, 8))
plt.stackplot(years, fruits, vegetables, grains, dairy, proteins, 
              labels=['Fruits', 'Veg', 'Grains', 'Dairy', 'Protein'], 
              colors=['#FF5733', '#33FF57', '#3357FF', '#DAF7A6', '#FFC300'], alpha=0.8)

plt.title('Diet Trends (2025-2035)', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12, fontweight='bold', color='darkslategray')
plt.ylabel('Units', fontsize=12, fontweight='bold', color='darkslategray')

plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Sources', fontsize=10)
plt.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

annotations = {
    2027: 'More Veggies',
    2030: 'Fruits Rise',
    2033: 'Dairy Down'
}

for year, text in annotations.items():
    total_amount = sum([fruits[year-2025], vegetables[year-2025], grains[year-2025], dairy[year-2025], proteins[year-2025]])
    plt.annotate(text, xy=(year, total_amount), xytext=(year, total_amount + 5),
                 arrowprops=dict(facecolor='black', arrowstyle='->'),
                 fontsize=10, ha='center', color='darkred', backgroundcolor='white')

plt.tight_layout()
plt.show()
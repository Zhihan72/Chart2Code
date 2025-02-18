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
              colors=['#FF5733', '#33FF57', '#3357FF', '#DAF7A6', '#FFC300'], alpha=0.75)

plt.title('Diet Trends (2025-2035)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Year', fontsize=12, fontweight='bold', color='navy')
plt.ylabel('Consumption (Units)', fontsize=12, fontweight='bold', color='navy')

plt.legend(loc='upper right', shadow=True, title='Diet Types', fontsize=9)
plt.grid(True, linestyle='-.', which='major', color='black', alpha=0.5)

annotations = {
    2027: 'Veggie Surge',
    2030: 'Fruit Boost',
    2033: 'Dairy Decline'
}

for year, text in annotations.items():
    total_amount = sum([fruits[year-2025], vegetables[year-2025], grains[year-2025], dairy[year-2025], proteins[year-2025]])
    plt.annotate(text, xy=(year, total_amount), xytext=(year, total_amount + 5),
                 arrowprops=dict(facecolor='green', arrowstyle='-[', shrinkB=10),
                 fontsize=10, ha='right', color='purple', backgroundcolor='yellow')

plt.tight_layout()
plt.show()
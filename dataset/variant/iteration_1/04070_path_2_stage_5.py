import matplotlib.pyplot as plt
import numpy as np

countries = np.array(['USA', 'China', 'Ger', 'Bra', 'India', 'UK', 'Fra', 'Aus', 'Canada', 'Jap'])
urban_parks = np.array([1300, 2900, 850, 750, 500, 1050, 980, 820, 740, 1250])

sorted_indices = np.argsort(urban_parks)[::-1]
sorted_countries = countries[sorted_indices]
sorted_urban_parks = urban_parks[sorted_indices]

fig, ax = plt.subplots(figsize=(14, 8))
ax.bar(sorted_countries, sorted_urban_parks, color='green', alpha=0.8, edgecolor='darkgreen', linestyle='dashed')

ax.set_title('Countries by Number of Parks (Descending)', fontsize=18, fontweight='bold', pad=20, loc='left')
ax.set_xlabel('Countries', fontsize=14, fontweight='light')
ax.set_ylabel('Parks Count', fontsize=14, fontweight='light')

for index, value in enumerate(sorted_urban_parks):
    ax.text(index, value + 50, str(value), fontsize=12, ha='center', color='darkred', style='italic')

ax.grid(False)
plt.xticks(fontsize=10, rotation=60, ha='right')
plt.yticks(fontsize=10)

plt.tight_layout()
plt.show()
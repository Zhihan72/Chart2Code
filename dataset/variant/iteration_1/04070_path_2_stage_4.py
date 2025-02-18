import matplotlib.pyplot as plt
import numpy as np

countries = np.array(['USA', 'China', 'Ger', 'Bra', 'India', 'UK', 'Fra', 'Aus', 'Canada', 'Jap'])
urban_parks = np.array([1300, 2900, 850, 750, 500, 1050, 980, 820, 740, 1250])

# Sort indices based on urban parks in descending order
sorted_indices = np.argsort(urban_parks)[::-1]
sorted_countries = countries[sorted_indices]
sorted_urban_parks = urban_parks[sorted_indices]

fig, ax = plt.subplots(figsize=(14, 8))
ax.bar(sorted_countries, sorted_urban_parks, color='blue', alpha=0.6, edgecolor='black')

ax.set_title('Countries by Number of Parks (Descending)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Countries', fontsize=14)
ax.set_ylabel('Parks Count', fontsize=14)

for index, value in enumerate(sorted_urban_parks):
    ax.text(index, value + 30, str(value), fontsize=10, ha='center', color='black')

ax.grid(True, linestyle='--', alpha=0.7)
plt.xticks(fontsize=12, rotation=45, ha='right')
plt.yticks(fontsize=12)

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import numpy as np

original_cities = np.arange(1, 11)
green_space_per_capita_orig = np.array([15, 30, 25, 40, 50, 32, 22, 60, 45, 35])
happiness_index_orig = np.array([6.0, 7.5, 7.0, 8.0, 9.0, 7.2, 6.5, 9.5, 8.2, 7.8])

additional_cities = np.arange(11, 21)
green_space_per_capita_add = np.array([10, 28, 24, 38, 48, 30, 20, 58, 42, 33])
happiness_index_add = np.array([5.5, 7.0, 6.8, 7.8, 8.8, 7.0, 6.3, 9.3, 8.0, 7.5])

plt.figure(figsize=(12, 7))
plt.scatter(green_space_per_capita_orig, happiness_index_orig, color='royalblue', edgecolors='black', s=150, alpha=0.7)
plt.scatter(green_space_per_capita_add, happiness_index_add, color='forestgreen', edgecolors='black', s=150, alpha=0.7)

for i, city in enumerate(original_cities):
    plt.annotate(f'Area {city}', 
                 (green_space_per_capita_orig[i], happiness_index_orig[i]),
                 textcoords="offset points",
                 xytext=(5, 5),
                 ha='center', fontsize=10, color='darkblue')

for i, city in enumerate(additional_cities):
    plt.annotate(f'Region {city}', 
                 (green_space_per_capita_add[i], happiness_index_add[i]),
                 textcoords="offset points",
                 xytext=(5, 5),
                 ha='center', fontsize=10, color='black')

plt.title("Relationship Between Urban Green Areas and Well-being Index\n Overview of Various Metropolitan Areas", fontsize=16, fontweight='bold')
plt.xlabel("Urban Green Areas per Resident (sqm)", fontsize=13)
plt.ylabel("Overall Well-being Index (scale 1-10)", fontsize=13)

m_orig, b_orig = np.polyfit(green_space_per_capita_orig, happiness_index_orig, 1)
plt.plot(green_space_per_capita_orig, m_orig * green_space_per_capita_orig + b_orig, color='firebrick', linestyle='--', linewidth=2)

m_add, b_add = np.polyfit(green_space_per_capita_add, happiness_index_add, 1)
plt.plot(green_space_per_capita_add, m_add * green_space_per_capita_add + b_add, color='darkorange', linestyle='--', linewidth=2)

for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()
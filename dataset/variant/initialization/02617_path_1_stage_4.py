import matplotlib.pyplot as plt

crops = ['Wheat', 'Corn', 'Rice', 'Soy', 'Cott']
wheat_yield = [3.1, 2.8, 3.0, 3.3, 2.4, 3.5, 2.5, 3.2, 2.7, 2.9]
corn_yield = [5.2, 5.0, 6.0, 5.8, 5.1, 5.4, 6.2, 5.3, 5.5, 5.7]
rice_yield = [4.6, 4.5, 4.3, 4.1, 4.0, 4.2, 4.8, 4.4, 4.5, 4.0]
soy_yield = [3.6, 3.5, 3.3, 3.7, 3.2, 3.1, 3.0, 3.9, 3.4, 3.8]
cotton_yield = [2.1, 2.3, 1.8, 2.0, 2.2, 1.9, 2.5, 2.0, 2.4, 2.1]

data = [wheat_yield, corn_yield, rice_yield, soy_yield, cotton_yield]

fig, ax = plt.subplots(figsize=(10, 7))
ax.boxplot(data, vert=False, patch_artist=True, showmeans=True, notch=True)

ax.set_yticklabels(crops)
ax.set_xlabel('Yield (t/ha)')
ax.set_ylabel('Crop')

plt.tight_layout()
plt.show()
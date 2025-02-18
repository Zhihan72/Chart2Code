import matplotlib.pyplot as plt

# Datasets for lifespans of different electronics
smartphones_lifespan = [2.5, 3, 2.8, 3.2, 2.9, 3.5, 3.1, 2.6, 3, 3.3]
tablets_lifespan = [3.5, 3.7, 4, 3.8, 3.6, 3.9, 3.5, 3.6, 3.8, 3.7]
laptops_lifespan = [4.5, 4.8, 5, 4.7, 4.6, 4.9, 4.8, 4.5, 4.7, 4.9]

data = [smartphones_lifespan, tablets_lifespan, laptops_lifespan]

fig, ax = plt.subplots(figsize=(8, 6))

boxes = ax.boxplot(data, vert=True, patch_artist=True, notch=False,
                   boxprops=dict(facecolor='skyblue'),
                   whiskerprops=dict(color='skyblue'),
                   capprops=dict(color='skyblue'),
                   medianprops=dict(color='blue'))

ax.set_xticklabels(['Smartphones', 'Tablets', 'Laptops'])

ax.grid(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()
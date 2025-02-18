import matplotlib.pyplot as plt

# Define the lifespan data for each device category in years
smartphones_lifespan = [2.5, 3, 2.8, 3.2, 2.9, 3.5, 3.1, 2.6, 3, 3.3]
laptops_lifespan = [4, 4.5, 3.8, 5, 4.2, 4.7, 4.1, 4.4, 5.1, 4.8]
tablets_lifespan = [3, 3.5, 3.2, 4, 3.1, 3.8, 3.9, 3.3, 3.6, 3.7]
wearables_lifespan = [1.5, 2, 1.8, 1.9, 2.1, 2.2, 1.7, 1.6, 2, 1.4]

data = [smartphones_lifespan, laptops_lifespan, tablets_lifespan, wearables_lifespan]
devices = ['Smartphones', 'Laptops', 'Tablets', 'Wearables']

fig, ax = plt.subplots(figsize=(10, 6))
boxes = ax.boxplot(data, vert=False, patch_artist=True, notch=True, 
                   boxprops=dict(facecolor='#FFDDC1', color='black'), 
                   whiskerprops=dict(color='black'), 
                   capprops=dict(color='black'), 
                   medianprops=dict(color='red'))

# Define a new set of colors
new_colors = ['#8B0000', '#00008B', '#006400', '#8B008B']
for patch, color in zip(boxes['boxes'], new_colors):
    patch.set_facecolor(color)

ax.set_title('Tech Device Lifespan Analysis:\nDurability of Popular Gadgets (2023)', fontsize=14, weight='bold', pad=20)
ax.set_xlabel('Lifespan (years)', fontsize=12)
ax.set_yticklabels(devices, fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
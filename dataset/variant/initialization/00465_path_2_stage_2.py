import matplotlib.pyplot as plt

smartphones_lifespan = [2.5, 3, 2.8, 3.2, 2.9, 3.5, 3.1, 2.6, 3, 3.3]
laptops_lifespan = [4, 4.5, 3.8, 5, 4.2, 4.7, 4.1, 4.4, 5.1, 4.8]
tablets_lifespan = [3, 3.5, 3.2, 4, 3.1, 3.8, 3.9, 3.3, 3.6, 3.7]
wearables_lifespan = [1.5, 2, 1.8, 1.9, 2.1, 2.2, 1.7, 1.6, 2, 1.4]

data = [smartphones_lifespan, laptops_lifespan, tablets_lifespan, wearables_lifespan]

fig, ax = plt.subplots(figsize=(10, 6))

# Plot with changed properties: linestyle, facecolor, etc.
boxes = ax.boxplot(data, vert=False, patch_artist=True, notch=False, 
                   boxprops=dict(facecolor='#AEC6CF', linestyle='-.'),
                   whiskerprops=dict(color='orange', linestyle='-.'), 
                   capprops=dict(color='orange', linestyle='-'), 
                   medianprops=dict(color='purple', marker='o'))

# Randomly adjust colors
colors = ['#FDD9B5', '#77DD77', '#FFB347', '#B39EB5']
for patch, color in zip(boxes['boxes'], colors):
    patch.set_facecolor(color)

# Remove grid for contrast
ax.grid(False)

# Adjust borders and ticks visibility
ax.spines['top'].set_visible(False)
ax.spines['right'].set_linewidth(2)
ax.spines['bottom'].set_color('gray')
ax.spines['left'].set_linestyle('--')

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt

smartphones_lifespan = [2.5, 3, 2.8, 3.2, 2.9, 3.5, 3.1, 2.6, 3, 3.3]

fig, ax = plt.subplots(figsize=(6, 8))

boxes = ax.boxplot(smartphones_lifespan, vert=True, patch_artist=True, notch=False, 
                   boxprops=dict(facecolor='#AEC6CF'),
                   whiskerprops=dict(color='orange'), 
                   capprops=dict(color='orange'), 
                   medianprops=dict(color='purple'))

ax.grid(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()
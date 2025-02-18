import matplotlib.pyplot as plt

# Modified content within the lifespan data while preserving dimensional structure
all_devices_lifespan = [3.8, 5, 4.2, 2.5, 3.3, 4, 3.5, 3.2, 4.5, 3, 
                        3.1, 4.7, 4.1, 2.6, 5.1, 4.4, 4.8, 2.9, 3, 3.2, 
                        3, 1.9, 2.1, 3.1, 2.2, 3.8, 1.5, 3.6, 3.7, 3.9, 
                        1.8, 2, 1.4, 2, 3.5, 3.3, 1.7, 2.8, 1.6, 3.7]

fig, ax = plt.subplots(figsize=(6, 8))
ax.boxplot(all_devices_lifespan, vert=True, patch_artist=True, 
           boxprops=dict(facecolor='#FFDDC1', color='black'), 
           whiskerprops=dict(color='black'), 
           capprops=dict(color='black'), 
           medianprops=dict(color='red'))

# Randomly altered textual elements
titles = ['Super Gadget Life', 'Lifespan Overview', 'Longevity of Devices']
y_labels = ['Years of Service', 'Functional Period (years)', 'Uptime in Years']
x_labels = ['Devices', 'Tech Gadgets', 'All Units']

ax.set_title(titles[1], fontsize=14, weight='bold', pad=20)
ax.set_ylabel(y_labels[2], fontsize=12)
ax.set_xticklabels([x_labels[0]], fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt

# Define the lifespan data for a single category in years
all_devices_lifespan = [2.5, 3, 2.8, 3.2, 2.9, 3.5, 3.1, 2.6, 3, 3.3, 
                        4, 4.5, 3.8, 5, 4.2, 4.7, 4.1, 4.4, 5.1, 4.8, 
                        3, 3.5, 3.2, 4, 3.1, 3.8, 3.9, 3.3, 3.6, 3.7, 
                        1.5, 2, 1.8, 1.9, 2.1, 2.2, 1.7, 1.6, 2, 1.4]

fig, ax = plt.subplots(figsize=(6, 8))
ax.boxplot(all_devices_lifespan, vert=True, patch_artist=True, 
           boxprops=dict(facecolor='#FFDDC1', color='black'), 
           whiskerprops=dict(color='black'), 
           capprops=dict(color='black'), 
           medianprops=dict(color='red'))

ax.set_title('Combined Device Lifespan', fontsize=14, weight='bold', pad=20)
ax.set_ylabel('Lifespan (years)', fontsize=12)
ax.set_xticklabels(['All Devices'], fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
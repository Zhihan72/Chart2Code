import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2010, 2023)

# Organic produce data (in metric tons)
region_a_produce = [200, 250, 300, 350, 400, 450, 550, 600, 650, 700, 750, 800, 850]
region_b_produce = [100, 150, 200, 300, 400, 500, 600, 700, 900, 950, 1000, 1050, 1100]
region_c_produce = [50, 75, 100, 125, 150, 200, 300, 350, 400, 450, 500, 600, 700]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the area chart with new colors
ax.stackplot(years, region_a_produce, region_b_produce, region_c_produce, 
             labels=['Zone X', 'Sector Y', 'Area Z'], 
             colors=['#76c7c0', '#f7a8b8', '#ffe082'], alpha=0.7)

# Adding titles and labels
ax.set_title('Harvest Trends: The Rise of Organic Deliveries\n2010-2022', fontsize=18, fontweight='bold')
ax.set_xlabel('Timeline', fontsize=14)
ax.set_ylabel('Organic Supplies Shipped (Metric Tons)', fontsize=14)

# Adding customizations
ax.set_xticks(years)
ax.yaxis.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper left', title='Locations', fontsize=12)
ax.tick_params(axis='x', labelrotation=45)

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2010, 2023)

# Manually shuffled organic produce data (in metric tons)
region_a_produce = [300, 250, 200, 350, 450, 400, 550, 600, 800, 700, 850, 750, 650]
region_b_produce = [200, 300, 100, 400, 150, 500, 600, 700, 1100, 900, 950, 1000, 1050]
region_c_produce = [75, 50, 100, 125, 200, 150, 600, 300, 450, 350, 400, 500, 700]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the area chart
ax.stackplot(years, region_a_produce, region_b_produce, region_c_produce, 
             labels=['A', 'B', 'C'], 
             colors=['#2ca02c', '#ff7f0e', '#1f77b4'], alpha=0.7)

# Titles and labels
ax.set_title('Organic Produce Growth 2010-22', fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Tons Delivered', fontsize=14)

# Customizations
ax.set_xticks(years)
ax.yaxis.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper left', title='Regions', fontsize=12)
ax.tick_params(axis='x', labelrotation=45)

# Optimize layout
plt.tight_layout()

# Show the plot
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Backstory: Our fictional chart describes the gradual emergence of "Farm-to-Table Revolution."
# This initiative encourages organic farming and direct consumption, with three key regions actively adopting it.
# The chart showcases data from 2010 to 2022 highlighting the growth of organic produce (in metric tons) 
# delivered from farms directly to markets in each region over the years.

# Data
years = np.arange(2010, 2023)

# Organic produce data (in metric tons)
region_a_produce = [200, 250, 300, 350, 400, 450, 550, 600, 650, 700, 750, 800, 850]
region_b_produce = [100, 150, 200, 300, 400, 500, 600, 700, 900, 950, 1000, 1050, 1100]
region_c_produce = [50, 75, 100, 125, 150, 200, 300, 350, 400, 450, 500, 600, 700]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the area chart
ax.stackplot(years, region_a_produce, region_b_produce, region_c_produce, 
             labels=['Region A', 'Region B', 'Region C'], 
             colors=['#2ca02c', '#ff7f0e', '#1f77b4'], alpha=0.7)

# Adding titles and labels
ax.set_title('Farm-to-Table Revolution: Growth of Organic Produce Delivery\n2010-2022', fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Organic Produce Delivered (Metric Tons)', fontsize=14)

# Adding customizations
ax.set_xticks(years)
ax.yaxis.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper left', title='Regions', fontsize=12)
ax.tick_params(axis='x', labelrotation=45)

# Ensure layout is optimized
plt.tight_layout()

# Show the plot
plt.show()
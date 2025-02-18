import matplotlib.pyplot as plt
import numpy as np

# Updated regions and corresponding data after removing 'Eastland'
regions = ['Northland', 'Southland', 'Westland', 'Central']
population_percentages = [16, 24, 18, 22]
demographics_labels = ['Children (<18)', 'Adults (18-64)', 'Seniors (65+)']
demographics_data = {
    'Children (<18)': [12, 14, 18, 16],
    'Adults (18-64)': [56, 64, 52, 54],
    'Seniors (65+)': [32, 22, 30, 30]
}

# Updated colors
region_colors = ['#66b3ff', '#ffcc99', '#ff9999', '#99ff99']
demographic_colors = ['#ff7f00', '#4daf4a', '#377eb8']

fig, ax = plt.subplots(1, 2, figsize=(14, 8))

# Plot pie charts for demographics within each updated region
for i, region in enumerate(regions):
    demographic_data = [demographics_data[label][i] for label in demographics_labels]
    ax[0].pie(
        demographic_data, colors=demographic_colors, startangle=140, wedgeprops=dict(edgecolor='white', width=0.3)
    )

# Create pie chart for updated population distribution by region
ax[1].pie(
    population_percentages, colors=region_colors, startangle=140,
    wedgeprops=dict(edgecolor='white'), explode=(0.05, 0.05, 0.05, 0.05), pctdistance=0.85
)

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Shuffled regions and corresponding data
regions = ['Central', 'Westland', 'Northland', 'Southland']
population_percentages = [22, 18, 16, 24]

# Shuffled demographics labels and data
demographics_labels = ['Seniors (65+)', 'Children (<18)', 'Adults (18-64)']
demographics_data = {
    'Seniors (65+)': [30, 30, 32, 22],
    'Children (<18)': [16, 18, 12, 14],
    'Adults (18-64)': [54, 52, 56, 64]
}

region_colors = ['#66b3ff', '#ffcc99', '#ff9999', '#99ff99']
demographic_colors = ['#ff7f00', '#4daf4a', '#377eb8']

fig, ax = plt.subplots(1, 2, figsize=(14, 8))

# Plot pie charts for demographics within randomly shuffled regions
for i, region in enumerate(regions):
    demographic_data = [demographics_data[label][i] for label in demographics_labels]
    ax[0].pie(
        demographic_data, colors=demographic_colors, startangle=140, 
        wedgeprops=dict(edgecolor='white', width=0.3)
    )
    ax[0].set_title(f'Demographic Distribution in {region}')

# Create pie chart for shuffled population distribution by region
ax[1].pie(
    population_percentages, colors=region_colors, startangle=140,
    wedgeprops=dict(edgecolor='white'), explode=(0.05, 0.05, 0.05, 0.05), pctdistance=0.85
)
ax[1].set_title('Region-wise Population')

plt.tight_layout()
plt.show()
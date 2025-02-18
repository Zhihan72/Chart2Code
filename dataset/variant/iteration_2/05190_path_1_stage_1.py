import matplotlib.pyplot as plt

# Updated data for an imaginary country with more regions
regions = ['Northland', 'Southland', 'Eastland', 'Westland', 'Central', 'Highland', 'Lowland']
population_percentages = [14, 20, 18, 16, 18, 5, 9]
demographics_labels = ['Children (<18)', 'Adults (18-64)', 'Seniors (65+)']
demographics_data = {
    'Children (<18)': [12, 14, 22, 18, 16, 10, 22],
    'Adults (18-64)': [56, 64, 48, 52, 54, 50, 60],
    'Seniors (65+)': [32, 22, 30, 30, 30, 40, 18]
}

# Updated colors
region_colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c2f0c2']
demographic_colors = ['#4daf4a', '#377eb8', '#ff7f00']

fig, ax = plt.subplots(1, 2, figsize=(14, 8))

# Pie chart for population distribution by region
ax[0].pie(
    population_percentages, labels=regions, colors=region_colors, autopct='%1.1f%%', startangle=140,
    wedgeprops=dict(edgecolor='white'), explode=[0.05]*len(regions), pctdistance=0.85
)
ax[0].set_title('Population Distribution by Region', fontsize=14, fontweight='bold')

# Pie charts for demographics within each region
all_wedges = []
for i, region in enumerate(regions):
    demographic_data = [demographics_data[label][i] for label in demographics_labels]
    wedges, _ = ax[1].pie(
        demographic_data, colors=demographic_colors, startangle=140, wedgeprops=dict(edgecolor='white', width=0.3)
    )
    all_wedges.extend(wedges)

# Updated legend
ax[1].legend(all_wedges[:3], demographics_labels, title="Demographics", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
ax[1].set_title('Demographic Distribution within Regions', fontsize=14, fontweight='bold')

fig.suptitle('Extended Regional and Demographic Distribution in Imaginaryland', fontsize=18, fontweight='bold', y=0.98)
plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt

regions = ['Northland', 'Southland', 'Eastland', 'Westland', 'Central', 'Highland', 'Lowland']
population_percentages = [14, 20, 18, 16, 18, 5, 9]
demographics_labels = ['Children (<18)', 'Adults (18-64)', 'Seniors (65+)']
demographics_data = {
    'Children (<18)': [12, 14, 22, 18, 16, 10, 22],
    'Adults (18-64)': [56, 64, 48, 52, 54, 50, 60],
    'Seniors (65+)': [32, 22, 30, 30, 30, 40, 18]
}

# Manually shuffled colors for regions
region_colors = ['#66b3ff', '#ffcc99', '#ff9999', '#c2f0c2', '#ffb3e6', '#99ff99', '#c2c2f0']  # Shuffled

# Manually shuffled colors for demographics
demographic_colors = ['#377eb8', '#ff7f00', '#4daf4a']  # Shuffled

fig, ax = plt.subplots(1, 2, figsize=(14, 8))

all_wedges = []
for i, region in enumerate(regions):
    demographic_data = [demographics_data[label][i] for label in demographics_labels]
    wedges, _ = ax[0].pie(
        demographic_data, colors=demographic_colors, startangle=140, wedgeprops=dict(edgecolor='white', width=0.3)
    )
    all_wedges.extend(wedges)
ax[0].legend(all_wedges[:3], demographics_labels, title="Demographics", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
ax[0].set_title('Demographic Distribution within Regions', fontsize=14, fontweight='bold')

ax[1].pie(
    population_percentages, labels=regions, colors=region_colors, autopct='%1.1f%%', startangle=140,
    wedgeprops=dict(edgecolor='white'), explode=[0.05]*len(regions), pctdistance=0.85
)
ax[1].set_title('Population Distribution by Region', fontsize=14, fontweight='bold')

fig.suptitle('Extended Regional and Demographic Distribution in Imaginaryland', fontsize=18, fontweight='bold', y=0.98)
plt.tight_layout()
plt.show()
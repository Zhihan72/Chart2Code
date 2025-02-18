import matplotlib.pyplot as plt
import numpy as np

countries = ['CH', 'DE', 'UK', 'USA', 'FR']
choco_2015 = [9.0, 8.4, 8.2, 5.5, 6.5]
choco_2020 = [10.1, 9.2, 8.5, 6.2, 7.0]

# Sorting data for 2015
sorted_indices_2015 = np.argsort(choco_2015)
sorted_choco_2015 = np.array(choco_2015)[sorted_indices_2015]
sorted_countries_2015 = np.array(countries)[sorted_indices_2015]

# Sorting data for 2020
sorted_indices_2020 = np.argsort(choco_2020)
sorted_choco_2020 = np.array(choco_2020)[sorted_indices_2020]
sorted_countries_2020 = np.array(countries)[sorted_indices_2020]

fig, ax = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

# Plotting 2015 consumption
locs_2015 = np.arange(len(sorted_countries_2015))
bars_2015 = ax[0].bar(locs_2015, sorted_choco_2015, color='darkorange', edgecolor='midnightblue', label='2015', linestyle='-')
ax[0].set_ylabel('Kg per Capita', fontsize=12)
ax[0].set_title('Choco Consumption, 2015', fontsize=14, fontweight='bold')
ax[0].legend(loc='lower left', fontsize=10)
ax[0].grid(axis='y', linestyle=':', alpha=0.5)

# Annotating values on bars
for bar in bars_2015:
    ax[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, f'{bar.get_height():.1f}',
               ha='center', va='bottom', fontsize=10, color='midnightblue')

# Plotting 2020 consumption
locs_2020 = np.arange(len(sorted_countries_2020))
bars_2020 = ax[1].bar(locs_2020, sorted_choco_2020, color='tomato', edgecolor='teal', label='2020', linestyle='--')
ax[1].set_ylabel('Kg per Capita', fontsize=12)
ax[1].set_title('Choco Consumption, 2020', fontsize=14, fontweight='bold')
ax[1].legend(loc='lower right', fontsize=10)
ax[1].grid(axis='y', linestyle='-', alpha=0.3)

# Annotating values on bars
for bar in bars_2020:
    ax[1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, f'{bar.get_height():.1f}',
               ha='center', va='bottom', fontsize=10, color='teal')

# Set shared x-axis labels
ax[1].set_xticks(locs_2020)
ax[1].set_xticklabels(sorted_countries_2020, rotation=45, ha='right', fontsize=12)

fig.text(0.5, 0.04, 'Country', ha='center', fontsize=12)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()
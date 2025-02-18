import matplotlib.pyplot as plt
import numpy as np

# Backstory: Annual Distribution of Meteor Showers Over the Past Decade
# This chart is designed to visualize the frequency of meteor showers observed annually over the past ten years. Astronomy clubs have meticulously recorded these observations.

# Data
years = list(range(2011, 2021))  # Years from 2011 to 2020
monthly_observations = [
    [2, 3, 1, 5, 6, 4, 3, 5, 6, 7, 9, 10],    # 2011
    [1, 0, 4, 3, 7, 6, 8, 9, 10, 12, 6, 5],   # 2012
    [7, 8, 10, 6, 5, 4, 9, 10, 11, 12, 6, 7], # 2013
    [2, 4, 3, 5, 6, 1, 3, 5, 7, 8, 9, 11],    # 2014
    [6, 8, 7, 5, 4, 3, 9, 10, 8, 7, 4, 5],    # 2015
    [4, 2, 3, 7, 9, 6, 5, 8, 7, 6, 8, 9],     # 2016
    [8, 9, 7, 6, 8, 5, 4, 6, 8, 10, 7, 5],    # 2017
    [5, 4, 3, 7, 9, 8, 7, 6, 10, 12, 9, 8],   # 2018
    [2, 3, 1, 5, 6, 4, 3, 5, 6, 7, 8, 7],     # 2019
    [4, 6, 5, 7, 8, 4, 6, 9, 10, 11, 9, 8]    # 2020
]

# Flattening and constructing data
all_months = np.concatenate(monthly_observations)
months = np.tile(np.arange(1, 13), len(years))

# Create a figure with a histogram and a scatter plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

# Subplot 1: Histogram for distribution of meteor showers across the entire decade
ax1.hist(all_months, bins=12, color='steelblue', edgecolor='black', alpha=0.7)
ax1.set_title("Annual Distribution of Meteor Showers\n(2011-2020)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Month", fontsize=14)
ax1.set_ylabel("Number of Meteor Showers", fontsize=14)
ax1.set_xticks(np.arange(1, 13))
ax1.set_xticklabels([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])
ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Subplot 2: Scatter plot for annual observations
for i, (year, observations) in enumerate(zip(years, monthly_observations)):
    months = np.arange(1, 13) + i * 0.1  # Small offset to avoid overlap
    ax2.scatter(months, observations, label=f'{year}', s=50, alpha=0.7)

ax2.set_title("Meteor Showers Recorded Monthly\nPer Year from 2011 to 2020", fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel("Month", fontsize=14)
ax2.set_ylabel("Number of Meteor Showers", fontsize=14)
ax2.set_xticks(np.arange(1, 13))
ax2.set_xticklabels([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])
ax2.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)
ax2.legend(title="Year", fontsize=10, title_fontsize='13', loc='upper right', edgecolor='black')

# Adjust the layout
plt.tight_layout()

# Display the plots
plt.show()
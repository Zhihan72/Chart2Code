import matplotlib.pyplot as plt
import numpy as np

# Define regions and years
regions = ['Americas', 'Europe', 'Asia', 'Africa']  # Removed 'Oceania'
years = ['2010', '2015', '2020']

# Internet users data (in millions) for each region over the years
internet_users = [
    [500, 800, 1100],  # Americas
    [400, 700, 1000],  # Europe
    [1000, 1600, 2300], # Asia
    [200, 400, 700]    # Africa
    # Removed data for 'Oceania'
]

# Colors for each region
colors = ['#0077b6', '#00b4d8', '#90e0ef', '#48cae4']  # Removed color for 'Oceania'

# Plot setup
fig, ax = plt.subplots(figsize=(14, 8))

# Calculate bar positions and width
bar_width = 0.15
ind = np.arange(len(years))

# Plotting the bars
for i, (region, color) in enumerate(zip(regions, colors)):
    bar_positions = ind + i * bar_width
    bars = ax.bar(bar_positions, internet_users[i], bar_width, color=color, label=region)
    
    # Add the data labels on top of the bars
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}M',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9, fontweight='bold')

# Configure the x-axis
ax.set_xlabel('Year', fontsize=12)
ax.set_xticks(ind + bar_width * (len(regions) - 1) / 2)
ax.set_xticklabels(years, fontsize=12)
ax.set_ylabel('Internet Users (in millions)', fontsize=12)
ax.set_title('Growth of Internet Users (2010-2020)', fontsize=16, fontweight='bold')

# Add legend and grid for better readability
ax.legend(title='Regions', fontsize=10, title_fontsize='12', bbox_to_anchor=(1.05, 1), loc='upper left')
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
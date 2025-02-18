import matplotlib.pyplot as plt
import numpy as np

# Backstory: Comparing Coffee Consumption Trends Among Different Age Groups Over a Decade (2010-2020)

# Years of interest
years = np.arange(2010, 2021)

# Coffee consumption data in thousand cups per day for different age groups
age_18_25 = np.array([20, 22, 25, 30, 35, 40, 45, 50, 55, 60, 65])
age_26_35 = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
age_36_50 = np.array([40, 42, 45, 47, 50, 53, 56, 59, 62, 65, 70])
age_51_65 = np.array([15, 18, 20, 22, 25, 28, 30, 32, 35, 38, 40])
age_65_above = np.array([10, 12, 14, 16, 18, 20, 23, 25, 27, 30, 32])

# Stack the consumption data
consumption_data = np.vstack([age_18_25, age_26_35, age_36_50, age_51_65, age_65_above])

# Set up the plot
plt.figure(figsize=(14, 9))

# Define colors for different age groups
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

# Create the stacked area plot
plt.stackplot(years, consumption_data, labels=['18-25', '26-35', '36-50', '51-65', '65+'], colors=colors, alpha=0.8)

# Set titles and labels with line breaks for better readability
plt.title('Decadal Coffee Consumption Trends\nAcross Different Age Groups (2010-2020)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Coffee Consumption (Thousand Cups/Day)', fontsize=12)

# Add legend with better positioning outside the plot area
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Age Groups', fontsize=10, frameon=False)

# Grid on y-axis only
plt.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5)

# Annotate significant growth in the 26-35 age group data
plt.annotate('Spike in Consumption', xy=(2017, 85), xytext=(2012, 120),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
             fontsize=11, color='darkblue')

# Enhance annotations for better insight
for i in range(len(years)):
    if i == len(years) - 1:  # Only mark the last data points to avoid clutter
        plt.text(years[i], consumption_data[1, i] + 3, f'{consumption_data[1, i]}', color=colors[1], fontsize=10, fontweight='bold')
        plt.text(years[i], consumption_data[0, i] + consumption_data[1, i] + 3, f'{consumption_data[0, i]}', color=colors[0], fontsize=10, fontweight='bold')

# Adjust layout to prevent any overlap
plt.tight_layout()

# Show plot
plt.show()
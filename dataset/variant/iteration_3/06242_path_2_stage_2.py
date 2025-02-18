import matplotlib.pyplot as plt
import numpy as np

# Years of interest
years = np.arange(2010, 2021)

# Coffee consumption data in thousand cups per day for different age groups
age_18_25 = np.array([20, 22, 25, 30, 35, 40, 45, 50, 55, 60, 65])
age_26_35 = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
age_36_50 = np.array([40, 42, 45, 47, 50, 53, 56, 59, 62, 65, 70])
age_51_65 = np.array([15, 18, 20, 22, 25, 28, 30, 32, 35, 38, 40])

# Stack the consumption data
consumption_data = np.vstack([age_18_25, age_26_35, age_36_50, age_51_65])

# Set up the plot
plt.figure(figsize=(14, 9))

# Define colors for the remaining age groups
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

# Create the stacked area plot
plt.stackplot(years, consumption_data, colors=colors, alpha=0.8)

# Set titles and labels
plt.title('Decadal Coffee Consumption Trends\nAcross Different Age Groups (2010-2020)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Coffee Consumption (Thousand Cups/Day)', fontsize=12)

# Show plot
plt.show()
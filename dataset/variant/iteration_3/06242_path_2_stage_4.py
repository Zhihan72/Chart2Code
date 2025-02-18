import matplotlib.pyplot as plt
import numpy as np

# Years
years = np.arange(2010, 2021)

# Coffee consumption for age groups
age_18_25 = np.array([20, 22, 25, 30, 35, 40, 45, 50, 55, 60, 65])
age_26_35 = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
age_36_50 = np.array([40, 42, 45, 47, 50, 53, 56, 59, 62, 65, 70])
age_51_65 = np.array([15, 18, 20, 22, 25, 28, 30, 32, 35, 38, 40])

# Stack the data
consumption_data = np.vstack([age_18_25, age_26_35, age_36_50, age_51_65])

# Plot
plt.figure(figsize=(14, 9))

# Colors for groups
colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3']

# Stacked area plot
plt.stackplot(years, consumption_data, colors=colors, alpha=0.8)

# Titles and labels
plt.title('Coffee Trends by Age (2010-2020)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Consumption (K Cups/Day)', fontsize=12)

# Show plot
plt.show()
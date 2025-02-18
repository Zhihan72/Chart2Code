import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2000, 2021)
country_a_adoption = np.array([2, 3, 4, 7, 10, 12, 15, 19, 22, 25, 30, 35, 41, 48, 55, 63, 70, 78, 86, 93, 100])
country_b_adoption = np.array([1, 1.5, 2.5, 4, 6, 8, 12, 15, 18, 22, 27, 33, 40, 48, 57, 67, 78, 90, 95, 98, 100])
country_c_adoption = np.array([0.5, 1, 1.5, 2.5, 4, 6, 9, 13, 17, 23, 30, 38, 47, 57, 68, 80, 85, 90, 94, 97, 100])

# Plotting setup
plt.figure(figsize=(12, 8))

# Plot data
plt.plot(years, country_a_adoption, label='Region X', color='blue', marker='o', linewidth=2, markersize=6)
plt.plot(years, country_b_adoption, label='Nation Y', color='green', marker='s', linewidth=2, markersize=6)
plt.plot(years, country_c_adoption, label='State Z', color='red', marker='^', linewidth=2, markersize=6)

# Plot details
plt.title("Growth of Clean Energy Usage\nIn Different Areas (2000-2020)", fontsize=16, fontweight='bold', ha='center')
plt.xlabel('Timeline', fontsize=14)
plt.ylabel('Renewable Share (%)', fontsize=14)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 101, 10))
plt.ylim(0, 110)
plt.grid(True, linestyle='--', alpha=0.6)

# Add legends
plt.legend(title='Territories', fontsize=12, loc='lower right')

# Annotations for key points
plt.annotate('Innovation Boost',
             xy=(2015, 63), xytext=(2012, 80),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, color='blue', fontweight='bold')

plt.annotate('Subsidy Increase',
             xy=(2010, 27), xytext=(2007, 45),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, color='green', fontweight='bold')

plt.annotate('Breakthrough Discovery',
             xy=(2015, 68), xytext=(2012, 85),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, color='red', fontweight='bold')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show final plot
plt.show()
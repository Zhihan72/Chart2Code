import matplotlib.pyplot as plt
import numpy as np

# Define years
years = np.arange(2013, 2023)

# Define adoption data for each technology
ai_adoption = np.array([5, 10, 20, 30, 40, 50, 55, 60, 70, 75])
blockchain_adoption = np.array([2, 8, 15, 22, 30, 28, 26, 24, 22, 20])
iot_adoption = np.array([10, 15, 25, 35, 45, 55, 53, 51, 50, 48])
ar_adoption = np.array([3, 7, 10, 15, 18, 20, 22, 20, 18, 17])

# Compute adoption percentages
total_adoption = ai_adoption + blockchain_adoption + iot_adoption + ar_adoption
ai_adoption_percentage = (ai_adoption / total_adoption) * 100
blockchain_adoption_percentage = (blockchain_adoption / total_adoption) * 100
iot_adoption_percentage = (iot_adoption / total_adoption) * 100
ar_adoption_percentage = (ar_adoption / total_adoption) * 100
adoption_data = np.vstack([ai_adoption_percentage, blockchain_adoption_percentage, iot_adoption_percentage, ar_adoption_percentage])

# Plotting the stacked area chart
plt.figure(figsize=(12, 7))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
plt.stackplot(years, adoption_data, labels=['AI', 'BC', 'IoT', 'AR'], colors=colors, alpha=0.8)

# Simplified titles and labels
plt.title('Tech Trends (2013-22)', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Adoption (%)', fontsize=12)

# Adjust x-axis labels
plt.xticks(years, rotation=45)

# Add legend outside plot area
plt.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()
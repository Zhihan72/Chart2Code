import matplotlib.pyplot as plt
import numpy as np

# Data: Countries and their renewable energy adoption percentages
countries = ['Norway', 'Germany', 'China', 'United States', 'India', 'Brazil', 'Spain', 'Australia', 'Japan', 'South Africa']
renewable_percentages = [98, 48, 35, 20, 28, 83, 45, 41, 25, 18]

# Colors for each country using shades of green
colors = plt.cm.Greens(np.linspace(0.4, 0.9, len(countries)))

# Create vertical bar chart
fig, ax1 = plt.subplots(figsize=(14, 8))

# Bar chart
bars = ax1.bar(countries, renewable_percentages, color=colors, edgecolor='black')
ax1.set_ylabel('Percentage of Energy from Renewables (%)', fontsize=12)
ax1.set_ylim(0, 100)
ax1.set_xticks(np.arange(len(countries)))
ax1.set_xticklabels(countries, rotation=45, ha='right', fontsize=12)
ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
ax1.bar_label(bars, fmt='%.0f%%', padding=3, fontsize=11)

# Title
ax1.set_title('Renewable Energy Adoption by Country in 2023', fontsize=16, fontweight='bold', pad=20)

# Adjust layout
plt.tight_layout()

# Display the chart
plt.show()
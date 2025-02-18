import matplotlib.pyplot as plt
import numpy as np

# Data for the pie chart
technologies = ['Solar Panels', 'Fusion Power', 'Geothermal', 'Wind Turbines', 'Hydrogen Fuel Cells', 'Nuclear Fusion']
power_distribution = [25, 20, 15, 10, 10, 20]

# Create a 1x2 grid of subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Main pie chart subplot with a new set of colors
ax1.pie(power_distribution, labels=technologies, autopct='%1.1f%%', startangle=90, 
        colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'], 
        explode=(0.1, 0, 0, 0, 0, 0))

ax1.set_title("Urban Communication Systems Power Sources (Year 2100)",
              fontsize=14, weight='bold', pad=20)

# Data for a secondary subplot comparing two power sources with new colors
tech_comparison = ['Solar Panels', 'Fusion Power']
efficiency = [88, 92]

bars = ax2.bar(tech_comparison, efficiency, color=['#1f77b4', '#ff7f0e'])
ax2.set_title("Efficiency Comparison Between Solar and Fusion Power",
              fontsize=14, weight='bold', pad=20)
ax2.set_ylabel("Efficiency (%)", fontsize=12)
ax2.set_ylim(0, 100)

# Display values on top of the bars
for bar, eff in zip(bars, efficiency):
    ax2.text(bar.get_x() + bar.get_width() / 2, eff + 2, f"{eff}%", ha='center', va='bottom', fontsize=12)

plt.tight_layout()
plt.show()
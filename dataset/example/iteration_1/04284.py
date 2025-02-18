import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# In 2100, futuristic urban communication systems are powered by various advanced technologies. The chart depicts
# the distribution of power sources for these systems in a sample metropolitan area.

# Data for the pie chart
technologies = ['Solar Panels', 'Fusion Power', 'Geothermal', 'Wind Turbines', 'Hydrogen Fuel Cells', 'Nuclear Fusion']
power_distribution = [25, 20, 15, 10, 10, 20]

# Create a 1x2 grid of subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Main pie chart subplot
ax1.pie(power_distribution, labels=technologies, autopct='%1.1f%%', startangle=90, 
        colors=['#FFD700', '#FF8C00', '#228B22', '#00BFFF', '#FF69B4', '#4682B4'], 
        explode=(0.1, 0, 0, 0, 0, 0))

ax1.set_title("Urban Communication Systems Power Sources (Year 2100)",
              fontsize=14, weight='bold', pad=20)

# Data for a secondary subplot comparing two power sources

tech_comparison = ['Solar Panels', 'Fusion Power']
efficiency = [88, 92]  # Efficiency percentages

bars = ax2.bar(tech_comparison, efficiency, color=['#FFD700', '#FF8C00'])
ax2.set_title("Efficiency Comparison Between Solar and Fusion Power",
              fontsize=14, weight='bold', pad=20)
ax2.set_ylabel("Efficiency (%)", fontsize=12)
ax2.set_ylim(0, 100)
ax2.grid(True, axis='y', linestyle='--', alpha=0.5)

# Display values on top of the bars
for bar, eff in zip(bars, efficiency):
    ax2.text(bar.get_x() + bar.get_width() / 2, eff + 2, f"{eff}%", ha='center', va='bottom', fontsize=12)

# Adding detailed annotations for important insights
ax1.annotate('Most used power source',
             xy=(0.8, 0.8), xytext=(1.2, 1.2),
             textcoords='figure fraction', arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, weight='bold')

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the plots
plt.show()
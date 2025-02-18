import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The city of Techville has been promoting electric car adoption aggressively over the past decade. 
# This script will visualize the yearly progress in electric vehicle (EV) purchases and the resulting reduction in CO2 emissions.
# We're focusing on data from 2015 to 2025 to illustrate this trend.

# Data for the number of electric vehicles sold per year
years = np.arange(2015, 2026)
ev_sales = [100, 200, 450, 700, 1100, 1500, 2000, 2700, 3500, 4300, 5200]

# Data for resultant CO2 emissions reduction per year (in tons)
co2_reduction = np.array(ev_sales) * 0.15  # Assuming each vehicle reduces 0.15 tons of CO2 per year

# Create a figure and axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot bar chart for EV sales
bars = ax1.bar(years, ev_sales, color='#4CAF50', edgecolor='black')

# Annotating each bar with the sales number
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 100, f'{yval}', ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

# Add labels and title
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of EVs Sold', fontsize=12)
ax1.set_title('Techville Electric Vehicle Adoption and CO2 Reduction (2015-2025)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45, ha='right')
ax1.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Create a secondary y-axis to plot CO2 reduction
ax2 = ax1.twinx()
ax2.plot(years, co2_reduction, color='blue', linestyle='--', marker='o', linewidth=2, markersize=8)
ax2.set_ylabel('CO2 Reduction (in tons)', fontsize=12, color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

# Annotating the CO2 reduction line plot
for i, reduction in enumerate(co2_reduction):
    ax2.text(years[i], reduction + 10, f'{reduction:.1f}', ha='center', va='bottom', fontsize=10, fontweight='bold', color='blue')

# Adding legend
fig.legend(['EV Sales', 'CO2 Reduction'], loc='upper left', bbox_to_anchor=(0.1, 0.95), fontsize=12)

# Tighter layout to prevent overlap and improve readability
plt.tight_layout()

# Display the chart
plt.show()
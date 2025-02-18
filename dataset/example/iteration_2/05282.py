import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart presents the trend of annual rainfall (in mm) in a fictional area named Rainville over a span of 20 years. 
# The aim is to analyze the patterns and fluctuations in rainfall to understand its impact on local agriculture and water resources.

years = np.arange(2000, 2020)
rainfall = np.array([850, 920, 940, 870, 860, 910, 820, 800, 960, 1000, 
                     1100, 1050, 1140, 1150, 1005, 1100, 1080, 1200, 1250, 1300])

# Create the main figure and axis
fig, ax = plt.subplots(figsize=(12, 6))

# Plotting the line chart for annual rainfall
ax.plot(years, rainfall, label='Annual Rainfall', color='blue', linewidth=2, marker='o')

# Highlighting certain years for annotations
annotations = {
    2003: "Drought Year",
    2010: "Peak Rainfall",
    2018: "Climate Change Noticeable"
}

for year, text in annotations.items():
    ax.annotate(text, xy=(year, rainfall[np.where(years == year)][0] + 30), 
                xytext=(10, -40), textcoords='offset points', 
                arrowprops=dict(arrowstyle='->', color='grey'),
                ha='center', fontsize=10, color='darkred', weight='bold')

# Customizing the plot appearance
ax.set_title("Annual Rainfall Trends in Rainville (2000 - 2019)", fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Annual Rainfall (mm)", fontsize=12)
ax.set_xlim(1999, 2020)
ax.set_ylim(750, 1350)
ax.grid(True, linestyle='--', alpha=0.7)

# Add legend
ax.legend(loc='upper left', frameon=True, fontsize=12)

# Ensure layout fits all elements and text
plt.tight_layout()

# Display the plot
plt.show()
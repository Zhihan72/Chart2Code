import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2010, 2020)

# Hypothetical crop yields (in metric tons) for Corn and Soybeans
corn_yield = np.array([5.2, 5.5, 5.8, 6.0, 5.7, 5.9, 6.3, 6.5, 6.1, 6.8])
soybean_yield = np.array([2.1, 2.4, 2.6, 2.9, 2.5, 2.8, 3.1, 3.3, 3.0, 3.5])

# Create the line chart
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot both Corn and Soybean yield over the years with altered styles
line1 = ax1.plot(years, corn_yield, color='blue', linestyle='-.', marker='^', linewidth=2, markersize=10, label='Corn Yield')
line2 = ax1.plot(years, soybean_yield, color='purple', linestyle='-', marker='d', linewidth=2, markersize=10, label='Soybean Yield')

# Annotate significant points
annotations = {
    2015: ('Drought Year', (0, 40)),
    2018: ('Record High Yield', (0, -40))
}

for year, (text, offset) in annotations.items():
    index = np.where(years == year)[0][0]
    ax1.annotate(
        text, 
        (years[index], corn_yield[index]), 
        xytext=offset, 
        textcoords='offset points', 
        arrowprops=dict(arrowstyle='->', color='darkblue'),
        ha='center', fontsize=10, color='darkgreen'
    )

# Titles and labels
ax1.set_title("Decade Long Crop Yield Analysis: Corn vs Soybean\n(2010-2019)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=14)
ax1.set_ylabel("Yield (Metric Tons)", fontsize=14, color='black')

# Changed legend and location
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='lower right', fontsize=12)

# Altered grid style
ax1.grid(True, linestyle='-.', alpha=0.5)

# Automatically adjust the layout to prevent overlaps
plt.tight_layout()

# Display the plot
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Average crop yields (in tons per hectare)
average_yields = np.array([2.5, 2.7, 2.9, 3.0, 3.1, 3.3, 3.5, 3.6, 3.8, 3.9, 4.0])

# Create the line chart without error bars
plt.figure(figsize=(12, 8))
plt.plot(
    years, 
    average_yields, 
    '-o', 
    color='forestgreen', 
    markerfacecolor='gold', 
    markersize=8,
    alpha=0.8
)

# Add titles and labels
plt.title('Decade of Organic Farming:\nYield Trends in Greenfield Valley (2010-2020)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Crop Yield (tons/ha)', fontsize=12)

# Add grid and legend
plt.grid(linestyle='--', alpha=0.6)
plt.legend(['Average Yield'], loc='upper left', fontsize=10)

# Annotate significant trends
plt.annotate(
    'Yield Improvement Initiatives', 
    xy=(2015, 3.1), 
    xytext=(2012, 3.5), 
    arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8), 
    fontsize=11, 
    color='blue'
)
plt.annotate(
    'Sustainable Practice Adoption', 
    xy=(2018, 3.8), 
    xytext=(2016, 4.1), 
    arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8), 
    fontsize=11, 
    color='red'
)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()
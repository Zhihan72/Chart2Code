import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Average crop yields and error margins for Groups A and B
average_yields_A = np.array([2.5, 2.7, 2.9, 3.0, 3.1, 3.3, 3.5, 3.6, 3.8, 3.9, 4.0])
average_yields_B = np.array([2.3, 2.5, 2.6, 2.8, 2.9, 3.0, 3.2, 3.3, 3.5, 3.7, 3.9])
error_margins_A = np.array([0.2, 0.25, 0.3, 0.3, 0.35, 0.4, 0.35, 0.3, 0.25, 0.2, 0.2])
error_margins_B = np.array([0.15, 0.2, 0.25, 0.25, 0.3, 0.35, 0.3, 0.25, 0.2, 0.15, 0.15])

# Create the horizontal bar chart with error bars
plt.figure(figsize=(12, 8))
plt.barh(
    years - 0.2, 
    average_yields_A, 
    xerr=error_margins_A, 
    height=0.4, 
    capsize=5, 
    color='forestgreen', 
    ecolor='orange', 
    alpha=0.8,
    label='Group A'
)
plt.barh(
    years + 0.2, 
    average_yields_B, 
    xerr=error_margins_B, 
    height=0.4, 
    capsize=5, 
    color='royalblue', 
    ecolor='red', 
    alpha=0.8,
    label='Group B'
)

# Add titles and labels
plt.title('Decade of Organic Farming:\nYield Trends in Greenfield Valley (2010-2020)', fontsize=16, fontweight='bold', pad=20)
plt.ylabel('Year', fontsize=12)
plt.xlabel('Average Crop Yield (tons/ha)', fontsize=12)

# Add grid and legend
plt.grid(linestyle='--', alpha=0.6, axis='x')
plt.legend(loc='upper left', fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()
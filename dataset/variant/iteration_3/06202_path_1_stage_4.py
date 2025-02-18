import matplotlib.pyplot as plt
import numpy as np

# Data Construction
years = np.arange(2000, 2021)

# Removed the Greenland temperature data group
# Which means there should be no meaningful data to plot

# Creating the Plot
plt.figure(figsize=(14, 8))

# There's no line plot to create after removing data

# Highlight
plt.axhline(y=-14, color='#1f77b4', linestyle='--', alpha=0.7)
plt.axvspan(2015, 2020, color='#1f77b4', alpha=0.1)

# Remove stylistic elements
plt.axis('off')

# Display the Plot
plt.show()
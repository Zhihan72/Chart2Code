import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2012, 2023)

# Data for the three glaciers in gigatons of ice lost per year
glacier_a = np.array([2.1, 2.3, 2.4, 2.6, 2.8, 3.0, 3.2, 3.3, 3.6, 3.8, 4.0])
glacier_b = np.array([1.8, 1.9, 2.0, 2.1, 2.3, 2.5, 2.7, 2.8, 3.0, 3.2, 3.4])
glacier_c = np.array([1.5, 1.6, 1.7, 1.8, 2.0, 2.2, 2.4, 2.5, 2.7, 2.9, 3.1])

# Calculate the cumulative ice loss for each glacier
cumulative_a = np.cumsum(glacier_a)
cumulative_b = np.cumsum(glacier_b)
cumulative_c = np.cumsum(glacier_c)

# Set up the plot
fig, axs = plt.subplots(2, 1, figsize=(12, 10))

# Plot the annual ice loss
axs[0].plot(years, glacier_a, marker='o', label='Glacier A', color='#1f77b4')
axs[0].plot(years, glacier_b, marker='s', label='Glacier B', color='#1f77b4')
axs[0].plot(years, glacier_c, marker='^', label='Glacier C', color='#1f77b4')
axs[0].set_title("Annual Ice Loss in the Arctic Glaciers\n(2012-2022)", fontsize=16, fontweight='bold')
axs[0].set_xlabel("Year", fontsize=12)
axs[0].set_ylabel("Ice Loss (Gigatons/year)", fontsize=12)
axs[0].legend(title='Glaciers', fontsize=10)
axs[0].grid(True, linestyle='--', alpha=0.5)
axs[0].tick_params(axis='x', rotation=45)

# Plot the cumulative ice loss
axs[1].plot(years, cumulative_a, marker='o', label='Glacier A', color='#1f77b4')
axs[1].plot(years, cumulative_b, marker='s', label='Glacier B', color='#1f77b4')
axs[1].plot(years, cumulative_c, marker='^', label='Glacier C', color='#1f77b4')
axs[1].set_title("Cumulative Ice Mass Loss in the Arctic Glaciers\n(2012-2022)", fontsize=16, fontweight='bold')
axs[1].set_xlabel("Year", fontsize=12)
axs[1].set_ylabel("Cumulative Ice Loss (Gigatons)", fontsize=12)
axs[1].legend(title='Glaciers', fontsize=10)
axs[1].grid(True, linestyle='--', alpha=0.5)
axs[1].tick_params(axis='x', rotation=45)

# Automatically adjust layout
plt.tight_layout()

# Display the plots
plt.show()
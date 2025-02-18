import matplotlib.pyplot as plt
import numpy as np

# Backstory: "Global Ocean Currents Over a Century"
# This chart examines the changes in ocean currents across different oceans over a century (1900-2000).

# Create artificial data representing the strength of ocean currents (in Sv, Sverdrup) across different oceans per decade
decades = np.arange(1900, 2001, 10)

# Data for ocean currents in Sverdrup (Sv is a unit of volume flow rate)
atlantic_data = [16, 16.5, 17, 17.2, 17.5, 17.6, 17.8, 18, 18.1, 18.3, 18.5]
pacific_data = [15, 15.2, 15.5, 15.6, 15.8, 16, 16.2, 16.4, 16.6, 16.8, 17]
indian_data = [10, 10.1, 10.3, 10.5, 10.7, 10.8, 11, 11.2, 11.4, 11.5, 11.7]
southern_data = [12, 12.3, 12.5, 12.6, 12.8, 13, 13.2, 13.3, 13.5, 13.6, 13.8]
arctic_data = [0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5]

# Create the figure and subplots
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot each ocean's current strength over time
ax1.plot(decades, atlantic_data, label='Atlantic Ocean', marker='o', linestyle='-', linewidth=2, color='#1f77b4')
ax1.plot(decades, pacific_data, label='Pacific Ocean', marker='s', linestyle='--', linewidth=2, color='#ff7f0e')
ax1.plot(decades, indian_data, label='Indian Ocean', marker='^', linestyle='-.', linewidth=2, color='#2ca02c')
ax1.plot(decades, southern_data, label='Southern Ocean', marker='D', linestyle=':', linewidth=2, color='#d62728')
ax1.plot(decades, arctic_data, label='Arctic Ocean', marker='v', linestyle='-', linewidth=2, color='#9467bd')

# Set the title and labels with detailed formatting options
ax1.set_title("Century-long Trends in Ocean Currents (1900-2000)\nAnalyzing Strength Across Various Oceans", fontsize=18, fontweight='bold')
ax1.set_xlabel('Decades', fontsize=14, fontweight='bold')
ax1.set_ylabel('Current Strength (Sverdrup, Sv)', fontsize=14, fontweight='bold')
ax1.legend(loc='upper left', title='Oceans', fontsize=12, title_fontsize='13')

# Enhance grid visibility for better readability
ax1.grid(True, linestyle='--', alpha=0.7)

# Annotate a specific data point of interest
ax1.annotate('Significant Increase\nin Arctic Ocean', xy=(2000, 1.5), xytext=(1940, 3),
             arrowprops=dict(facecolor='blue', shrink=0.05, width=1, headwidth=5),
             fontsize=12, color='darkblue')

# Ensure tight layout to avoid overlap of elements
plt.tight_layout()

# Display the plot
plt.show()
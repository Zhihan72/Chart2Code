import matplotlib.pyplot as plt
import numpy as np

# Define years for the timeline
years = np.arange(2010, 2021)

# Stock prices over the years for each company
techcorp_stocks = [120, 135, 150, 180, 210, 250, 300, 350, 400, 450, 500]
innovateinc_stocks = [80, 85, 100, 140, 180, 220, 280, 330, 420, 520, 650]
futuresystems_stocks = [60, 70, 90, 110, 140, 170, 210, 260, 320, 400, 490]

# Create the plot
plt.figure(figsize=(12, 8))

# Plot each company's stock data
plt.plot(years, techcorp_stocks, color='blue', marker='s', linewidth=2, linestyle='-')
plt.plot(years, innovateinc_stocks, color='green', marker='d', linewidth=2, linestyle='--')
plt.plot(years, futuresystems_stocks, color='red', marker='o', linewidth=2, linestyle='-.')

# Remove annotations
# Remove title and axis labels

# Set y-axis range and add gridlines
plt.ylim(0, 700)
plt.grid(True, linestyle='--', alpha=0.6)

# Remove legend

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()
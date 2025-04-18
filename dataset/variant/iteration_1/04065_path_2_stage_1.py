import matplotlib.pyplot as plt
import numpy as np

# Weeks of observation
weeks = np.arange(1, 11)

# Data: Sales (in units), Temperature (in °C), and Customer Satisfaction (rating 0 to 10)
sales = np.array([60, 75, 90, 120, 130, 160, 170, 150, 135, 125])
temperature = np.array([20, 22, 25, 27, 30, 32, 33, 31, 28, 26])
satisfaction = np.array([6, 7, 7.5, 8, 9, 9, 9.5, 8.5, 8, 7.5])

# Create figure and horizontal bar chart
plt.figure(figsize=(14, 9))

# Horizontal bar chart for Sales vs Temperature colored by Satisfaction
bar_chart = plt.barh(temperature, sales, color=plt.cm.viridis(satisfaction / max(satisfaction)), edgecolor='black')

# Titles and labels
plt.title("Impact of Temperature on Ice Cream Sales and Customer Satisfaction\nin Fictional Town's Summer Weeks", fontsize=18, fontweight='bold', pad=20)
plt.xlabel("Ice Cream Sales (Units)", fontsize=14)
plt.ylabel("Temperature (°C)", fontsize=14)

# Annotate bars with week numbers
for i, (sales_val, temp, week) in enumerate(zip(sales, temperature, weeks)):
    plt.text(sales_val + 2, temp, f"Week {week}", fontsize=10, fontweight='bold', va='center')

# Add grid lines
plt.grid(True, linestyle='--', alpha=0.6, axis='x')

# Create a mappable for colorbar based on satisfaction
sm = plt.cm.ScalarMappable(cmap='viridis', norm=plt.Normalize(0, 10))
sm.set_array([])
cbar = plt.colorbar(sm, ax=plt.gca())
cbar.set_label('Customer Satisfaction (0 to 10)', fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Backstory: Visualizing Ice Cream Sales vs. Temperature with Customer Satisfaction
# In a fictional town during each week of summer, ice cream sales, temperatures, and customer satisfaction
# were tracked to understand the impact of weather on sales and satisfaction.

# Weeks of observation
weeks = np.arange(1, 11)

# Data: Sales (in units), Temperature (in °C), and Customer Satisfaction (rating 0 to 10)
sales = np.array([60, 75, 90, 120, 130, 160, 170, 150, 135, 125])
temperature = np.array([20, 22, 25, 27, 30, 32, 33, 31, 28, 26])
satisfaction = np.array([6, 7, 7.5, 8, 9, 9, 9.5, 8.5, 8, 7.5])

# Create figure and scatter plot
plt.figure(figsize=(14, 9))

# Scatter plot for Sales vs Temperature colored by Satisfaction
scatter = plt.scatter(temperature, sales, s=satisfaction*100, c=satisfaction, cmap='viridis', alpha=0.75, edgecolors='black', linewidth=1)

# Titles and labels
plt.title("Impact of Temperature on Ice Cream Sales and Customer Satisfaction\nin Fictional Town's Summer Weeks", fontsize=18, fontweight='bold', pad=20)
plt.xlabel("Temperature (°C)", fontsize=14)
plt.ylabel("Ice Cream Sales (Units)", fontsize=14)

# Annotate points with week numbers
for i, week in enumerate(weeks):
    plt.annotate(f"Week {week}", (temperature[i] + 0.5, sales[i]), fontsize=10, fontweight='bold', bbox=dict(facecolor='white',alpha=0.7, edgecolor='gray'))

# Add grid lines
plt.grid(True, linestyle='--', alpha=0.6)

# Add colorbar to indicate customer satisfaction rating
cbar = plt.colorbar(scatter)
cbar.set_label('Customer Satisfaction (0 to 10)', fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()
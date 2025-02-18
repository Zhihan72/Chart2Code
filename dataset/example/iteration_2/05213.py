import matplotlib.pyplot as plt
import numpy as np

# Define time periods (years)
years = np.arange(2020, 2031)

# Artificial data representing the growth in the adoption of electric vehicles (EVs)
ev_sales = [1, 3, 5, 9, 14, 20, 27, 35, 44, 54, 65] # in millions
charging_stations = [50, 70, 100, 150, 220, 300, 400, 520, 660, 820, 1000] # in thousands

# Construct backstory
# The chart shows the trend of electric vehicle adoption and the corresponding growth of charging infrastructure over the decade 2020-2030.
# The data highlights the increasing shift towards sustainable transportation solutions.

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot EV sales data
ax1.plot(years, ev_sales, color='blue', marker='o', linewidth=2, label='EV Sales (millions)')

# Set title and labels for the first plot
ax1.set_title("Adoption of Electric Vehicles\nand Charging Infrastructure Growth (2020-2030)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=14)
ax1.set_ylabel("EV Sales (millions)", fontsize=14, color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Add secondary y-axis for charging station count data
ax2 = ax1.twinx()
ax2.plot(years, charging_stations, color='green', marker='s', linestyle='--', linewidth=2, label='Charging Stations (thousands)')
ax2.set_ylabel("Charging Stations (thousands)", fontsize=14, color='green')
ax2.tick_params(axis='y', labelcolor='green')
    
# Add grid and legend
ax1.grid(True, linestyle='--', alpha=0.7)
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left', fontsize=12)

# Annotate significant data points
ax1.annotate(f'{ev_sales[0]}M', xy=(2020, ev_sales[0]), xytext=(2020, ev_sales[0] + 2),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold', color='darkblue')

ax1.annotate(f'{ev_sales[-1]}M', xy=(2030, ev_sales[-1]), xytext=(2029.5, ev_sales[-1] - 8),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold', color='darkred')

ax2.annotate(f'{charging_stations[0]}K', xy=(2020, charging_stations[0]), xytext=(2020.5, charging_stations[0] + 50),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold', color='darkgreen')
             
ax2.annotate(f'{charging_stations[-1]}K', xy=(2030, charging_stations[-1]), xytext=(2029, charging_stations[-1] - 200),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold', color='darkgreen')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()
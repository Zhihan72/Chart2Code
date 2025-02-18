import matplotlib.pyplot as plt
import numpy as np

# Define time periods (years)
years = np.arange(2020, 2031)

# Artificially modified data representing the growth in the adoption of electric vehicles (EVs)
ev_sales = [1, 3, 6, 8, 15, 19, 28, 34, 45, 55, 63]  # Altered in millions
charging_stations = [45, 75, 95, 155, 210, 310, 390, 530, 650, 810, 995]  # Altered in thousands

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot EV sales data
ax1.plot(years, ev_sales, color='blue', marker='o', linewidth=2, label='EV Sales Quantity')

# Set title and labels
ax1.set_title("EV Growth and Charging Network Expansion (2020-2030)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Timeline", fontsize=14)
ax1.set_ylabel("EV Units Sold (millions)", fontsize=14, color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Add secondary y-axis for charging station count data
ax2 = ax1.twinx()
ax2.plot(years, charging_stations, color='green', marker='s', linestyle='--', linewidth=2, label='Station Count')
ax2.set_ylabel("Stations (thousands)", fontsize=14, color='green')
ax2.tick_params(axis='y', labelcolor='green')

# Add grid and legend
ax1.grid(True, linestyle='--', alpha=0.7)
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left', fontsize=12)

# Annotate significant data points
ax1.annotate(f'Init {ev_sales[0]}M', xy=(2020, ev_sales[0]), xytext=(2020, ev_sales[0] + 2),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold', color='darkblue')

ax1.annotate(f'End {ev_sales[-1]}M', xy=(2030, ev_sales[-1]), xytext=(2029.5, ev_sales[-1] - 8),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold', color='darkred')

ax2.annotate(f'Start {charging_stations[0]}K', xy=(2020, charging_stations[0]), xytext=(2020.5, charging_stations[0] + 50),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold', color='darkgreen')

ax2.annotate(f'Peak {charging_stations[-1]}K', xy=(2030, charging_stations[-1]), xytext=(2029, charging_stations[-1] - 200),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold', color='darkgreen')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()
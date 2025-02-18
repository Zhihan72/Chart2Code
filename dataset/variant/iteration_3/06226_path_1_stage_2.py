import numpy as np
import matplotlib.pyplot as plt

# Define the years
years = np.arange(2020, 2036)

# Data for different modes of transportation (in million passenger-kilometers)
public_transport = np.array([85, 87, 90, 95, 100, 105, 110, 120, 130, 140, 150, 160, 170, 180, 195, 210])
bicycles = np.array([10, 11, 12, 15, 18, 22, 25, 30, 35, 40, 45, 50, 60, 70, 85, 100])
electric_vehicles = np.array([5, 8, 12, 18, 30, 40, 55, 75, 95, 120, 150, 180, 210, 240, 270, 300])
pedestrians = np.array([15, 15, 16, 18, 20, 23, 26, 30, 35, 40, 45, 50, 55, 60, 65, 70])
traditional_cars = np.array([70, 68, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0])

# Stacked area plot
plt.figure(figsize=(14, 8))

# Plotting the area chart
plt.stackplot(years, public_transport, bicycles, electric_vehicles, pedestrians, traditional_cars,
              labels=['Bikes', 'Foot Traffic', 'Legacy Vehicles', 'Public Buses', 'EVs'],
              colors=['#f5a742', '#42f548', '#4287f5', '#f5426f', '#b742f5'], alpha=0.85)

# Title and labels
plt.title("Charting Urban Commute Past\n(2020-2035)", fontsize=18, fontweight='normal')
plt.xlabel("Calendar Year", fontsize=13)
plt.ylabel("Millions of Passengers per Kilometer", fontsize=13)

# Legend
plt.legend(loc='lower left', fontsize=10, title='Transport Styles', title_fontsize='13')

# Annotations to highlight key transitions
plt.annotate('EV Usage Spike', xy=(2030, 400), xytext=(2025, 420),
             arrowprops=dict(facecolor='grey', arrowstyle='-|>'), fontsize=10)

plt.annotate('Traditional Cars\nReduction', xy=(2029, 240), xytext=(2023, 300),
             arrowprops=dict(facecolor='darkgrey', arrowstyle='->'), fontsize=10)

# Customize x-axis labels
plt.xticks(years, rotation=30)

# Grid for better readability
plt.grid(axis='x', linestyle='-.', color='darkgrey', alpha=0.6)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
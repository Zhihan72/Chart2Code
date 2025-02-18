import matplotlib.pyplot as plt
import numpy as np

# Data for 12 months
months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

# Energy consumption data (in kWh)
heating = np.array([350, 310, 280, 220, 180, 140, 130, 140, 200, 270, 310, 340])
cooling = np.array([50, 60, 100, 200, 300, 370, 400, 380, 290, 170, 80, 60])
lighting = np.array([100, 90, 80, 90, 100, 110, 120, 110, 100, 90, 80, 100])
appliances = np.array([120, 110, 105, 115, 120, 125, 130, 128, 122, 115, 108, 112])
ventilation = np.array([30, 35, 40, 50, 60, 70, 80, 75, 65, 55, 45, 40])  # New data series

# Monthly savings
overall_consumption = heating + cooling + lighting + appliances + ventilation
monthly_savings = 0.1 * overall_consumption

# Plotting
plt.figure(figsize=(14, 8))
plt.plot(months, heating, marker='o', linestyle='-', color='r', linewidth=2)
plt.plot(months, cooling, marker='s', linestyle='--', color='b', linewidth=2)
plt.plot(months, lighting, marker='^', linestyle='-.', color='g', linewidth=2)
plt.plot(months, appliances, marker='d', linestyle=':', color='m', linewidth=2)
plt.plot(months, ventilation, marker='x', linestyle='-', color='y', linewidth=2)  # New plot
plt.plot(months, monthly_savings, marker='*', linestyle='-', color='c', linewidth=2)

# Title and labels
plt.title('Monthly Energy Consumption and Savings in a Smart Home', fontsize=16, fontweight='bold', pad=15)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Energy (kWh)', fontsize=12)

# Show the plot
plt.show()
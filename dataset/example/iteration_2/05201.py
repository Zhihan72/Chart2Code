import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# We want to visualize the trends in the temperature (daily high and low) and the amount of rainfall over a year in a fictional city named Arcadia. The chart will have two subplots: one for daily high and low temperatures and another for monthly rainfall.

# Generate data for temperatures and rainfall
days = np.arange(1, 366)
months = np.arange(1, 13)

# Temperatures (in degrees Celsius)
high_temps = np.concatenate([
    np.linspace(0, 20, 90),   # Jan-Mar
    np.linspace(20, 25, 61),  # Apr-May
    np.linspace(25, 30, 92),  # Jun-Aug
    np.linspace(30, 20, 61),  # Sep-Oct
    np.linspace(20, 10, 61)   # Nov-Dec
])

low_temps = np.concatenate([
    np.linspace(-5, 5, 90),   # Jan-Mar
    np.linspace(5, 10, 61),   # Apr-May
    np.linspace(10, 15, 92),  # Jun-Aug
    np.linspace(15, 5, 61),   # Sep-Oct
    np.linspace(5, -2, 61)    # Nov-Dec
])

# Monthly rainfall (in mm)
rainfall = np.array([50, 40, 55, 70, 100, 150, 200, 180, 120, 90, 60, 55])

# Create subplots
fig, ax = plt.subplots(2, 1, figsize=(12, 12), dpi=100)

# Plot high and low temperatures
ax[0].plot(days, high_temps, label='High Temp', color='red')
ax[0].plot(days, low_temps, label='Low Temp', color='blue')
ax[0].fill_between(days, low_temps, high_temps, facecolor='lightgrey', alpha=0.3)

# Customize the temperature plot
ax[0].set_title('Arcadia Temperature Trends in 2023', fontsize=16, fontweight='bold')
ax[0].set_xlabel('Day of the Year', fontsize=14)
ax[0].set_ylabel('Temperature (°C)', fontsize=14)
ax[0].legend(loc='upper left')

# Plot rainfall
ax[1].bar(months, rainfall, color='skyblue', edgecolor='black')

# Customize the rainfall plot
ax[1].set_title('Arcadia Monthly Rainfall in 2023', fontsize=16, fontweight='bold')
ax[1].set_xlabel('Month', fontsize=14)
ax[1].set_ylabel('Rainfall (mm)', fontsize=14)
ax[1].set_xticks(months)
ax[1].set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Improve the layout
plt.tight_layout()

# Display the chart
plt.show()
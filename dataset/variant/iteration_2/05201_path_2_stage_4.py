import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 366)
months = np.arange(1, 13)

high_temps = np.concatenate([
    np.linspace(0, 20, 90),
    np.linspace(20, 25, 61),
    np.linspace(25, 30, 92),
    np.linspace(30, 20, 61),
    np.linspace(20, 10, 61)
])

low_temps = np.concatenate([
    np.linspace(-5, 5, 90),
    np.linspace(5, 10, 61),
    np.linspace(10, 15, 92),
    np.linspace(15, 5, 61),
    np.linspace(5, -2, 61)
])

# Calculating average temperatures
average_temps = (high_temps + low_temps) / 2

# Adding a fixed pattern for humidity for each month (in percentage)
humidity_levels = np.array([80, 75, 70, 65, 60, 55, 60, 65, 70, 75, 80, 85])

rainfall = np.array([50, 40, 55, 70, 100, 150, 200, 180, 120, 90, 60, 55])

fig, ax = plt.subplots(1, 2, figsize=(16, 6), dpi=100)

# Plot high, low, and average temperatures
ax[0].plot(days, high_temps, color='darkorange')
ax[0].plot(days, low_temps, color='navy')
ax[0].plot(days, average_temps, color='green', linestyle='--')  # Adding average temperatures
ax[0].fill_between(days, low_temps, high_temps, facecolor='lightcoral', alpha=0.3)

ax[0].set_title('Arcadia Temperature Trends in 2023', fontsize=16, fontweight='bold')
ax[0].set_xlabel('Day of the Year', fontsize=14)
ax[0].set_ylabel('Temperature (°C)', fontsize=14)
ax[0].legend(['High Temps', 'Low Temps', 'Avg Temps'])

# Plot rainfall and humidity levels
ax[1].bar(months, rainfall, color='mediumpurple', label='Rainfall (mm)')
ax[1].plot(months, humidity_levels, color='teal', marker='o', label='Humidity (%)')  # Adding humidity levels

ax[1].set_title('Arcadia Monthly Rainfall and Humidity in 2023', fontsize=16, fontweight='bold')
ax[1].set_xlabel('Month', fontsize=14)
ax[1].set_ylabel('Rainfall (mm) / Humidity (%)', fontsize=14)
ax[1].set_xticks(months)
ax[1].set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax[1].legend()

plt.show()
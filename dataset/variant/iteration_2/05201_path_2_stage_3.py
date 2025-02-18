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

rainfall = np.array([50, 40, 55, 70, 100, 150, 200, 180, 120, 90, 60, 55])

fig, ax = plt.subplots(1, 2, figsize=(16, 6), dpi=100)

ax[0].plot(days, high_temps, color='darkorange')  # New color for high temperature
ax[0].plot(days, low_temps, color='navy')         # New color for low temperature
ax[0].fill_between(days, low_temps, high_temps, facecolor='lightcoral', alpha=0.3)  # New color for fill between

ax[0].set_title('Arcadia Temperature Trends in 2023', fontsize=16, fontweight='bold')
ax[0].set_xlabel('Day of the Year', fontsize=14)
ax[0].set_ylabel('Temperature (°C)', fontsize=14)

ax[1].bar(months, rainfall, color='mediumpurple')  # New color for rainfall bars

ax[1].set_title('Arcadia Monthly Rainfall in 2023', fontsize=16, fontweight='bold')
ax[1].set_xlabel('Month', fontsize=14)
ax[1].set_ylabel('Rainfall (mm)', fontsize=14)
ax[1].set_xticks(months)
ax[1].set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

plt.show()
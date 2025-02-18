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

fig, ax = plt.subplots(2, 1, figsize=(12, 12), dpi=100)

ax[0].plot(days, high_temps, label='Max Temp', color='blue')  # Shuffled: from 'red' to 'blue'
ax[0].plot(days, low_temps, label='Min Temp', color='red')    # Shuffled: from 'blue' to 'red'
ax[0].fill_between(days, low_temps, high_temps, facecolor='lightgrey', alpha=0.3)

ax[0].set_title('2023 Temp Patterns in A. City', fontsize=16, fontweight='bold')
ax[0].set_xlabel('Year Day', fontsize=14)
ax[0].set_ylabel('Temp (Degrees)', fontsize=14)
ax[0].legend(loc='upper left')

ax[1].bar(months, rainfall, color='limegreen', edgecolor='black')  # Shuffled: from 'skyblue' to 'limegreen'

ax[1].set_title('2023 Monthly Waterfall in A. City', fontsize=16, fontweight='bold')
ax[1].set_xlabel('Month of Year', fontsize=14)
ax[1].set_ylabel('Water Level (mm)', fontsize=14)
ax[1].set_xticks(months)
ax[1].set_xticklabels(['Jnr', 'Fbr', 'Mrh', 'Apl', 'My', 'Jn', 'Jl', 'Ag', 'Spt', 'Oct', 'Nmv', 'Dcb'])

plt.tight_layout()
plt.show()
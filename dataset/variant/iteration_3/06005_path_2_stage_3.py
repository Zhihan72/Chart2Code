import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
year_2022_temps = [30, 32, 31, 29, 28, 29, 30]
year_2023_temps = [32, 33, 34, 32, 31, 30, 33]
year_2024_temps = [35, 36, 35, 34, 33, 32, 31]

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(days, year_2022_temps, marker='^', linestyle='-', color='blue', label='2022')
ax.plot(days, year_2023_temps, marker='x', linestyle=':', color='purple', label='2023')
ax.plot(days, year_2024_temps, marker='h', linestyle='--', color='orange', label='2024')

ax.set_title("Weekly Temperature Variation\n2022-2024", fontsize=18, fontweight='light', pad=15)
ax.set_xlabel('Days', fontsize=12)
ax.set_ylabel('Temperature (°C)', fontsize=12)

for i, temp in enumerate(year_2022_temps):
    ax.annotate(f'{temp}', xy=(days[i], temp), xytext=(-10, 10), textcoords='offset points', fontsize=8, color='darkblue')

for i, temp in enumerate(year_2023_temps):
    ax.annotate(f'{temp}', xy=(days[i], temp), xytext=(-10, -15), textcoords='offset points', fontsize=8, color='darkgreen')

for i, temp in enumerate(year_2024_temps):
    ax.annotate(f'{temp}', xy=(days[i], temp), xytext=(-10, -25), textcoords='offset points', fontsize=8, color='darkred')

ax.legend(loc='lower left', fontsize=10, frameon=True, facecolor='lightgrey')
ax.grid(True, linestyle='-', which='both', color='black', alpha=0.3)

plt.tight_layout()
plt.show()
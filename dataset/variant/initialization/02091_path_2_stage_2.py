import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_capacity = np.array([50, 60, 75, 95, 110, 130, 150, 180, 210, 240, 280])
wind_capacity = np.array([70, 80, 90, 110, 130, 150, 180, 220, 260, 300, 350])
hydro_capacity = np.array([30, 35, 40, 48, 55, 60, 75, 80, 95, 100, 120])

total_capacity = solar_capacity + wind_capacity + hydro_capacity
solar_percentage = (solar_capacity / total_capacity) * 100
wind_percentage = (wind_capacity / total_capacity) * 100
hydro_percentage = (hydro_capacity / total_capacity) * 100

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

ax1.plot(years, solar_capacity, marker='o', linestyle='-', color='orange', label='Sun Power', linewidth=2)
ax1.plot(years, wind_capacity, marker='s', linestyle='--', color='blue', label='Breeze Energy', linewidth=2)
ax1.plot(years, hydro_capacity, marker='^', linestyle=':', color='green', label='Water Energy', linewidth=2)

for i, (x, y) in enumerate(zip(years, solar_capacity)):
    ax1.annotate(f'{y} MW', (x, y), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=8, color='orange')
for i, (x, y) in enumerate(zip(years, wind_capacity)):
    ax1.annotate(f'{y} MW', (x, y), textcoords="offset points", xytext=(10,-15), ha='center', fontsize=8, color='blue')
for i, (x, y) in enumerate(zip(years, hydro_capacity)):
    ax1.annotate(f'{y} MW', (x, y), textcoords="offset points", xytext=(10,10), ha='center', fontsize=8, color='green')

ax1.set_title('Green Power Surge in EcoVille\n(2010-2020)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Calendar Year', fontsize=10)
ax1.set_ylabel('Power Capacity (MW)', fontsize=10)
ax1.legend(loc='upper left')
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.axvline(x=2015, color='gray', linestyle=':', linewidth=1)
ax1.text(2015, max(max(solar_capacity), max(wind_capacity), max(hydro_capacity)) + 20, 'Climate Accord', ha='center', color='gray')

ax2.stackplot(years, solar_percentage, wind_percentage, hydro_percentage, labels=['Sun %', 'Breeze %', 'Water %'], colors=['orange', 'blue', 'green'], alpha=0.6)
ax2.set_title('Renewables Share Growth\n(2010-2020)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Calendar Year', fontsize=10)
ax2.set_ylabel('Total Capacity %', fontsize=10)
ax2.legend(loc='upper left')
ax2.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
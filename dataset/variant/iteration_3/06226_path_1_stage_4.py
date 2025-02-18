import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2020, 2036)

public_transport = np.array([85, 87, 90, 95, 100, 105, 110, 120, 130, 140, 150, 160, 170, 180, 195, 210])
bicycles = np.array([10, 11, 12, 15, 18, 22, 25, 30, 35, 40, 45, 50, 60, 70, 85, 100])
electric_vehicles = np.array([5, 8, 12, 18, 30, 40, 55, 75, 95, 120, 150, 180, 210, 240, 270, 300])
pedestrians = np.array([15, 15, 16, 18, 20, 23, 26, 30, 35, 40, 45, 50, 55, 60, 65, 70])

plt.figure(figsize=(14, 8))

plt.stackplot(years, public_transport, bicycles, electric_vehicles, pedestrians,
              labels=['Bikes', 'Foot Traffic', 'Legacy Vehicles', 'Public Buses'],
              colors=['#42f548', '#f5426f', '#f5a742', '#4287f5'], alpha=0.85)

plt.title("Charting Urban Commute Past\n(2020-2035)", fontsize=18, fontweight='normal')
plt.xlabel("Calendar Year", fontsize=13)
plt.ylabel("Millions of Passengers per Kilometer", fontsize=13)

plt.legend(loc='lower left', fontsize=10, title='Transport Styles', title_fontsize='13')

plt.annotate('EV Usage Spike', xy=(2030, 350), xytext=(2025, 370),
             arrowprops=dict(facecolor='grey', arrowstyle='-|>'), fontsize=10)

plt.xticks(years, rotation=30)

plt.grid(axis='x', linestyle='-.', color='darkgrey', alpha=0.6)

plt.tight_layout()

plt.show()
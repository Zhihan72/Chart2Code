import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2041)

batteries = np.array([50, 75, 110, 150, 180, 210, 260, 300, 350, 400, 450, 520, 580, 650, 720, 800, 870, 950, 1050, 1150, 1250])
hydropumped = np.array([20, 22, 24, 26, 30, 35, 40, 45, 50, 55, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160])
thermal = np.array([10, 15, 20, 28, 35, 45, 60, 75, 90, 105, 120, 135, 150, 170, 190, 210, 230, 250, 270, 290, 310])
flywheels = np.array([5, 7, 10, 13, 18, 25, 35, 48, 60, 75, 90, 110, 130, 150, 175, 200, 225, 250, 280, 310, 340])

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, batteries, hydropumped, thermal, flywheels,
             labels=['Batteries', 'Hydro-Pump', 'Thermal', 'Flywheels'],
             colors=['#FF5733', '#3498DB', '#9B59B6', '#16A085'], alpha=0.7)

ax.set_title('Renewable Energy Storage in GreenValley (2020-2040)', fontsize=16, fontweight='normal', pad=15)
ax.set_xlabel('Year', fontsize=12, fontstyle='italic')
ax.set_ylabel('Capacity (MWh)', fontsize=12, fontstyle='italic')

ax.legend(loc='upper right', title='Techs', fontsize=10)

ax.grid(False)

plt.tight_layout()

plt.show()
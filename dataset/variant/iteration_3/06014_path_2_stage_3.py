import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2041)

batteries = np.array([110, 300, 210, 950, 260, 150, 450, 75, 720, 650, 580, 50, 180, 400, 350, 1250, 1050, 800, 870, 1150, 520])
hydropumped = np.array([40, 24, 120, 50, 130, 30, 140, 90, 160, 20, 45, 110, 100, 60, 55, 26, 35, 22, 150, 80, 70])
thermal = np.array([230, 90, 20, 28, 15, 60, 35, 150, 170, 210, 120, 45, 290, 75, 310, 190, 10, 250, 135, 270, 105])
flywheels = np.array([48, 35, 5, 130, 340, 250, 18, 200, 280, 150, 90, 7, 110, 13, 60, 310, 225, 175, 25, 75, 10])

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, batteries, hydropumped, thermal, flywheels,
             colors=['#4C9F70'], alpha=0.8)

ax.set_title('GreenValley Renewable Energy Storage Evolution (2020-2040)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Capacity (MWh)', fontsize=14)

plt.tight_layout()
plt.show()
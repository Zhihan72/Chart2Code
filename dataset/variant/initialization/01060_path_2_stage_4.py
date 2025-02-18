import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2031)

ai_growth = [5, 8, 12, 18, 25, 30, 38, 45, 55, 60, 65, 70, 75, 80, 85, 88, 90, 92, 94, 95, 96, 97, 98, 99, 100, 100, 100, 100, 100, 100, 100]
renewable_energy_growth = [10, 15, 20, 25, 30, 35, 40, 48, 55, 60, 65, 68, 72, 76, 79, 82, 85, 87, 89, 92, 94, 96, 97, 98, 99, 100, 100, 100, 100, 100, 100]
biotechnology_growth = [7, 10, 15, 20, 25, 30, 35, 42, 50, 55, 60, 65, 70, 75, 78, 82, 85, 88, 90, 92, 94, 95, 96, 97, 98, 99, 100, 100, 100, 100, 100]

ai_economic_impact = [1, 2, 4, 6, 10, 15, 20, 28, 35, 45, 55, 65, 75, 85, 95, 105, 120, 135, 150, 170, 190, 210, 225, 235, 245, 260, 270, 280, 290, 300, 310]
renewable_energy_economic_impact = [2, 3, 5, 8, 11, 16, 22, 30, 40, 50, 60, 72, 85, 95, 105, 120, 135, 150, 165, 180, 195, 210, 220, 230, 245, 260, 275, 290, 305, 320, 335]
biotechnology_economic_impact = [1, 1.5, 2.5, 4, 6, 9, 13, 19, 28, 36, 45, 56, 68, 80, 92, 105, 120, 135, 150, 170, 190, 210, 230, 250, 270, 290, 310, 330, 350, 370, 390]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

ax1.plot(years, ai_growth, label='AI Technology', marker='o', color='tab:blue', linestyle='-')
ax1.plot(years, renewable_energy_growth, label='Green Energy', marker='s', color='tab:blue', linestyle='--')
ax1.plot(years, biotechnology_growth, label='Bio-Tech Evolution', marker='d', color='tab:blue', linestyle=':')

ax1.set_title('Tech Progress:\n2000 to 2030', fontsize=16, pad=10)
ax1.set_xlabel('Timeline: Year', fontsize=12)
ax1.set_ylabel('Maturity Index Level', fontsize=12)
ax1.set_xticks(np.arange(2000, 2031, 2))
ax1.set_yticks(np.arange(0, 101, 10))
ax1.set_xlim(2000, 2030)
ax1.set_ylim(0, 100)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend(title='Innovations', loc='upper left', fontsize=10)

ax2.bar(years - 0.2, ai_economic_impact, width=0.2, label='AI Revenue', color='tab:blue')
ax2.bar(years, renewable_energy_economic_impact, width=0.2, label='Eco Energy Gain', color='tab:blue')
ax2.bar(years + 0.2, biotechnology_economic_impact, width=0.2, label='Bio Profit', color='tab:blue')

ax2.set_title('Tech Economics:\nBillions of USD (2000-2030)', fontsize=16, pad=10)
ax2.set_xlabel('Annual Measure', fontsize=12)
ax2.set_ylabel('Economic Value (USD billions)', fontsize=12)
ax2.set_xticks(np.arange(2000, 2031, 2))
ax2.set_xlim(2000, 2030)
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.legend(title='Sectors', loc='upper left', fontsize=10)

plt.tight_layout()
plt.show()
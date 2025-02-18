import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar = np.array([10, 15, 20, 30, 45, 60, 80, 110, 150, 195, 250])
wind = np.array([40, 55, 70, 90, 110, 130, 160, 200, 250, 310, 380])
hydroelectric = np.array([300, 305, 310, 320, 330, 340, 350, 365, 380, 395, 410])

plt.figure(figsize=(12, 7))

plt.stackplot(years, hydroelectric, solar, wind,
              labels=['Hydro', 'Solar', 'Wind'],
              colors=['#1f77b4'],
              alpha=0.6, linestyle='--')

plt.title("Renewable Growth: 2010-2020", fontsize=14, fontweight='bold')
plt.xlabel("Yr", fontsize=10)
plt.ylabel("Production (PWh)", fontsize=10)

plt.legend(loc='lower center', fontsize=9, title='Types', title_fontsize='10')

plt.grid(True, linestyle=':', linewidth=0.7, alpha=0.5)

plt.tight_layout()
plt.show()
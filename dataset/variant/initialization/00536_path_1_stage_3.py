import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

solar = np.array([15, 20, 10, 45, 30, 250, 80, 110, 195, 60, 150])
wind = np.array([310, 40, 70, 90, 130, 250, 55, 200, 110, 380, 160])
hydroelectric = np.array([395, 310, 410, 330, 320, 340, 365, 305, 300, 350, 380])
biomass = np.array([52, 58, 50, 66, 62, 70, 85, 74, 55, 90, 79])

plt.figure(figsize=(12, 7))

plt.stackplot(years, solar, wind, hydroelectric, biomass, 
              labels=['Wind Force', 'Water Power', 'Bioenergy', 'Solar Power'],
              colors=['#cc99ff', '#66b3ff', '#ffcc00', '#99ff99'], 
              alpha=0.85)

plt.title("Exploring Renewable Energy Sources\n2010-2020", fontsize=18, style='italic')
plt.xlabel("Years", fontsize=13, style='oblique')
plt.ylabel("Energy Output (PWh)", fontsize=13, style='oblique')

plt.legend(loc='upper right', fontsize=11, title='Energy Source', shadow=True, frameon=True)
plt.grid(visible=True, linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()
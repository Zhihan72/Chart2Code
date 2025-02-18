import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

solar = np.array([10, 15, 20, 30, 45, 60, 80, 110, 150, 195, 250])
wind = np.array([40, 55, 70, 90, 110, 130, 160, 200, 250, 310, 380])
hydroelectric = np.array([300, 305, 310, 320, 330, 340, 350, 365, 380, 395, 410])
biomass = np.array([50, 52, 55, 58, 62, 66, 70, 74, 79, 85, 90])

plt.figure(figsize=(12, 7))

plt.stackplot(years, solar, wind, hydroelectric, biomass, 
              labels=['Bioenergy', 'Water Power', 'Solar Power', 'Wind Force'],
              colors=['#ffcc00', '#66b3ff', '#99ff99', '#cc99ff'], 
              alpha=0.8)

plt.title("A Glimpse at Green Power\n2010-2020", fontsize=16)
plt.xlabel("Timeline", fontsize=12)
plt.ylabel("Production (PWh)", fontsize=12)

plt.legend(loc='upper left', fontsize=10, title='Power Types', bbox_to_anchor=(1, 1))

plt.tight_layout()

plt.show()
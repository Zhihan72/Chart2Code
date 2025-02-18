import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

# Randomly altering the content within the energy arrays
solar = np.array([15, 20, 10, 45, 30, 250, 80, 110, 195, 60, 150])
wind = np.array([310, 40, 70, 90, 130, 250, 55, 200, 110, 380, 160])
hydroelectric = np.array([395, 310, 410, 330, 320, 340, 365, 305, 300, 350, 380])
biomass = np.array([52, 58, 50, 66, 62, 70, 85, 74, 55, 90, 79])

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
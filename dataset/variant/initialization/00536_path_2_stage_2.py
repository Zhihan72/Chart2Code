import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar = np.array([10, 15, 20, 30, 45, 60, 80, 110, 150, 195, 250])
wind = np.array([40, 55, 70, 90, 110, 130, 160, 200, 250, 310, 380])
hydroelectric = np.array([300, 305, 310, 320, 330, 340, 350, 365, 380, 395, 410])

plt.figure(figsize=(12, 7))

# Alter the order and appearance of the stacks
plt.stackplot(years, hydroelectric, solar, wind,
              labels=['Hydroelectric', 'Solar', 'Wind'],
              colors=['#99ff99', '#ffcc00', '#66b3ff'],
              alpha=0.6, linestyle='--')

# Change title font size and style
plt.title("Renewable Growth Across a Decade: 2010-2020", fontsize=14, fontweight='bold')
plt.xlabel("Year", fontsize=10)
plt.ylabel("Energy Production (PWh)", fontsize=10)

# Modify legend location and remove the bounding box
plt.legend(loc='lower center', fontsize=9, title='Sources', title_fontsize='10')

# Add grid for emphasis
plt.grid(True, linestyle=':', linewidth=0.7, alpha=0.5)

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import numpy as np

energy_consumption = [
    150, 155, 160, 162, 165, 170, 175, 180, 185, 188, 190, 195, 198, 200, 205,
    210, 215, 220, 223, 225, 230, 235, 238, 240, 245, 250, 255, 258, 260, 265,
    270, 275, 278, 280, 285, 290, 295, 300, 310, 320, 330, 340, 350, 360, 370,
    380, 390, 400, 410, 420, 425, 430, 435, 440, 445, 450, 460, 470, 480, 490,
    200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270,
    275, 280, 285, 290, 295, 300, 305, 310, 315, 320, 325, 330, 335, 340, 345,
    350, 355, 360, 365, 370, 375, 380, 385, 390, 395
]

# New group representing higher consumption
energy_consumption_high = [
    500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640,
    650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790,
    800, 810, 820, 830, 840, 850
]

# Combine the original data and the new high consumption data
combined_energy_consumption = energy_consumption + energy_consumption_high

plt.figure(figsize=(12, 8))
plt.hist(combined_energy_consumption, bins=20, color='mediumseagreen', edgecolor='black', alpha=0.8)

plt.title('Ecohaven Energy Usage: Exploring High Consumption Units', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Energy Used (Gigawatt-hours)', fontsize=12)
plt.ylabel('Neighborhood Count', fontsize=12)

plt.grid(True, linestyle='--', alpha=0.5)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

plt.tight_layout()
plt.show()
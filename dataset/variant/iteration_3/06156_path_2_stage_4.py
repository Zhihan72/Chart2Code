import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
salmon_catches = [115, 138, 153, 158, 150, 142, 134, 147, 163, 175, 188]
tuna_catches = [205, 225, 215, 212, 198, 192, 185, 170, 170, 155, 148]
cod_catches = [295, 315, 305, 300, 290, 275, 265, 255, 250, 245, 235]

fig, ax1 = plt.subplots(figsize=(14, 8))

# Replacing original colors with new ones
ax1.plot(years, salmon_catches, marker='x', linestyle='--', linewidth=1.5, color='green', label='Catch of Salmon')
ax1.plot(years, tuna_catches, marker='d', linestyle='-.', linewidth=1.5, color='blue', label='Catch of Tuna')
ax1.plot(years, cod_catches, marker='v', linestyle=':', linewidth=1.5, color='red', label='Catch of Cod')

ax1.set_title("Charting Fish Hauls (2010-2020)\nA View on Variability of Output", fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel("Yearly Details", fontsize=14)
ax1.set_ylabel("Total Catch (tons)", fontsize=14)

ax1.grid(True, linestyle='-', alpha=0.8)
ax1.legend(title='Species of Fish', fontsize=12, loc='lower right')

ax1.text(2011, 185, 'Enhanced Salmon\nCapture Techniques', fontsize=10, ha='center', color='green', backgroundcolor='white')
ax1.text(2014, 265, 'Marginal Dip\nDue to Intensive Fishing', fontsize=10, ha='center', color='red', backgroundcolor='white')

plt.tight_layout()

plt.show()
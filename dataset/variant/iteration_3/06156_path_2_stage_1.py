import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

# Modified artificial data representing catches in tons for three species of fish
salmon_catches = [115, 138, 153, 158, 150, 142, 134, 147, 163, 175, 188]
tuna_catches = [205, 225, 215, 212, 198, 192, 185, 170, 170, 155, 148]
cod_catches = [295, 315, 305, 300, 290, 275, 265, 255, 250, 245, 235]

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(years, salmon_catches, marker='o', linestyle='-', linewidth=2, color='salmon', label='Salmon Catches')
ax1.plot(years, tuna_catches, marker='s', linestyle='-', linewidth=2, color='dodgerblue', label='Tuna Catches')
ax1.plot(years, cod_catches, marker='^', linestyle='-', linewidth=2, color='darkgreen', label='Cod Catches')

ax1.set_title("Decadal Analysis of Seafood Catches in Coastal Town (2010-2020)\nUnderstanding Yield Fluctuations", fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=14)
ax1.set_ylabel("Catch Yield (tons)", fontsize=14)

ax1.grid(True, linestyle='--', alpha=0.6)

ax1.legend(title='Fish Species', fontsize=12, loc='upper left')

ax1.annotate('Significant drop in Tuna Catches', xy=(2017, 170), xytext=(2014, 245),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
             fontsize=12, color='black')

ax1.text(2011, 185, 'Improved Salmon\nFishing Methods', fontsize=10, ha='center', color='salmon', backgroundcolor='white')
ax1.text(2014, 265, 'Slight Decrease\nDue to Overfishing', fontsize=10, ha='center', color='darkgreen', backgroundcolor='white')

plt.tight_layout()

plt.show()
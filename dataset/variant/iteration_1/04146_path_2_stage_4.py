import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2020, 2110)

carbon_emissions = np.array([
    56, 44, 42, 53, 51, 45, 47, 41, 49, 59, 
    62, 66, 43, 40, 46, 70, 75, 80, 85, 90, 
    96, 102, 108, 114, 120, 134, 127, 120, 114, 108,
    163, 171, 141, 148, 155, 171, 179, 187, 196, 205,
    253, 263, 274, 223, 214, 187, 205, 214, 205, 233,
    320, 298, 332, 358, 371, 384, 398, 412, 426, 440,
    485, 470, 455, 441, 423, 407, 398, 371, 358, 345,
    682, 610, 578, 502, 584, 580, 532, 516, 548, 564,
    668, 688, 708, 726, 744, 768, 791, 810, 829, 848
])

renewable_energy = np.array([
    72, 60, 66, 79, 50, 110, 119, 129, 139, 101, 
    86, 93, 55, 55, 72, 110, 119, 129, 119, 101, 
    254, 254, 269, 285, 225, 301, 239, 211, 301, 224, 
    409, 429, 449, 449, 491, 471, 353, 353, 531, 513, 
    790, 818, 847, 847, 606, 935, 631, 656, 739, 662, 
    1128, 1162, 1196, 1030, 967, 907, 900, 907, 847, 876, 
    2031, 2076, 2031, 2049, 2031, 1488, 1162, 1231, 1375, 1412, 
    1687, 1728, 1802, 1812, 1855, 1898, 1494, 1898, 1942, 1986, 
    2401, 2449, 2031, 1929, 1827, 2031, 2031, 2031, 2213, 2259
])

carbon_capture_investment = np.array([
    1, 6, 3, 8, 5, 2, 7, 4, 9, 12, 
    16, 14, 20, 25, 22, 14, 12, 30, 31, 31, 
    45, 37, 41, 49, 53, 54, 57, 49, 49, 49, 
    89, 67, 83, 89, 67, 77, 73, 67, 62, 49,
    151, 159, 151, 159, 151, 159, 113, 61, 223, 213,
    203, 203, 233, 248, 265, 276, 256, 276, 300, 312,
    338, 351, 365, 379, 393, 402, 355, 355, 365, 379,
    698, 437, 452, 468, 468, 548, 555, 548, 531, 548,
    858, 878, 778, 799, 820, 841, 871, 898, 900, 884
])

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, renewable_energy, carbon_capture_investment, carbon_emissions, 
             labels=['Green Power Growth', 'Investment in CO2 Tech', 'Carbon Footprint'], 
             colors=['#0000CD', '#FF4500', '#90EE90'], alpha=0.7)

ax.set_title('Climate Speculations: Investment vs. Emissions (2020-2100)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline', fontsize=12)
ax.set_ylabel('Metrics (GW / Billion $ / GT CO2e)', fontsize=12)
ax.legend(loc='upper right', title='Data Type', fontsize=9, frameon=True)
ax.grid(linestyle=':', alpha=0.8)

ax.annotate('Emission Surge', xy=(2060, 1000), xytext=(2040, 1150),
            arrowprops=dict(facecolor='orange', arrowstyle='->'),
            fontsize=11, color='orange')

ax.annotate('Renewables Boost', xy=(2070, 2300), xytext=(2045, 2400),
            arrowprops=dict(facecolor='darkgreen', arrowstyle='->'),
            fontsize=11, color='darkgreen')

ax.annotate('CO2 Capture Spike', xy=(2055, 280), xytext=(2035, 320),
            arrowprops=dict(facecolor='darkblue', arrowstyle='->'),
            fontsize=11, color='darkblue')

plt.tight_layout()
plt.show()
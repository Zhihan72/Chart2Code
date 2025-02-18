import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2020, 2110)

carbon_emissions = np.array([
    40, 41, 42, 43, 44, 45, 46, 47, 49, 51, 
    53, 56, 59, 62, 66, 70, 75, 80, 85, 90, 
    96, 102, 108, 114, 120, 127, 134, 141, 148, 155, 
    163, 171, 179, 187, 196, 205, 214, 223, 233, 243, 
    253, 263, 274, 285, 296, 308, 320, 332, 345, 358, 
    371, 384, 398, 412, 426, 440, 455, 470, 485, 500, 
    516, 532, 548, 564, 580, 596, 613, 630, 647, 664, 
    682, 700, 718, 736, 754, 772, 791, 810, 829, 848, 
    868, 888, 908, 928, 948, 968, 988, 1008, 1029, 1050
])

renewable_energy = np.array([
    50, 55, 60, 66, 72, 79, 86, 93, 101, 110, 
    119, 129, 139, 150, 161, 173, 185, 198, 211, 225, 
    239, 254, 269, 285, 301, 318, 335, 353, 371, 390, 
    409, 429, 449, 470, 491, 513, 535, 558, 582, 606, 
    631, 656, 682, 708, 735, 762, 790, 818, 847, 876, 
    906, 936, 967, 998, 1030, 1062, 1095, 1128, 1162, 1196, 
    1231, 1266, 1302, 1338, 1375, 1412, 1450, 1488, 1527, 1566, 
    1606, 1646, 1687, 1728, 1770, 1812, 1855, 1898, 1942, 1986, 
    2031, 2076, 2121, 2167, 2213, 2259, 2306, 2353, 2401, 2449
])

carbon_capture_investment = np.array([
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
    12, 14, 16, 18, 20, 22, 25, 28, 31, 34, 
    37, 41, 45, 49, 53, 57, 62, 67, 72, 77, 
    83, 89, 95, 101, 107, 114, 121, 128, 135, 143, 
    151, 159, 167, 176, 185, 194, 203, 213, 223, 233, 
    243, 254, 265, 276, 288, 300, 312, 325, 338, 351, 
    365, 379, 393, 407, 422, 437, 452, 468, 484, 500, 
    517, 534, 551, 568, 586, 604, 622, 641, 660, 679, 
    698, 718, 738, 758, 778, 799, 820, 841, 862, 884
])

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, renewable_energy, carbon_capture_investment, carbon_emissions, 
             labels=['Green Power Growth', 'Investment in CO2 Tech', 'Carbon Footprint'], 
             colors=['#8FBC8F', '#6495ED', '#FF6347'], alpha=0.8)

ax.set_title('Climate Speculations: Investment vs. Emissions (2020-2100)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline', fontsize=12)
ax.set_ylabel('Metrics (GW / Billion $ / GT CO2e)', fontsize=12)
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), title='Key Stats', fontsize=10, frameon=False)
ax.grid(linestyle='--', alpha=0.5)

ax.annotate('Emission Surge', xy=(2060, 1050), xytext=(2040, 1200),
            arrowprops=dict(facecolor='red', arrowstyle='->'),
            fontsize=10, color='red')

ax.annotate('Renewables Boost', xy=(2070, 2400), xytext=(2045, 2500),
            arrowprops=dict(facecolor='green', arrowstyle='->'),
            fontsize=10, color='green')

ax.annotate('CO2 Capture Spike', xy=(2055, 300), xytext=(2035, 350),
            arrowprops=dict(facecolor='blue', arrowstyle='->'),
            fontsize=10, color='blue')

plt.tight_layout()
plt.show()
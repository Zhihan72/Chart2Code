import numpy as np
import matplotlib.pyplot as plt

# Timeframe from 2020 to 2110
years = np.arange(2020, 2110)

# Carbon emissions (in gigatons of CO2 equivalents)
carbon_emissions = np.array([
    90, 41, 155, 43, 253, 56, 345, 47, 49, 371,
    102, 127, 410, 564, 580, 440, 332, 71, 134, 440,
    201, 210, 61, 155, 120, 650, 174, 690, 364, 177,
    96, 943, 196, 243, 758, 279, 312, 116, 366, 702,
    253, 730, 742, 285, 591, 308, 82, 665, 409, 651,
    358, 557, 248, 201, 426, 676, 455, 90, 485, 133,
    516, 523, 102, 480, 580, 112, 613, 58, 736, 648,
    571, 270, 718, 999, 336, 485, 913, 647, 264, 672,
    309, 546, 761, 795, 556, 968, 888, 974, 1029, 1050
])

# Renewable energy production (in gigawatts)
renewable_energy = np.array([
    1986, 65, 1450, 128, 84, 1987, 765, 999, 1180, 1670,
    256, 229, 1230, 1044, 161, 730, 1301, 198, 72, 324,
    567, 381, 269, 740, 465, 2124, 235, 453, 1629, 930,
    88, 29, 772, 118, 949, 452, 818, 576, 431, 76,
    898, 1080, 682, 569, 2335, 962, 730, 547, 47, 429,
    914, 2437, 1300, 943, 103, 1413, 265, 691, 1165, 210,
    1234, 739, 120, 1438, 985, 312, 1284, 422, 1427, 223,
    4318, 123, 2213, 221, 2820, 478, 1134, 1982, 459, 66,
    611, 2076, 1438, 172, 2259, 1266, 1302, 1746, 213, 243
])

# Investment in carbon capture technology (in billions of dollars)
carbon_capture_investment = np.array([
    57, 14, 16, 128, 5, 89, 145, 89, 128, 300,
    243, 154, 267, 368, 20, 215, 125, 88, 157, 34,
    40, 281, 245, 488, 423, 318, 3, 411, 62, 150,
    13, 89, 135, 401, 409, 261, 178, 700, 135, 225,
    15, 516, 67, 145, 235, 294, 192, 613, 723, 233,
    451, 354, 295, 76, 49, 108, 111, 132, 155, 376,
    222, 379, 618, 150, 343, 554, 122, 167, 373, 200,
    130, 534, 41, 168, 678, 113, 305, 225, 341, 508,
    698, 19, 738, 176, 99, 799, 445, 411, 262, 884
])

# Stacked area plot
fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, renewable_energy, carbon_capture_investment, carbon_emissions, 
             labels=['Renewable Energy Production', 'Carbon Capture Investment', 'Carbon Emissions'], 
             colors=['#8FBC8F', '#6495ED', '#FF6347'], alpha=0.8)

ax.set_title('Future Climate Scenarios: Investment and Emissions (2020-2100)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Values (Gigawatts / Billion $ / Gigatons CO2e)', fontsize=12)
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), title='Elements', fontsize=10, frameon=False)
ax.grid(linestyle='--', alpha=0.5)

ax.annotate('Rapid Rise in Emissions', xy=(2060, 1050), xytext=(2040, 1200),
            arrowprops=dict(facecolor='red', arrowstyle='->'),
            fontsize=10, color='red')

ax.annotate('Surge in Renewable Energy', xy=(2070, 2400), xytext=(2045, 2500),
            arrowprops=dict(facecolor='green', arrowstyle='->'),
            fontsize=10, color='green')

ax.annotate('Increased Investment in Carbon Capture', xy=(2055, 300), xytext=(2035, 350),
            arrowprops=dict(facecolor='blue', arrowstyle='->'),
            fontsize=10, color='blue')

plt.tight_layout()
plt.show()
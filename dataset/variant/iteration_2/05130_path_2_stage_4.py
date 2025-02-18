import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2100, 2151)

# Manually alter within each species' population maintaining the dimensional structure
mammals_population = np.array([5000, 5050, 5120, 5200, 5290, 5380, 5460, 5520, 5550, 5540,
                               5490, 5400, 5270, 5100, 4890, 4640, 4350, 4020, 3650, 3240,
                               2790, 2300, 1770, 1200, 590, 0, 80, 320, 700, 1220, 1890, 2710, 3670, 4770, 6000, 7360, 8840, 10440, 12160, 14000, 15960, 18040, 20240, 22560, 25000, 27560, 30240, 33040, 35960, 39000, 42160,])
birds_population = np.array([3000, 3050, 3120, 3190, 3270, 3350, 3440, 3540, 3650, 3770,
                             3900, 4040, 4190, 4350, 4520, 4700, 4890, 5090, 5300, 5520,
                             5750, 5990, 6240, 6500, 6770, 7050, 7340, 7640, 7950, 8270,
                             8600, 8940, 9290, 9650, 10020, 10400, 10850, 11300, 11770, 12250, 12740, 13240, 13750, 14270, 14800, 15340, 15900, 16470, 17050, 17640, 18240])
reptiles_population = np.array([3000, 3160, 3310, 3440, 3550, 3630, 3680, 3700, 3680, 3630,
                                3550, 3440, 3310, 3160, 3000, 2840, 2690, 2560, 2450, 2370,
                                2320, 2300, 2320, 2370, 2450, 2560, 2690, 2840, 3000, 3160,
                                3310, 3440, 3550, 3630, 3680, 3700, 3680, 3630, 3550, 3440, 3310, 3160, 3000, 2840, 2690, 2560, 2450, 2370, 2320, 2300, 2320])
amphibians_population = np.array([1500, 1528, 1556, 1585, 1614, 1643, 1673, 1703, 1734, 1765,
                                  1797, 1829, 1862, 1895, 1928, 1962, 1996, 2031, 2066, 2102,
                                  2138, 2174, 2211, 2248, 2286, 2324, 2362, 2401, 2440, 2479,
                                  2519, 2559, 2600, 2641, 2683, 2725, 2767, 2810, 2853, 2897, 2941, 2985, 3030, 3075, 3121, 3167, 3213, 3260, 3307, 3354, 3402])
fish_population = np.array([7000, 6950, 6900, 6850, 6800, 6750, 6700, 6650, 6600, 6550,
                            6500, 6450, 6400, 6350, 6300, 6250, 6200, 6150, 6100, 6050,
                            6000, 5950, 5900, 5850, 5800, 5750, 5700, 5650, 5600, 5550,
                            5500, 5450, 5400, 5350, 5300, 5250, 5200, 5150, 5100, 5050, 5000, 4950, 4900, 4850, 4800, 4750, 4700, 4650, 4600, 4550, 4500])

species_data = np.vstack([
    mammals_population,
    birds_population,
    reptiles_population,
    amphibians_population,
    fish_population
])

plt.figure(figsize=(16, 10))

plt.stackplot(years, species_data, labels=['Mam', 'Brd', 'Rep', 'Amp', 'Fish'],
              colors=['#FFD700', '#8B4513', '#7B68EE', '#4682B4', '#228B22'], alpha=0.7)

plt.title("Pop. Trends (2100-2150)", fontsize=18, fontweight='medium', color='#555555')
plt.xlabel("Year", fontsize=13, fontstyle='italic')
plt.ylabel("Pop. (000s)", fontsize=13, fontstyle='italic')

plt.xticks(years[::5], rotation=30)
plt.yticks(np.arange(0, 21000, 2500))
plt.grid(False)

plt.legend(loc='upper right', fontsize=10, facecolor='white', edgecolor='#DDDDDD')

plt.annotate('Brd Peak', xy=(2130, birds_population[30]), xytext=(2110, 19000),
             arrowprops=dict(arrowstyle='-[', color='gray'), fontsize=10, color='darkblue')
plt.annotate('Fish Decline', xy=(2140, fish_population[40]), xytext=(2120, 4000),
             arrowprops=dict(arrowstyle='-[', color='gray'), fontsize=10, color='darkred')

plt.tight_layout()

plt.show()
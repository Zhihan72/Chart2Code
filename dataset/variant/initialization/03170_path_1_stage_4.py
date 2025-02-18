import matplotlib.pyplot as plt

red_giants = {
    "Brightness": [70, 68, 72, 75, 74, 69, 71, 73],
    "Distance": [2500, 2400, 2600, 2550, 2450, 2350, 2650, 2500]
}

white_dwarfs = {
    "Brightness": [20, 22, 19, 21, 23, 24, 18, 25],
    "Distance": [3000, 3100, 2950, 3200, 3050, 3250, 3150, 3050]
}

main_sequence_stars = {
    "Brightness": [40, 45, 42, 44, 41, 47, 43, 46],
    "Distance": [4000, 3900, 4100, 4050, 3950, 4150, 4250, 4050]
}

neutron_stars = {
    "Brightness": [85, 88, 90, 86, 84, 87, 89, 91],
    "Distance": [1500, 1600, 1400, 1550, 1450, 1650, 1350, 1550]
}

plt.figure(figsize=(12, 8))

plt.scatter(red_giants["Distance"], red_giants["Brightness"], 
            color='blue', s=120, alpha=0.7, edgecolors='k')
plt.scatter(white_dwarfs["Distance"], white_dwarfs["Brightness"], 
            color='purple', s=120, alpha=0.7, edgecolors='k')
plt.scatter(main_sequence_stars["Distance"], main_sequence_stars["Brightness"], 
            color='red', s=120, alpha=0.7, edgecolors='k')
plt.scatter(neutron_stars["Distance"], neutron_stars["Brightness"], 
            color='green', s=120, alpha=0.7, edgecolors='k')

plt.title('Andromeda Galaxy Stars: Brightness vs Distance', fontsize=16, fontweight='bold')
plt.xlabel('Distance Light-years from Earth', fontsize=14)
plt.ylabel('Star Luminosity Level', fontsize=14)

plt.tight_layout()

plt.show()
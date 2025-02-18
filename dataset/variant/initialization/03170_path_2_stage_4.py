import matplotlib.pyplot as plt
import numpy as np

# Handcrafted data for different types of stars in the Andromeda Galaxy
red_giants = {
    "Brightness": [70, 68, 72, 75, 74, 69, 71, 73],
    "Distance": [2500, 2400, 2600, 2550, 2450, 2350, 2650, 2500]
}

main_sequence_stars = {
    "Brightness": [40, 45, 42, 44, 41, 47, 43, 46],
    "Distance": [4000, 3900, 4100, 4050, 3950, 4150, 4250, 4050]
}

plt.figure(figsize=(12, 8))

plt.scatter(red_giants["Distance"], red_giants["Brightness"], 
            color='orange', s=120, alpha=0.7, edgecolors='k')
plt.scatter(main_sequence_stars["Distance"], main_sequence_stars["Brightness"], 
            color='purple', s=120, alpha=0.7, edgecolors='k')

plt.title('Star Luminosity vs. Proximity\nfor Andromeda', fontsize=16, fontweight='bold')
plt.xlabel('Earth Proximity (ly)', fontsize=14)
plt.ylabel('Luminosity (units)', fontsize=14)

plt.tight_layout()

plt.show()
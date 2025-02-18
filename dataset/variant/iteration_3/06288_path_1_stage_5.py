import matplotlib.pyplot as plt
import numpy as np

species = ["Eldarian", "Ignitoid", "Galzor", "Xylok", "Andronian",
           "Zepherite", "Fermian", "Hydrixian", "Nebulon", "Vortix",
           "Lithorian", "Plazmoid", "Quarkian", "Solaran", "Astralan"]

weights = np.array([140, 180, 110, 95, 120, 150, 75, 170, 100, 130,
                    115, 185, 85, 190, 135])

new_colors = ['#FF5733', '#33FFBD', '#FF33F6', '#335BFF', '#FF8F33', 
              '#33FF57', '#FF3333', '#33D1FF', '#B833FF', '#33FF99',
              '#DFFF33', '#FF5733', '#33A8FF', '#FF33A8', '#33FF77']

fig, ax = plt.subplots(figsize=(12, 8))
bar = ax.barh(species, weights, color=new_colors, edgecolor='k', linewidth=2.5, hatch='/')

ax.set_title("Fictional Species Mass Spectrum", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Mass (Kilograms)", fontsize=12, fontstyle='italic')
ax.set_ylabel("Alien Types", fontsize=12, fontstyle='italic')

ax.grid(True, axis='x', linestyle=':', color='gray', alpha=0.9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.yaxis.grid(False)

plt.tight_layout()
plt.show()
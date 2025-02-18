import matplotlib.pyplot as plt
import numpy as np

species = ["Andronian", "Xylok", "Zepherite", "Fermian", "Galzor",
           "Ignitoid", "Hydrixian", "Eldarian", "Nebulon", "Vortix",
           "Lithorian", "Plazmoid", "Quarkian", "Solaran", "Astralan"]

weights = np.array([120, 95, 150, 75, 110, 180, 170, 140, 100, 130,
                    115, 185, 85, 190, 135])

# Define a new set of colors
new_colors = ['#FF5733', '#33FFBD', '#FF33F6', '#335BFF', '#FF8F33', 
              '#33FF57', '#FF3333', '#33D1FF', '#B833FF', '#33FF99',
              '#DFFF33', '#FF5733', '#33A8FF', '#FF33A8', '#33FF77']

fig, ax = plt.subplots(figsize=(12, 8))
bar = ax.barh(species, weights, color=new_colors, edgecolor='k', linewidth=2.5, hatch='/')

# Randomly altered stylistic elements
ax.set_title("The Galactic Fauna: Weights of Fictional Alien Species", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Weight (kg)", fontsize=12, fontstyle='italic')
ax.set_ylabel("Species", fontsize=12, fontstyle='italic')

# Change grid style
ax.grid(True, axis='x', linestyle=':', color='gray', alpha=0.9)

# Change border visibility
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Removing the grid on y-axis
ax.yaxis.grid(False)

plt.tight_layout()
plt.show()
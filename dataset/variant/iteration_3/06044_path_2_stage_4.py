import matplotlib.pyplot as plt
import squarify

universe_population = {
    "Planet Earth": {
        "Humans": 7800,
        "Animals": 4000,
        "Plant-life": 3500000
    },
    "Planet Xylarn": {
        "Xylarnians": 1200,
        "Flora": 800000,
        "Fauna": 3000
    },
    "Planet Nibiru": {
        "Nibirians": 600,
        "Megaflora": 200000,
        "Microfauna": 15000
    },
    "Planet Zog": {
        "Zogians": 1500,
        "Bioforms": 500000,
        "Synthetic Life": 100
    }
}

sizes = []
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', 
          '#c2c2f0', '#ffb3e6', '#ff6666', '#c4e17f',
          '#76d7c4', '#fdedec', '#f3e5ab', '#d6e09c']

for planet, species in universe_population.items():
    for spec, population in species.items():
        sizes.append(population)

plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, color=colors, alpha=0.8, pad=3, text_kwargs={'fontsize': 10, 'visible': False})

plt.axis('off')
plt.show()
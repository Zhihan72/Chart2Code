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

labels = []
sizes = []

# Assigning a static color manually as we are removing stylistic colors
color = '#4682b4'

# Prepare the data for the tree map
for planet, species in universe_population.items():
    for spec, population in species.items():
        labels.append(f"{spec}\n({population}K)")
        sizes.append(population)

plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, label=labels, color=color, alpha=0.8, pad=3, text_kwargs={'fontsize': 10})

plt.axis('off')

plt.show()
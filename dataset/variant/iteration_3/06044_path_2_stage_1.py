import matplotlib.pyplot as plt
import squarify

# Define the fictional universe's population distribution across different species and planets
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

# Prepare data for the tree map
labels = []
sizes = []
colors = []

# Assigning a vibrant color palette
color_palette = plt.cm.viridis.colors

# Loop through each planet and its species to prepare labels, sizes, and colors
planet_index = 0
for planet, species in universe_population.items():
    for spec, population in species.items():
        labels.append(f"{spec}\n({population}K)")
        sizes.append(population)
        colors.append(color_palette[planet_index % len(color_palette)])
    planet_index += 1

# Create the tree map
plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8, pad=3, text_kwargs={'fontsize': 10})

# Add title and adjust layout
plt.title('Population Distribution Across the Galaxy:\nAn Overview of Diverse Species', fontsize=16, fontweight='bold', pad=20)
plt.axis('off')
plt.tight_layout()

# Show the tree map
plt.show()
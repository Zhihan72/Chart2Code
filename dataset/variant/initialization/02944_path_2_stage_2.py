import matplotlib.pyplot as plt

energy_sources = ['Solar Energy', 'Wind Energy', 'Hydroelectric', 'Biomass', 'Fossil Fuels', 'Nuclear']
energy_distribution = [25, 20, 15, 10, 20, 10]
colors = ['#FFDB58', '#32CD32', '#4682B4', '#8B4513', '#808080', '#B0C4DE']

fig, ax = plt.subplots(figsize=(8, 8))

ax.pie(
    energy_distribution, labels=energy_sources, colors=colors,
    autopct='%1.1f%%', startangle=140, explode=(0.05, 0.05, 0.05, 0.05, 0.05, 0.05)
)

ax.set_title('Energy Mix in a Sustainable City\n2023', fontsize=16, fontweight='bold', pad=20)

plt.show()
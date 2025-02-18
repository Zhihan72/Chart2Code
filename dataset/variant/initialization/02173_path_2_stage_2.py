import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# Define the energy sources and their percentage share in EcoVille for 2023
energy_sources = ['Solar', 'Wind', 'Hydropower', 'Biomass', 'Fossil Fuels']
consumption_2023 = [30, 25, 20, 15, 10]

# Define a color gradient
gradient = cm.get_cmap('YlOrRd')(np.linspace(0.2, 0.8, len(energy_sources)))

# Create a subplot for 2023 data
fig, ax = plt.subplots(figsize=(7, 7))

wedges, texts, autotexts = ax.pie(
    consumption_2023, 
    labels=energy_sources, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=[gradient[i] for i in range(len(energy_sources))],
    wedgeprops=dict(width=0.3, edgecolor='w'),
    pctdistance=0.85
)

plt.setp(autotexts, size=9, weight="bold", color='white')

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

# Annotate solar energy to highlight growth
ax.annotate(
    'Increased Solar Investment',
    xy=(0.1, 0.5), xytext=(0.3, 0.7),
    arrowprops=dict(facecolor='black', shrink=0.05),
    fontsize=10, ha='center', color='#FDB813'
)

plt.tight_layout()
plt.show()
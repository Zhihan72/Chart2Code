import matplotlib.pyplot as plt

energy_sources = ['Solar', 'Wind', 'Hydroelectric', 'Biomass', 'Geothermal']
energy_proportions = [35, 30, 20, 10, 5]

# Shuffled version of the original color list
shuffled_colors = ['#32CD32', '#FFD700', '#8A2BE2', '#FF8C00', '#87CEEB']
explode = (0.1, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))
ax.pie(energy_proportions, labels=energy_sources, autopct='%1.1f%%', startangle=140, 
       colors=shuffled_colors, explode=explode, wedgeprops={'width': 0.3})

plt.show()
import matplotlib.pyplot as plt

# Existing energy sources and their proportions
energy_sources = ['Solar', 'Wind', 'Hydroelectric', 'Biomass', 'Geothermal']
energy_proportions = [35, 30, 20, 10, 5]

# Incorporate an additional data series: New Energy
additional_sources = ['Nuclear', 'Coal', 'Natural Gas']
additional_proportions = [10, 15, 25]

# Concatenate the original and additional data series
all_sources = energy_sources + additional_sources
all_proportions = energy_proportions + additional_proportions

# Combine shuffled colors for existing and new data series
shuffled_colors = ['#32CD32', '#FFD700', '#8A2BE2', '#FF8C00', '#87CEEB', '#A52A2A', '#708090', '#FF4500']
explode = (0.1, 0, 0, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))
ax.pie(all_proportions, labels=all_sources, autopct='%1.1f%%', startangle=140, 
       colors=shuffled_colors, explode=explode[:len(all_sources)], wedgeprops={'width': 0.3})

plt.show()
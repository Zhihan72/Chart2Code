import matplotlib.pyplot as plt

# Energy sources and proportions
sources = ['Solar', 'Wind', 'Hydro', 'Biomass', 'Geo', 'Nuclear', 'Coal', 'Gas']
proportions = [35, 30, 20, 10, 5, 10, 15, 25]

# Shuffled colors for the data series
shuffled_colors = ['#32CD32', '#FFD700', '#8A2BE2', '#FF8C00', '#87CEEB', '#A52A2A', '#708090', '#FF4500']
explode = (0.1, 0, 0, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))
ax.pie(proportions, labels=sources, autopct='%1.1f%%', startangle=140, 
       colors=shuffled_colors, explode=explode, wedgeprops={'width': 0.3})

plt.show()
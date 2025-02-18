import matplotlib.pyplot as plt

# Data for a single city
cities = ['City A']
population_density = [5000]

fig, ax = plt.subplots(figsize=(14, 8))

# Plotting horizontal density bar plot
ax.barh(cities, population_density, color='skyblue', edgecolor='black', alpha=0.8)

ax.set_title("Population Density: A Comparative Chart of Urban Environments", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Population Density (people/sq km)', fontsize=12)

plt.xlim(4000, 7500)

plt.tight_layout()
plt.show()
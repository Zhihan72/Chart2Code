import matplotlib.pyplot as plt
import numpy as np

countries = ['Ita.', 'USA', 'Bra.', 'Ger.', 'Swi.', 
             'Den.', 'Ice.', 'Nor.', 'Swe.', 'Fin.']
consumption = np.array([4.0, 4.5, 5.0, 6.5, 7.9, 8.5, 9.0, 9.8, 10.5, 12.0])

color_map = plt.get_cmap("YlGnBu")
colors = color_map(np.linspace(0.3, 0.9, len(countries)))

colors_sorted = [
    colors[9], colors[8], colors[2], colors[6], colors[4], 
    colors[0], colors[3], colors[7], colors[1], colors[5]
]

fig, ax = plt.subplots(figsize=(12, 8))

ax.barh(countries, consumption, color=colors_sorted, height=0.6)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

ax.xaxis.grid(False)

plt.tight_layout()
plt.show()
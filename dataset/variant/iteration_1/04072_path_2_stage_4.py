import matplotlib.pyplot as plt
import numpy as np

energy_sources = ['Hydro', 'Sol', 'Wnd', 'Oth', 'Geo', 'Bio']
percentages = [18, 23, 27, 12, 8, 12]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
explode = (0, 0, 0.1, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 8))

# Donut pie chart
wedges, texts, autotexts = ax.pie(
    percentages,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)

# Creating the donut shape by drawing a white circle in the middle
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

for autotext in autotexts:
    autotext.set_color('black')

ax.axis('equal')

years = np.arange(2012, 2023)
growth = [8, 10, 12, 15, 18, 21, 24, 28, 32, 35, 40]
ax_inset = fig.add_axes([0.8, 0.1, 0.15, 0.3])
ax_inset.bar(years, growth, color='skyblue')

plt.show()
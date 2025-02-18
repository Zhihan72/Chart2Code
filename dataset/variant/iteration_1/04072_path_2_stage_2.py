import matplotlib.pyplot as plt
import numpy as np

# Data for renewable energy sources in 2022
energy_sources = ['Wnd', 'Sol', 'Hydro', 'Bio', 'Geo', 'Oth']
percentages = [27, 23, 18, 12, 8, 12]

# Colors for each energy source
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Emphasize 'Wind' sector
explode = (0.1, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 8))

# Pie chart
ax.pie(
    percentages,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)

ax.axis('equal')

# Inset bar chart for energy growth
years = np.arange(2012, 2023)
growth = [8, 10, 12, 15, 18, 21, 24, 28, 32, 35, 40]

ax_inset = fig.add_axes([0.8, 0.1, 0.15, 0.3])
ax_inset.bar(years, growth, color='skyblue')

plt.show()
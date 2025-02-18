import matplotlib.pyplot as plt
import numpy as np

# Data representing the global energy mix percentages for various renewable energy sources in 2022
energy_sources = ['Wind', 'Solar', 'Hydropower', 'Biomass', 'Geothermal', 'Other']
percentages = [27, 23, 18, 12, 8, 12]

# Colors chosen to represent each renewable energy source
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Explode configuration to emphasize 'Wind' sector
explode = (0.1, 0, 0, 0, 0, 0)

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Create the pie chart
ax.pie(
    percentages,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)

# Ensure the pie chart is a circle
ax.axis('equal')

# Create an inset bar chart showing renewable energy growth over the past decade
years = np.arange(2012, 2023)
growth = [8, 10, 12, 15, 18, 21, 24, 28, 32, 35, 40]

# Create an inset axes at the specified position within the main chart
ax_inset = fig.add_axes([0.8, 0.1, 0.15, 0.3])
ax_inset.bar(years, growth, color='skyblue')

plt.show()
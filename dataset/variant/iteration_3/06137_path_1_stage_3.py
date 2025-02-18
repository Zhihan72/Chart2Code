import numpy as np
import matplotlib.pyplot as plt

# Years for the x-axis
years = np.array(['2000', '2005', '2010', '2015', '2020'])

# Number of households owning each pet type (data in millions)
dogs = np.array([60, 65, 70, 75, 80])
cats = np.array([55, 58, 60, 62, 65])
birds = np.array([15, 20, 22, 25, 28])
fish = np.array([30, 32, 35, 38, 40])

# Colors for each pet type
colors = ['#3cb44b', '#4363d8', '#e6194b', '#ffe119']

fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(years, dogs, color=colors[0], alpha=0.9)
ax.bar(years, cats, bottom=dogs, color=colors[1], alpha=0.9)
ax.bar(years, birds, bottom=dogs + cats, color=colors[2], alpha=0.9)
ax.bar(years, fish, bottom=dogs + cats + birds, color=colors[3], alpha=0.9)

# Remove the borders by setting them to invisible
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Automatically adjust the layout to fit everything nicely
plt.tight_layout()

plt.show()
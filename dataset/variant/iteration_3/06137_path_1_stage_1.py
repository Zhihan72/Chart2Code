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
colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8']

# Create the stacked bar chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(years, dogs, color=colors[0], label='Dogs', alpha=0.9)
ax.bar(years, cats, bottom=dogs, color=colors[1], label='Cats', alpha=0.9)
ax.bar(years, birds, bottom=dogs + cats, color=colors[2], label='Birds', alpha=0.9)
ax.bar(years, fish, bottom=dogs + cats + birds, color=colors[3], label='Fish', alpha=0.9)

# Title and labels
ax.set_title("Rise in Different Pet Ownership Types Over Two Decades", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Number of Households (in millions)", fontsize=12)

# Rotate x-axis labels to prevent overlap
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

# Add a legend with larger spacing to avoid overlap
ax.legend(loc='upper left', title="Pet Types", bbox_to_anchor=(1.05, 1), fontsize=10, title_fontsize='12', frameon=False)

# Automatically adjust the layout to fit everything nicely
plt.tight_layout()

# Display the plot
plt.show()
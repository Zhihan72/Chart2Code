import numpy as np
import matplotlib.pyplot as plt

# Updated values with shuffled labels
xticks = np.array(['2010', '2000', '2020', '2005', '2015'])

# Data remains the same
dogs = np.array([60, 65, 70, 75, 80])
cats = np.array([55, 58, 60, 62, 65])
birds = np.array([15, 20, 22, 25, 28])
fish = np.array([30, 32, 35, 38, 40])

colors = ['#3cb44b', '#4363d8', '#e6194b', '#ffe119']

fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(xticks, dogs, color=colors[0], alpha=0.9)
ax.bar(xticks, cats, bottom=dogs, color=colors[1], alpha=0.9)
ax.bar(xticks, birds, bottom=dogs + cats, color=colors[2], alpha=0.9)
ax.bar(xticks, fish, bottom=dogs + cats + birds, color=colors[3], alpha=0.9)

ax.set_title('Popular Pets Over the Years', fontsize=18)
ax.set_xlabel('Different Time Periods', fontsize=14)
ax.set_ylabel('Homes Owning Pets (in millions)', fontsize=14)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()
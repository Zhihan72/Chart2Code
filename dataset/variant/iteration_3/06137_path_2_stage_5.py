import numpy as np
import matplotlib.pyplot as plt

years = np.array(['2000', '2005', '2010', '2015', '2020'])
dogs = np.array([60, 65, 70, 75, 80])
cats = np.array([55, 58, 60, 62, 65])
birds = np.array([15, 20, 22, 25, 28])
fish = np.array([30, 32, 35, 38, 40])
reptiles = np.array([5, 7, 9, 10, 12])
small_mammals = np.array([10, 12, 14, 16, 18])
rabbits = np.array([8, 11, 13, 15, 17])
hamsters = np.array([7, 9, 10, 12, 13])

colors = ['#4363d8', '#e6194b', '#911eb4', '#3cb44b', '#f58231', '#ffe119', '#bfef45', '#fabed4']

bar_width = 0.10
x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(12, 8))

ax.bar(x - bar_width * 3.5, dogs, width=bar_width, color=colors[0], alpha=0.9, label='Woofers')
ax.bar(x - bar_width * 2.5, cats, width=bar_width, color=colors[1], alpha=0.9, label='Felines')
ax.bar(x - bar_width * 1.5, birds, width=bar_width, color=colors[2], alpha=0.9, label='Avians')
ax.bar(x - bar_width * 0.5, fish, width=bar_width, color=colors[3], alpha=0.9, label='Swimmers')
ax.bar(x + bar_width * 0.5, reptiles, width=bar_width, color=colors[4], alpha=0.9, label='Scalies')
ax.bar(x + bar_width * 1.5, small_mammals, width=bar_width, color=colors[5], alpha=0.9, label='Tiny Furries')
ax.bar(x + bar_width * 2.5, rabbits, width=bar_width, color=colors[6], alpha=0.9, label='Hoppers')
ax.bar(x + bar_width * 3.5, hamsters, width=bar_width, color=colors[7], alpha=0.9, label='Nibblers')

ax.set_xticks(x)
ax.set_xticklabels(['Y2K', '05', 'Ten Years', 'Year 15', 'New Decade'], rotation=45, ha='right')

ax.set_title("Pet Popularities Over Time")
ax.set_xlabel("Time Period")
ax.set_ylabel("Counts of Pets")

ax.legend()

plt.tight_layout()
plt.show()
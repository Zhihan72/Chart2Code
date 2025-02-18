import numpy as np
import matplotlib.pyplot as plt

xticks = np.array(['2010', '2000', '2020', '2005', '2015'])
dogs = np.array([60, 65, 70, 75, 80])
cats = np.array([55, 58, 60, 62, 65])
birds = np.array([15, 20, 22, 25, 28])
fish = np.array([30, 32, 35, 38, 40])

colors = ['#3cb44b', '#4363d8', '#e6194b', '#ffe119']

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.2
x = np.arange(len(xticks)) 

ax.bar(x, dogs, width=bar_width, color=colors[0], label='Dogs', alpha=0.9)
ax.bar(x + bar_width, cats, width=bar_width, color=colors[1], label='Cats', alpha=0.9)
ax.bar(x + 2*bar_width, birds, width=bar_width, color=colors[2], label='Birds', alpha=0.9)
ax.bar(x + 3*bar_width, fish, width=bar_width, color=colors[3], label='Fish', alpha=0.9)

ax.set_xticks(x + bar_width * 1.5)
ax.set_xticklabels(xticks)

ax.set_title('Popular Pets Over the Years', fontsize=18)
ax.set_xlabel('Different Time Periods', fontsize=14)
ax.set_ylabel('Homes Owning Pets (in millions)', fontsize=14)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

ax.legend()

plt.tight_layout()
plt.show()
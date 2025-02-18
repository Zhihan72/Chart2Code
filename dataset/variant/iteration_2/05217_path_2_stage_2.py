import matplotlib.pyplot as plt
import numpy as np

child_sleep = [10, 11, 9, 10, 8.5, 9, 10.5, 11, 12, 8]
teen_sleep = [7, 8, 7.5, 7, 6.5, 8, 9, 7, 6, 8.5]
adult_sleep = [6, 6.5, 7, 5.5, 7.5, 6, 7, 8, 6, 5]
senior_sleep = [5.5, 6, 6.5, 5, 6, 7, 5.5, 6, 5, 6]

fig, (ax2, ax1) = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))

bins = np.linspace(4.5, 12, 15)
ax2.hist([child_sleep, teen_sleep, adult_sleep, senior_sleep], 
         bins=bins, rwidth=0.9)
ax2.grid(True, alpha=0.5, linestyle='--')

colors = ['skyblue', 'lightcoral', 'lightgreen', 'orchid']
for i, data in enumerate([child_sleep, teen_sleep, adult_sleep, senior_sleep]):
    ax1.hist(data, bins=bins, alpha=0.6, color=colors[i], edgecolor='black')

plt.tight_layout()
plt.show()
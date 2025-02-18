import matplotlib.pyplot as plt
import numpy as np

years = np.array([2019, 2020, 2021, 2022, 2023])
gardens_created = np.array([5, 15, 25, 40, 60])
volunteers_joined = np.array([50, 120, 180, 250, 320])
average_area = np.array([200, 250, 300, 350, 400])

fig, ax1 = plt.subplots(figsize=(10, 6))

bar_width = 0.35
ax1.bar(years - bar_width/2, gardens_created, bar_width, color='#66c2a5')
ax2 = ax1.twinx()
ax2.bar(years + bar_width/2, volunteers_joined, bar_width, color='#fc8d62')
ax2.plot(years, average_area, color='blue', marker='o', linestyle='-', lw=2, markerfacecolor='blue')

ax1.set_xticks(years)
ax1.set_xticklabels([])

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import numpy as np

years = np.array([2019, 2020, 2021, 2022, 2023])
gardens_created = np.array([5, 15, 25, 40, 60])
volunteers_joined = np.array([50, 120, 180, 250, 320])
average_area = np.array([200, 250, 300, 350, 400])

fig, ax1 = plt.subplots(figsize=(10, 6))

bar_width = 0.35
ax1.barh(years - bar_width/2, gardens_created, bar_width, color='#66c2a5', label='Gardens Created')
ax2 = ax1.twiny()
ax2.barh(years + bar_width/2, volunteers_joined, bar_width, color='#fc8d62', label='Volunteers Joined')
ax2.plot(average_area, years, color='blue', marker='o', linestyle='-', lw=2, markerfacecolor='blue', label='Average Area')

ax1.set_yticks(years)
ax1.set_yticklabels(years)

plt.tight_layout()
plt.show()
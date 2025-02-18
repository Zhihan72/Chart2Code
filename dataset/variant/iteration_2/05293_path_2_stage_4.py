import matplotlib.pyplot as plt
import numpy as np

weeks = np.arange(1, 53)

spring_park_visitors = [
    5, 6, 6.5, 7, 6.8, 9, 10, 11, 12, 10.5, 11, 13, 14, 15, 16.5,
    17, 18, 18.5, 17, 16, 16.5, 15.5, 14, 13.5, 13, 12.5, 10, 9.5,
    8, 7.5, 7, 6.5, 6, 6.2, 6.8, 7.2, 7.8, 9, 9.5, 10, 10.5, 11,
    11.5, 12, 12.3, 11.7, 11, 10.2, 9.8, 9.5, 9, 9
]

ocean_park_visitors = [
    8, 7.5, 7.8, 8.5, 8.8, 9.2, 10.1, 10.7, 10.5, 11, 11.5, 13, 13.5,
    14.2, 15, 17, 16.5, 16, 15.5, 15, 14.2, 13, 12, 11.5, 11, 10.8,
    10, 9.8, 9.2, 8.8, 8.5, 8.2, 8, 7.5, 7.2, 7, 7.5, 8, 8.5, 9,
    9.5, 10, 10.8, 11, 11.5, 11.8, 11.2, 10.7, 10.5, 10, 9.7, 9.5
]

mountain_park_visitors = [
    3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10,
    10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 15, 
    14.5, 14, 13.5, 13, 12.5, 12, 11.5, 11, 10.5, 10, 9.8, 9.5,
    9.2, 9, 8.8, 8.5, 8.2, 8, 7.8, 7.5, 7.2, 7, 6.8, 6.5, 6
]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(weeks, spring_park_visitors, marker='o', color='orange', linewidth=2)
ax.plot(weeks, ocean_park_visitors, marker='s', color='purple', linewidth=2)
ax.plot(weeks, mountain_park_visitors, marker='^', color='green', linewidth=2)

ax.set_xticks(np.arange(0, 53, 4))
ax.set_yticks(np.arange(0, 20, 2))

plt.tight_layout()
plt.show()
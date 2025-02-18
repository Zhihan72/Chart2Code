import numpy as np
import matplotlib.pyplot as plt

decades = np.arange(1970, 2030, 10)

# Data groups after removing 'disco'
rock = [40, 35, 25, 15, 10, 5]
pop = [10, 15, 25, 30, 35, 40]
hip_hop = [0, 0, 10, 20, 25, 30]
electronic = [5, 10, 15, 20, 20, 15]
indie = [0, 0, 5, 10, 10, 10]

# Stack the data excluding 'disco'
stacked_data = np.vstack([rock, pop, hip_hop, electronic, indie])

streaming_services = [0, 0, 5, 20, 50, 70]

fig, ax1 = plt.subplots(figsize=(14, 8))

# Adjusted colors array to match the reduced number of categories
altered_colors = ['#bbf7d0', '#fef3c7', '#c7d2fe', '#fca5a5', '#a5f3fc']
ax1.stackplot(decades, stacked_data, colors=altered_colors, alpha=0.6)

ax1.set_xticks(decades)
ax1.grid(axis='x', linestyle='-', alpha=0.8)

ax2 = ax1.twinx()
ax2.plot(decades, streaming_services, color='navy', linestyle='-', marker='s')

plt.tight_layout()
plt.show()
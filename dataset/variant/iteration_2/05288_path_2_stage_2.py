import matplotlib.pyplot as plt
import numpy as np

allocations = [30, 20, 15, 10, 15, 10]  # Budget allocations as percentages
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']

plt.figure(figsize=(12, 7))

# Subplot 1: Pie Chart
ax1 = plt.subplot(121)
ax1.pie(
    allocations, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors
)

# Subplot 2: Bar Chart
quarter_allocations = [
    [7, 5, 4, 3, 4, 2],  # Q1
    [8, 5, 4, 2, 4, 3],  # Q2
    [7, 5, 4, 2, 4, 3],  # Q3
    [8, 5, 3, 3, 3, 2]   # Q4
]
quarter_allocations = np.array(quarter_allocations).T

ax2 = plt.subplot(122)
bar_width = 0.35
ind = np.arange(len(quarter_allocations[0]))
bottom = np.zeros(len(quarter_allocations[0]))

for i, allocation in enumerate(quarter_allocations):
    ax2.bar(
        ind, 
        allocation, 
        bar_width, 
        bottom=bottom, 
        color=colors[i]
    )
    bottom += allocation

# Display the plot
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Randomly altered quarter labels
quarters = ['Second Quarter', 'One Quarter', 'Fourth Quarter', 'Three Quarters']

quarter_allocations = [
    [6, 6, 5, 3, 3, 2],  
    [7, 6, 4, 2, 4, 2],  
    [7, 5, 5, 3, 3, 2],  
    [5, 5, 4, 4, 4, 2]   
]

quarter_allocations = np.array(quarter_allocations).T
sorted_allocations = np.sort(quarter_allocations, axis=0)

plt.figure(figsize=(8, 7))
bar_width = 0.35
ind = np.arange(len(quarters))
bottom = np.zeros(len(quarters))
single_color = '#66b3ff'

for allocation in sorted_allocations:
    plt.bar(
        ind,
        allocation,
        bar_width,
        bottom=bottom,
        color=single_color,
        edgecolor='black'
    )
    bottom += allocation

# Randomly altered x and y labels, and title
plt.xticks(ind, quarters)
plt.ylabel('Distribution Percentage')
plt.title('Quarterly Allocation Visualization')

plt.tight_layout()
plt.show()
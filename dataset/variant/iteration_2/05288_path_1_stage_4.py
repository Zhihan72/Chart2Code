import matplotlib.pyplot as plt
import numpy as np

quarters = ['Q1', 'Q2', 'Q3', 'Q4']

quarter_allocations = [
    [6, 6, 5, 3, 3, 2],  
    [7, 6, 4, 2, 4, 2],  
    [7, 5, 5, 3, 3, 2],  
    [5, 5, 4, 4, 4, 2]   
]

quarter_allocations = np.array(quarter_allocations).T

# Sort allocations in ascending order for each quarter
sorted_allocations = np.sort(quarter_allocations, axis=0)

plt.figure(figsize=(8, 7))
bar_width = 0.35
ind = np.arange(len(quarters))

# Plot sorted bar chart
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

plt.xticks(ind, quarters)
plt.ylabel('Percentage Allocation')
plt.title('Sorted Bar Chart of Quarterly Allocations')

plt.tight_layout()
plt.show()
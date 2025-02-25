import matplotlib.pyplot as plt
import numpy as np

sectors = [
    'Research & Development', 
    'Marketing & Sales', 
    'Operations & Maintenance', 
    'Employee Welfare', 
    'Infrastructure', 
    'Corporate Social Responsibility'
]

allocations = [25, 22, 18, 12, 13, 10]

single_color = '#66b3ff'

plt.figure(figsize=(12, 7))

# Subplot 1: Pie Chart
ax1 = plt.subplot(121)
ax1.pie(
    allocations, 
    colors=[single_color]*len(sectors),  
    startangle=140,
    explode=(0.1, 0, 0, 0, 0, 0),
    wedgeprops={'edgecolor': 'black'}
)

# Subplot 2: Bar Chart
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

quarter_allocations = [
    [6, 6, 5, 3, 3, 2],  
    [7, 6, 4, 2, 4, 2],  
    [7, 5, 5, 3, 3, 2],  
    [5, 5, 4, 4, 4, 2]   
]
quarter_allocations = np.array(quarter_allocations).T

ax2 = plt.subplot(122)
bar_width = 0.35
ind = np.arange(len(quarters))

bottom = np.zeros(len(quarters))
for i, allocation in enumerate(quarter_allocations):
    ax2.bar(
        ind, 
        allocation, 
        bar_width, 
        bottom=bottom, 
        color=single_color,  
        edgecolor='black'
    )
    bottom += allocation

ax2.set_xticks(ind)
ax2.set_xticklabels(quarters)
ax2.set_ylabel('Percentage Allocation')

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
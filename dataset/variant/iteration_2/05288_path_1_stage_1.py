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

# Altered budget allocations
allocations = [25, 22, 18, 12, 13, 10]  # Changed from [30, 20, 15, 10, 15, 10]

colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']

plt.figure(figsize=(12, 7))

# Subplot 1: Pie Chart
ax1 = plt.subplot(121)
wedges, texts, autotexts = ax1.pie(
    allocations, 
    labels=sectors, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors,
    shadow=True,
    explode=(0.1, 0, 0, 0, 0, 0),
    wedgeprops={'edgecolor': 'black'}
)

for text in texts:
    text.set_fontsize(11)
    text.set_fontweight('bold')
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(11)

ax1.set_title('Budget Allocation for Fiscal Year 2023\nTech Innovators Inc.', fontsize=14, fontweight='bold', pad=20)

# Subplot 2: Bar Chart
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

# Altered quarterly allocations
quarter_allocations = [
    [6, 6, 5, 3, 3, 2],  # Q1
    [7, 6, 4, 2, 4, 2],  # Q2
    [7, 5, 5, 3, 3, 2],  # Q3
    [5, 5, 4, 4, 4, 2]   # Q4
]
quarter_allocations = np.array(quarter_allocations).T

ax2 = plt.subplot(122)
bar_width = 0.35
ind = np.arange(len(quarters))

bottom = np.zeros(len(quarters))
for i, (sector, allocation) in enumerate(zip(sectors, quarter_allocations)):
    ax2.bar(
        ind, 
        allocation, 
        bar_width, 
        bottom=bottom, 
        label=sector, 
        color=colors[i],
        edgecolor='black'
    )
    bottom += allocation

ax2.set_xticks(ind)
ax2.set_xticklabels(quarters)
ax2.set_ylabel('Percentage Allocation')
ax2.set_title('Quarterly Budget Allocation\nDistribution (in %)', fontsize=12, fontweight='bold')
ax2.legend(title='Sectors', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
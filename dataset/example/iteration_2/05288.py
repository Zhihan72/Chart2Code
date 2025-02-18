import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart represents a breakdown of a fictional company's budget allocation
# across various sectors for the fiscal year 2023. The company, "Tech Innovators Inc.",
# aims to balance its investments in different areas to support sustainable growth.

# Define the sectors and their respective budget allocations
sectors = [
    'Research & Development', 
    'Marketing & Sales', 
    'Operations & Maintenance', 
    'Employee Welfare', 
    'Infrastructure', 
    'Corporate Social Responsibility'
]

# Define the budget allocations as percentages
allocations = [30, 20, 15, 10, 15, 10]  # Explicitly created without using random()

# Define colors for each sector
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']

# Create the pie chart
plt.figure(figsize=(12, 7))

# Creating two subplots
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

# Customizing the text properties for better readability
for text in texts:
    text.set_fontsize(11)
    text.set_fontweight('bold')
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(11)

# Set title and layout adjustments for the pie chart
ax1.set_title('Budget Allocation for Fiscal Year 2023\nTech Innovators Inc.', fontsize=14, fontweight='bold', pad=20)

# Subplot 2: Additional Info using Bar Chart on Quarter Allocation
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
quarter_allocations = [
    [7, 5, 4, 3, 4, 2],  # Q1
    [8, 5, 4, 2, 4, 3],  # Q2
    [7, 5, 4, 2, 4, 3],  # Q3
    [8, 5, 3, 3, 3, 2]   # Q4
]
quarter_allocations = np.array(quarter_allocations).T  # Transpose for proper bar stacking

# Plotting the bar chart
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

# Labeling and providing the title
ax2.set_xticks(ind)
ax2.set_xticklabels(quarters)
ax2.set_ylabel('Percentage Allocation')
ax2.set_title('Quarterly Budget Allocation\nDistribution (in %)', fontsize=12, fontweight='bold')
ax2.legend(title='Sectors', bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust layout to prevent overlap and display the plots
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Display the plot
plt.show()
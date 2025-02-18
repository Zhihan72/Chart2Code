import matplotlib.pyplot as plt
import numpy as np

# Define coffee types
coffee_types = ['Espresso', 'Latte', 'Cappuccino', 'Americano', 'Mocha']

# Sales data for each coffee type over the four quarters in 2023
sales_Q1 = [150, 200, 180, 220, 210]
sales_Q2 = [160, 210, 190, 230, 220]
sales_Q3 = [170, 220, 200, 240, 230]
sales_Q4 = [180, 230, 210, 250, 240]

data = [sales_Q1, sales_Q2, sales_Q3, sales_Q4]

# Create a numpy array for the x locations for the groups
x = np.arange(len(coffee_types))

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(12, 7))

# Define the bar width
width = 0.2

# Plotting for each quarter
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
for i, (sales, color) in enumerate(zip(data, colors)):
    rects = ax.bar(x + i * width, sales, width, label=f'Q{i+1}', color=color)
    # Annotate each bar with its value
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}', xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10, color='black')

# Adding titles and labels
ax.set_title('Coffee Sales Distribution by Type and Quarter in 2023', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Coffee Types', fontsize=12)
ax.set_ylabel('Number of Sales', fontsize=12)
ax.set_xticks(x + width * 1.5)
ax.set_xticklabels(coffee_types, fontsize=11)
ax.legend(title='Quarters', fontsize=10, loc='upper left')

# Customize the grid for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()
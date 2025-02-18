import matplotlib.pyplot as plt
import numpy as np

# Months and expense categories
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
categories = ['Housing', 'Food', 'Transportation', 'Utilities', 'Medical', 'Entertainment']

# Expense data: rows are categories, columns are months
expenses_data = np.array([
    [1200, 1250, 1300, 1280, 1230, 1190, 1220, 1240, 1210, 1260, 1280, 1290],  # Housing
    [500, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620],              # Food
    [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310],              # Transportation
    [100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155],              # Utilities
    [150, 160, 170, 165, 160, 155, 150, 145, 140, 135, 130, 125],              # Medical
    [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210]               # Entertainment
])

# Colors for each category
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Generate the figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Define bar width
bar_width = 0.15

# Create the month index for each category
index = np.arange(len(months))

# Create a grouped bar chart
for i in range(len(categories)):
    ax.bar(index + i * bar_width, expenses_data[i], bar_width, color=colors[i])

# Add title and axis labels
ax.set_xlabel('Months', fontsize=12)
ax.set_ylabel('Expenses (USD)', fontsize=12)

# Add x-ticks for months
ax.set_xticks(index + bar_width * (len(categories) - 1) / 2)
ax.set_xticklabels(months, rotation=45, ha='right')

# Annotate each bar segment with the expense value
for i in range(len(categories)):
    for j in range(len(months)):
        ax.text(index[j] + i * bar_width, expenses_data[i, j] + 10, str(expenses_data[i, j]), ha='center', va='bottom', fontsize=8, fontweight='bold')

# Show the plot
plt.show()
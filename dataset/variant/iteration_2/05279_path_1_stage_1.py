import matplotlib.pyplot as plt
import numpy as np

# Cities and pizzas sold data sorted in descending order of pizzas sold
cities = ['New York', 'Los Angeles', 'Dallas', 'Chicago', 'Philadelphia', 'San Jose', 'San Diego', 'Houston', 'Phoenix', 'San Antonio']
pizzas_sold = [240, 220, 190, 180, 170, 165, 160, 150, 140, 130]

# Data for New York City's pizza types (unchanged)
types = ['Cheese', 'Pepperoni', 'Veggie', 'BBQ Chicken', 'Hawaiian']
type_data_ny = [80, 60, 40, 30, 30]

# Set up the figure and axis
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 14))

# Sorted Bar chart for total pizzas sold in each city
bars1 = ax1.barh(cities, pizzas_sold, color='dodgerblue', edgecolor='black')

# Bar chart for pizza types in New York City
bars2 = ax2.bar(types, type_data_ny, color='orange', edgecolor='black')

# Title and Labels
ax1.set_title('Monthly Pizza Sales Across Major US Cities', fontsize=18, fontweight='bold')
ax1.set_xlabel('Number of Pizzas Sold', fontsize=14, labelpad=10)
ax1.set_ylabel('Cities', fontsize=14, labelpad=10)

ax2.set_title('Pizza Type Sales in New York City', fontsize=18, fontweight='bold')
ax2.set_xlabel('Pizza Type', fontsize=14, labelpad=10)
ax2.set_ylabel('Number of Pizzas Sold', fontsize=14, labelpad=10)

# Grid lines for readability
ax1.grid(axis='x', linestyle='--', alpha=0.7)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate total pizzas sold bars
for bar in bars1:
    width = bar.get_width()
    ax1.text(width + 5, bar.get_y() + bar.get_height() / 2, f'{width}', va='center', ha='left', fontsize=12, fontweight='bold')

# Annotate pizza types bars for New York City
for bar in bars2:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, height + 2, f'{height}', ha='center', va='bottom', fontsize=12, fontweight='bold')

# Customize the layout for better readability
plt.tight_layout(pad=3.0)

# Show the plot
plt.show()
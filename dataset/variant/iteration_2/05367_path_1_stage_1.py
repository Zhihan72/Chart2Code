import matplotlib.pyplot as plt
import squarify

# Corresponding expenses in dollars
expenses = [1200, 300, 500, 150, 200, 100, 50, 100] 

# Normalize the expenses for use in the treemap
total_expenses = sum(expenses)
sizes = [expense / total_expenses * 100 for expense in expenses]

# Define colors for each category
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff6666', '#c2f0c2']

# Create the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, color=colors, alpha=0.8, edgecolor="white", linewidth=2)

# Hide axes
plt.axis('off')

# Display the plot
plt.show()
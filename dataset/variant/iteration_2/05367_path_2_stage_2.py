import matplotlib.pyplot as plt
import squarify

# Corresponding expenses in dollars
expenses = [1200, 300, 500, 150, 100, 50] 

# Normalize the expenses for use in the treemap
total_expenses = sum(expenses)
sizes = [expense / total_expenses * 100 for expense in expenses]

# Define colors for each category
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ffb3e6', '#ff6666']

# Create the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, 
              color=colors, alpha=0.8, edgecolor="white", linewidth=2)

plt.axis('off')  # Hide axes

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()
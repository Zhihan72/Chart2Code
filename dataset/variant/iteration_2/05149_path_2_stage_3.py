import matplotlib.pyplot as plt

# Define energy sources consumption percentages
consumption_percentages = [35, 25, 15, 10, 5]  # Removed one group

# Colors for each energy source
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ffb3e6']  # Adjusted number of colors

# Explode the 'Solar' slice to emphasize it
explode = (0.1, 0, 0, 0, 0)  # Adjusted the explode length

# Create figure and axis for the pie chart
fig, ax = plt.subplots(figsize=(10, 7))

# Create the pie chart
ax.pie(
    consumption_percentages, 
    explode=explode, 
    colors=colors,
    autopct='%1.1f%%', 
    startangle=140,
    shadow=True
)

ax.axis('equal')  
plt.tight_layout()

plt.show()
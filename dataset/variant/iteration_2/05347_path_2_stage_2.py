import matplotlib.pyplot as plt

# Data for the pie chart
popularity = [40, 25, 5, 7, 6, 4, 3, 3, 4, 3]

# Colors for each segment
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff6666', '#b3b3cc', '#ffb366', '#c8e4ff']
explode = (0.05, 0.05, 0, 0, 0, 0, 0, 0, 0, 0) 

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 10))

# Pie chart without labels or text
ax.pie(popularity, explode=explode, colors=colors, startangle=140, wedgeprops=dict(edgecolor='w', linewidth=2))

# Adjust layout
plt.tight_layout()

# Displaying the plot
plt.show()
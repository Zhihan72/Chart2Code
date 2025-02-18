import matplotlib.pyplot as plt

# Data for the donut chart
market_share = [60, 10, 20, 5, 5]

# Define colors for each segment
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create a donut chart
fig, ax = plt.subplots(figsize=(10, 10))
wedges, _ = ax.pie(
    market_share, 
    startangle=140, 
    colors=colors, 
    wedgeprops=dict(width=0.3)
)

# Ensure the chart is drawn as a circle
ax.axis('equal')

# Show the plot
plt.show()
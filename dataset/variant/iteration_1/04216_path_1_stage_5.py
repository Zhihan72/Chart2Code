import matplotlib.pyplot as plt

# Data for the donut chart
market_share = [60, 10, 20, 5, 5]

# Define a single color for all segments
color = ['#66b3ff']  # A chosen color for consistency

# Create a donut chart
fig, ax = plt.subplots(figsize=(10, 10))
wedges, _ = ax.pie(
    market_share, 
    startangle=140, 
    colors=color * len(market_share),  # Apply the single color to all segments
    wedgeprops=dict(width=0.3)
)

# Ensure the chart is drawn as a circle
ax.axis('equal')

# Show the plot
plt.show()
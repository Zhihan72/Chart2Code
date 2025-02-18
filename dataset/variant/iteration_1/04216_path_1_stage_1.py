import matplotlib.pyplot as plt

# Data for the pie chart
market_share = [55, 15, 10, 15, 5]

# Define colors for each console
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create a pie chart
fig, ax = plt.subplots(figsize=(10, 10))

# Create wedges without labels and percentages
wedges, _ = ax.pie(
    market_share, 
    startangle=140, 
    colors=colors, 
    pctdistance=0.85,
    explode=(0.1, 0, 0, 0.1, 0)
)

# Add a circular center to create the "sector" pie chart look
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Ensure the pie is drawn as a circle
ax.axis('equal')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()
import matplotlib.pyplot as plt

# Data for the donut pie chart
popularity = [40, 25, 5, 7, 6, 4, 3, 3, 4, 3]

# Manually shuffled colors for each segment
colors = ['#66b3ff', '#ff9999', '#99ff99', '#c2c2f0', '#ffb3e6', '#ffcc99', '#b3b3cc', '#ffb366', '#c8e4ff', '#ff6666']
explode = (0.05, 0.05, 0, 0, 0, 0, 0, 0, 0, 0)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 10))

# Draw donut pie chart
wedges, texts = ax.pie(popularity, explode=explode, colors=colors, startangle=140, wedgeprops=dict(edgecolor='w', linewidth=2))

# Draw a circle in the center
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.set_aspect('equal')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()
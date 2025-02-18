import matplotlib.pyplot as plt

# Define the data
percentages = [25, 20, 30, 10, 10, 5]

# Colors for the transport modes
colors = ['#ffcc99', '#66b3ff', '#99ff99', '#ff9999', '#c2c2f0', '#ffb3e6']

# Create pie chart
fig, ax = plt.subplots(figsize=(10, 7))

# Creating the pie chart without labels or percent texts
ax.pie(
    percentages,
    startangle=90,
    colors=colors,
    wedgeprops=dict(edgecolor='w')
)

# Draw a circle at the center to turn it into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the pie chart
plt.show()
import matplotlib.pyplot as plt

# Define the data
percentages = [25, 20, 30, 10, 10, 5]

# Manually adjusted colors for the segments
colors = ['#99ff99', '#ffb3e6', '#ffcc99', '#c2c2f0', '#ff9999', '#66b3ff']

# Create pie chart
fig, ax = plt.subplots(figsize=(10, 7))

# Creating the pie chart without any stylistic elements
ax.pie(
    percentages,
    startangle=90,
    colors=colors
)

# Display the pie chart
plt.show()
import matplotlib.pyplot as plt

# Define the data with additional data series
percentages = [25, 20, 30, 10, 10, 5, 15, 35]

# Adjust colors for the new data segments
colors = [
    '#99ff99', '#ffb3e6', '#ffcc99', '#c2c2f0',
    '#ff9999', '#66b3ff', '#ff6666', '#b3b3cc'
]

# Create pie chart
fig, ax = plt.subplots(figsize=(10, 7))

ax.pie(
    percentages,
    startangle=90,
    colors=colors
)

plt.show()
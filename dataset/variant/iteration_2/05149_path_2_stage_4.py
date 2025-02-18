import matplotlib.pyplot as plt

# Define energy sources consumption percentages
consumption_percentages = [35, 25, 15, 10, 5]

# Use a single color for all slices
single_color = ['#66b3ff'] * len(consumption_percentages)

# Explode the 'Solar' slice to emphasize it
explode = (0.1, 0, 0, 0, 0)

# Create figure and axis for the pie chart
fig, ax = plt.subplots(figsize=(10, 7))

# Create the pie chart
ax.pie(
    consumption_percentages, 
    explode=explode,
    colors=single_color,
    autopct='%1.1f%%', 
    startangle=140,
    shadow=True
)

ax.axis('equal')
plt.tight_layout()

plt.show()
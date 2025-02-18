import matplotlib.pyplot as plt

# Define data
civilizations = ['Egyptians', 'Mesopotamians', 'Greeks', 'Romans', 'Mayans']
wonders_count = [15, 8, 12, 20, 5]

# Define colors
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Explode the slice for better emphasis (e.g., Romans)
explode = (0, 0.1, 0, 0.1, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(
    wonders_count,
    colors=colors,
    explode=explode,
    autopct='%1.1f%%',
    startangle=140
)

# Display the plot
plt.show()
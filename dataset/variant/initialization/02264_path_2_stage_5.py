import matplotlib.pyplot as plt

# Original data series
percentages = [25, 20, 15, 18, 12, 10]

# Additional made-up data series
additional_percentages = [5, 8, 9]

# Combine the original percentages with the additional made-up data
all_percentages = percentages + additional_percentages

# Generate colors for the added data
single_color = ['#66c2a5' for _ in range(len(all_percentages))]

# Adjust the explode to incorporate the additional segments
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0)

# Plot updated pie chart
fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(
    all_percentages,
    labels=None,
    autopct=None,
    startangle=90,
    colors=single_color,
    explode=explode
)

ax.axis('equal')
plt.show()
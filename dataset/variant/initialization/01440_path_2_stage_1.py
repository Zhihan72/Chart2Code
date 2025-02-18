import matplotlib.pyplot as plt

# Define the data for the architectural styles
styles = [
    'Modern', 'Classical', 'Art Deco', 'Gothic', 'Futuristic',
    'Baroque', 'Renaissance', 'Neoclassical', 'Minimalist', 'Brutalism', 'Romanesque'
]
# Manually altered percentages while maintaining the sum at 100
percentages = [22.0, 14.0, 10.0, 9.0, 8.0, 5.5, 6.0, 5.0, 6.0, 7.5, 7.0]

# Adjust last percentage to ensure the total sums to 100
total = sum(percentages)
correction = 100 - total
percentages[-1] += correction

# Verify percentages sum to 100, allowing for minor floating-point margin
assert abs(sum(percentages) - 100) < 1e-9, "Percentages must sum up to 100."

# Define colors using a color map
colors = plt.cm.viridis([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.15, 0.25])

# Set explode to highlight significant categories
explode = tuple(0.1 if p >= 10 else 0 for p in percentages)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 10))
wedges, texts, autotexts = ax.pie(
    percentages,
    labels=styles,
    autopct=lambda pct: f'{pct:.1f}%\n({pct / 100 * 1000:.0f}/1000)',
    startangle=140,
    colors=colors,
    explode=explode
)

# Style the text
plt.setp(autotexts, size=10, weight='bold', color='white')
plt.setp(texts, size=10)

# Add a title
ax.set_title(
    'Architectural Styles Distribution in Architectura City\n'
    'Breakdown of New Developments in the 2020s\n'
    'Data as Percentage and Fractional Representation',
    fontsize=14,
    fontweight='bold'
)

# Add a legend
ax.legend(
    wedges,
    styles,
    title='Styles',
    loc='upper left',
    bbox_to_anchor=(1, 1)
)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()
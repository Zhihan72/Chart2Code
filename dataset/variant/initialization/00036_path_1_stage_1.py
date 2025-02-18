import matplotlib.pyplot as plt
import numpy as np

# Categories and corresponding energy contribution values
activities = [
    'Heating & Cooling', 'Water Heating', 'Lighting', 'Appliances', 'Electronics',
    'Other', 'Renewable Energy', 'Insulation', 'Cooking', 'Refrigerators', 'Washing Machines'
]

# Define energy consumption contributions; positive and negative changes from base, as example
contributions = np.array([5, -4, 3, -1, 2, -0.5, 1, -2, 0.5, -0.3, 0.2])

# Color palette including negative and positive variations
colors = [
    '#ff9999', '#ffcc99', '#99ff99', '#ffb3e6', '#66b3ff',
    '#ff6666', '#66ffb3', '#c2c2f0', '#b3b3cc', '#99ccff', '#ffcccb'
]

# Initialize the figure and axis for a diverging bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Centerline for the diverging bars
ax.axvline(x=0, color='gray', linewidth=0.8)

# Create the diverging horizontal bar chart
bars = ax.barh(activities, contributions, color=colors)

# Add percentage labels for each bar segment
for bar, contribution in zip(bars, contributions):
    label_position = bar.get_width() - 0.5 if contribution > 0 else bar.get_width() + 0.5
    ax.text(label_position, bar.get_y() + bar.get_height()/2, f'{contribution:.1f}', 
            va='center', ha='center', color='black', fontsize=9)

# Set title and labels
ax.set_title('Diverging Bar Chart: Impact on Energy Consumption', fontsize=16, pad=20)
ax.set_xlabel('Contribution to Total Energy Consumption', fontsize=12)

# Adjust the limits to ensure all bars are centered and visible
ax.set_xlim(-10, 10)

# Improve layout spacing
plt.tight_layout()

plt.show()
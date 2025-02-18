import matplotlib.pyplot as plt
import numpy as np

# Define the backstory:
# This chart displays the productivity of different types of fruits grown in various regions over the year.
# The comparison is between the production quantities in kilograms for Apples, Oranges, and Grapes.

# Define regions and production quantities in kilograms for the year 2023.
regions = ['Region A', 'Region B', 'Region C', 'Region D', 'Region E']
apples = [1200, 850, 1250, 950, 1100]
oranges = [900, 1200, 820, 950, 1020]
grapes = [880, 950, 1100, 1200, 980]

# Calculate total production for each region
total_production = np.array(apples) + np.array(oranges) + np.array(grapes)

# Create the bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Set the width of the bars
bar_width = 0.6

# Plot bars
ax.bar(regions, apples, label='Apples', color='#FF6347', width=bar_width)
ax.bar(regions, oranges, bottom=apples, label='Oranges', color='#FFA500', width=bar_width)
ax.bar(regions, grapes, bottom=np.array(apples) + np.array(oranges), label='Grapes', color='#9370DB', width=bar_width)

# Titles and labels
ax.set_title("Fruit Production by Region in 2023\nComparison between Apples, Oranges, and Grapes", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Regions", fontsize=12)
ax.set_ylabel("Production in Kilograms (kg)", fontsize=12)
ax.set_ylim(0, max(total_production) + 300)  # Adding some padding above the top bar

# Create a legend
ax.legend(title="Type of Fruit", loc='upper right')

# Add grid lines for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate text on top of the bars
for idx, (region, total) in enumerate(zip(regions, total_production)):
    ax.text(idx, total + 50, f"{total} kg", ha='center', va='bottom', fontsize=10, fontweight='bold')

# Rotate the region names to avoid overlap
plt.xticks(rotation=45, ha='right')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()
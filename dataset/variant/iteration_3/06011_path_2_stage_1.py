import matplotlib.pyplot as plt
import numpy as np

# Define regions and production quantities in kilograms for the year 2023.
regions = ['Region B', 'Region D', 'Region E', 'Region A', 'Region C']
apples = [850, 950, 1100, 1200, 1250]
oranges = [1200, 950, 1020, 900, 820]
grapes = [950, 1200, 980, 880, 1100]

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
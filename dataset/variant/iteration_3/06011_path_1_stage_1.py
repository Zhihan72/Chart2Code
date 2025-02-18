import matplotlib.pyplot as plt
import numpy as np

# Define regions and production quantities in kilograms for the year 2023.
regions = ['Region A', 'Region B', 'Region C', 'Region D', 'Region E']
apples = [1200, 850, 1250, 950, 1100]
oranges = [900, 1200, 820, 950, 1020]
grapes = [880, 950, 1100, 1200, 980]

# Calculate total production for each region
total_production = np.array(apples) + np.array(oranges) + np.array(grapes)

# Create the horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plot horizontal bars
ax.barh(regions, apples, label='Apples', color='#FF6347')
ax.barh(regions, oranges, left=apples, label='Oranges', color='#FFA500')
ax.barh(regions, grapes, left=np.array(apples) + np.array(oranges), label='Grapes', color='#9370DB')

# Titles and labels
ax.set_title("Fruit Production by Region in 2023\nComparison between Apples, Oranges, and Grapes", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Production in Kilograms (kg)", fontsize=12)
ax.set_ylabel("Regions", fontsize=12)
ax.set_xlim(0, max(total_production) + 300)

# Create a legend
ax.legend(title="Type of Fruit", loc='upper right')

# Add grid lines for better readability
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Annotate text on the bars
for idx, (region, total) in enumerate(zip(regions, total_production)):
    ax.text(total + 50, idx, f"{total} kg", va='center', ha='left', fontsize=10, fontweight='bold')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()
import matplotlib.pyplot as plt

# Data for monthly water consumption (liters) for different types of households
small_families = [150, 160, 170, 155, 165, 180, 175, 160, 170, 165, 175, 190]
large_families = [300, 310, 320, 305, 315, 350, 345, 310, 330, 325, 340, 360]
single_adults = [100, 110, 115, 105, 120, 125, 110, 120, 115, 125, 130, 135]
student_households = [200, 210, 220, 205, 215, 230, 220, 210, 220, 215, 230, 240]
elderly_couples = [80, 85, 90, 82, 88, 95, 92, 85, 90, 88, 92, 97]

# Combine data into a list
water_usage_data = [small_families, large_families, single_adults, student_households, elderly_couples]

household_types = ['Small Families', 'Large Families', 'Single Adults', 'Student Households', 'Elderly Couples']

# Create the horizontal box plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the data horizontally
box = ax.boxplot(water_usage_data, vert=False, patch_artist=True, labels=household_types, notch=True, whis=[5, 95])

# Define colors for each household type
colors = ['lightcoral', 'lightblue', 'lightgreen', 'plum', 'khaki']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customize plot appearance
for whisker, cap, median, flier in zip(box['whiskers'], box['caps'], box['medians'], box['fliers']):
    whisker.set(color='grey', linewidth=1.5, linestyle='--')
    cap.set(color='grey', linewidth=1.5)
    median.set(color='darkred', linewidth=2)
    flier.set(marker='o', color='gold', alpha=0.5)

# Set titles and labels
ax.set_title('Monthly Water Consumption:\nComparison Across Different Types of Households', fontsize=16, fontweight='bold')
ax.set_xlabel('Water Consumption (Liters)', fontsize=12)
ax.set_ylabel('Household Type', fontsize=12)
ax.xaxis.grid(True, linestyle='--', color='grey', alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()
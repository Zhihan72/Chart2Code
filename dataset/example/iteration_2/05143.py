import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# A small-town farmer decided to experiment with different crop yields over the span of five years to figure out which crops produce the best yield in his fields. This chart displays the results of his experiment.

# Define the years and crop-specific yields
years = np.arange(2015, 2020)
crops = ['Wheat', 'Corn', 'Barley', 'Soybeans']

# Yield data for each crop (in tons per hectare)
wheat_yield = [3.5, 3.7, 3.9, 4.1, 4.0]      # Wheat
corn_yield = [7.0, 7.3, 7.8, 8.0, 7.9]        # Corn
barley_yield = [2.5, 2.7, 2.8, 3.0, 3.1]     # Barley
soybean_yield = [2.0, 2.1, 2.2, 2.3, 2.4]    # Soybeans

# Colors for the stacked bars
colors = ['#FFD700', '#ADFF2F', '#20B2AA', '#FF6347']

# Create stacked bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting each layer of the stack
ax.bar(years, wheat_yield, label='Wheat', color=colors[0])
ax.bar(years, corn_yield, bottom=wheat_yield, label='Corn', color=colors[1])
ax.bar(years, barley_yield, bottom=np.array(wheat_yield) + np.array(corn_yield), label='Barley', color=colors[2])
ax.bar(years, soybean_yield, bottom=np.array(wheat_yield) + np.array(corn_yield) + np.array(barley_yield), label='Soybeans', color=colors[3])

# Title and Axis Labels
ax.set_title("Crop Yield Experimentation Results\n(2015-2019)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Yield (tons per hectare)", fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(years, rotation=45)

# Configure legend and position
ax.legend(title='Crops', loc='upper left', bbox_to_anchor=(1, 1))

# Add grid lines for easier reading
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Add annotations to each bar
for i in range(len(years)):
    height_sum = 0
    for yield_name in [wheat_yield, corn_yield, barley_yield, soybean_yield]:
        # Calculate cumulative height up to the current segment
        height_sum += yield_name[i]
        ax.text(years[i], height_sum - yield_name[i]/2, f'{yield_name[i]}', ha='center', va='center', color='black', fontsize=10)

# Adjust layout to prevent clipping of labels and titles
plt.tight_layout()

# Display the plot
plt.show()
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Data and backstory: The funnel represents the consumer journey in a newly launched eco-friendly electric vehicle (EV) company.
steps = [
    "Initial Inquiry",
    "Test Drive Scheduled",
    "Test Drive Completed",
    "Price Negotiation",
    "Financing Options",
    "Purchase Agreement Signed",
    "Vehicle Delivered",
    "Ownership Beyond 6 Months"
]

# Number of consumers at each stage (explicitly constructed data)
consumer_counts = np.array([5000, 3800, 3500, 2900, 2600, 2200, 2000, 1700])

# Calculate conversion rates
conversion_rates = 100 * (consumer_counts[1:] / consumer_counts[:-1])

# Normalize widths for funnel-like appearance
widths = consumer_counts / consumer_counts[0]

# Define colors for each step
colors = ['#91bfdb', '#4575b4', '#91bfdb', '#74add1', '#abd9e9', '#e0f3f8', '#fee090', '#fc8d59']

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 10))

# Add trapezoids for each stage of the funnel
for i in range(len(steps)):
    top_width = widths[i-1] if i > 0 else 1.0
    bottom_width = widths[i]
    
    trapezoid = patches.Polygon(
        [
            [(1 - top_width) / 2, i], [(1 + top_width) / 2, i], 
            [(1 + bottom_width) / 2, i + 1], [(1 - bottom_width) / 2, i + 1]
        ], closed=True, color=colors[i], edgecolor='black'
    )
    ax.add_patch(trapezoid)
    
    # Center text within each trapezoid
    ax.text(0.5, i + 0.5, f"{steps[i]}\n{consumer_counts[i]} Consumers",
            ha='center', va='center', fontsize=11, color='black', weight='bold')

    # Add conversion rate annotation if applicable
    if i > 0:
        ax.text(0.95, i + 0.5, f"Conversion: {conversion_rates[i-1]:.1f}%", 
                ha='right', va='center', fontsize=10, color='green', weight='bold')

# Customize the plot
ax.set_xlim(0, 1)
ax.set_ylim(0, len(steps))
ax.axis('off')  # Remove axes for a cleaner look

# Title and Subtitle
ax.set_title('Consumer Journey in Eco-friendly EV Company:\nConversion Funnel',
             fontsize=16, weight='bold', ha='center', va='bottom', pad=30)

# Ensure tight layout
plt.tight_layout()

# Display the plot
plt.show()
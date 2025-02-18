import matplotlib.pyplot as plt
import numpy as np

# Define the international cuisines and their respective popularity scores
cuisines = ["Italian", "Japanese", "Mexican", "Indian", "Chinese", "Thai", "French", "Greek", "Spanish", "Middle Eastern"]
popularity_scores = np.array([85, 75, 70, 65, 60, 55, 50, 45, 40, 35])

# Colors for the bars, using a warm color palette
colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300', '#DAF7A6', '#FFC0CB', '#FF6F61', '#92A8D1', '#B833FF']

# Create the vertical bar chart
fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.bar(cuisines, popularity_scores, color=colors, edgecolor='black')

# Set the title and labels
ax.set_title('Culinary Adventures:\nPopularity of International Cuisines Among City Residents', fontsize=16, fontweight='bold', ha='center')
ax.set_ylabel('Popularity Score (out of 100)', fontsize=14)
ax.set_xlabel('Cuisines', fontsize=14)

# Add data labels to each bar
for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 5, f'{bar.get_height()}', 
            ha='center', va='top', color='white', fontsize=10, fontweight='bold')

# Add horizontal grid lines
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Set y-axis limit to provide appropriate spacing
ax.set_ylim(0, 100)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Define the international cuisines and their respective altered popularity scores
cuisines = ["Italian", "Japanese", "Mexican", "Indian", "Chinese", "Thai", "French", "Greek", "Spanish", "Middle Eastern"]
popularity_scores = np.array([70, 85, 60, 55, 75, 40, 45, 35, 65, 50])

# Colors for the bars, shuffled within the existing palette
colors = ['#C70039', '#FF5733', '#FFC300', '#581845', '#92A8D1', '#900C3F', '#DAF7A6', '#B833FF', '#FFC0CB', '#FF6F61']

# Create the vertical bar chart
fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.bar(cuisines, popularity_scores, color=colors, edgecolor='black')

# Title and labels
ax.set_title('Culinary Adventures:\nPopularity of International Cuisines Among City Residents', fontsize=16, fontweight='bold', ha='center')
ax.set_ylabel('Popularity Score (out of 100)', fontsize=14)
ax.set_xlabel('Cuisines', fontsize=14)

# Data labels on bars
for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 5, f'{bar.get_height()}', 
            ha='center', va='top', color='white', fontsize=10, fontweight='bold')

# Grid lines
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Limits for y-axis
ax.set_ylim(0, 100)

# Layout adjustment
plt.tight_layout()

# Show plot
plt.show()
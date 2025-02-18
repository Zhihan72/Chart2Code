import matplotlib.pyplot as plt
import numpy as np

# Culinary techniques and their popularity scores
culinary_techniques = [
    "Smoking",     # Swapped position 2 with 0
    "Fermentation", 
    "Sous Vide",
    "Pickling",    # Swapped position 3 with 1
    "Braising",
    "Sautéing",
    "Grilling",
    "Poaching",
    "Roasting",    # Swapped position 9 with 4
    "Steaming"     # Swapped position 8 with 7
]

# Popularity scores in percentage (shuffle a few values)
popularity_scores = [20, 25, 15, 18, 45, 40, 50, 30, 17, 35]

# Assigning colors for each bar (shuffled to match new culinary order)
colors = ['#41b6c4', '#7fcdbb', '#c7e9b4', '#1d91c0', '#fc8d59', 
          '#253494', '#081d58', '#b30000', '#225ea8', '#e34a33']

# Plotting the horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))
y_pos = np.arange(len(culinary_techniques))

# Create horizontal bars
ax.barh(y_pos, popularity_scores, color=colors, edgecolor='black', alpha=0.8)

# Set y-ticks with the culinary techniques
ax.set_yticks(y_pos)
ax.set_yticklabels(culinary_techniques, fontsize=10, fontweight='medium')
ax.invert_yaxis()  # Highest score on top

# Titles and labels with minor changes
ax.set_title('Varied Taste Trends in Gastronomy\nChef Preferences Globally', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Score of Popularity (%)', fontsize=12)
ax.set_ylabel('Methodologies', fontsize=12)

# Annotate each bar with the popularity score
for i in range(len(popularity_scores)):
    ax.text(popularity_scores[i] + 1, i, f'{popularity_scores[i]}%', 
            va='center', color='black', fontsize=10)

# Add grid lines for x-axis
ax.grid(axis='x', linestyle='--', alpha=0.6)

# Ensure layout is tight
plt.tight_layout()

# Display the plot
plt.show()
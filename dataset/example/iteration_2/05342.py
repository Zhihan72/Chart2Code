import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# In 2023, a global organization conducted a survey about the popular hobbies people picked up during quarantine. 
# They categorized the responses into several types of hobbies and measured the percentage of people who adopted them.

# Categories and percentages of people who picked up new hobbies during quarantine
hobbies = [
    "Cooking/Baking", 
    "Reading", 
    "Gardening", 
    "DIY Projects", 
    "Exercise", 
    "Gaming", 
    "Music", 
    "Crafting", 
    "Photography", 
    "Writing"
]

# Corresponding percentages
percentages = [35, 30, 25, 20, 45, 40, 15, 10, 5, 8]

# Colors to distinguish hobby categories
colors = plt.cm.Paired(np.linspace(0, 1, len(hobbies)))

# Create a vertical bar chart
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the bars
bars = ax.bar(hobbies, percentages, color=colors, edgecolor='black')

# Add percentage labels on top of each bar
ax.bar_label(bars, fmt='%.0f%%', padding=5, fontsize=10)

# Title, labels, and axis limits
ax.set_title("Popular Hobbies During Quarantine in 2023",
             fontsize=18, fontweight='bold', pad=15)
ax.set_ylabel("Percentage (%)", fontsize=14)
ax.set_ylim(0, 50)
ax.set_xticklabels(hobbies, rotation=45, ha='right', fontsize=12)

# Customize x-tick labels for aesthetic spacing and clarity
ax.set_xticks(range(len(hobbies)))

# Adding horizontal grid lines for easier reading
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Highlight the top 3 most popular hobbies with additional annotations
annotations = [
    ("Exercise was the most popular", 45),
    ("Cooking/Baking saw a surge", 35),
    ("Gaming became a major outlet", 40)
]

for annotation, value in annotations:
    hobby_index = percentages.index(value)
    ax.annotate(annotation, xy=(hobby_index, value), 
                xytext=(hobby_index, value + 5),
                arrowprops=dict(arrowstyle="->", color='black'),
                fontsize=10, color='black')

# Automatically adjust layout to ensure no overlap of elements
plt.tight_layout()

# Display the plot
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Backstory: This chart visualizes the data on various fruits' vitamin content per 100 grams and their average consumer rating. 
# The bars represent the vitamin content (in mg), and a line chart overlays the bars to provide the average rating (out of 10) for each fruit.

# Data
fruits = ["Apple", "Banana", "Orange", "Blueberry", "Strawberry", "Grapes", "Kiwi", "Watermelon"]
vitamin_content = [6, 10, 70, 9, 32, 10, 92, 8]  # Vitamin C content (in mg per 100g)
avg_rating = [7.5, 8.0, 9.0, 8.5, 9.5, 7.0, 8.5, 7.0]  # Average rating (out of 10)

fig, ax1 = plt.subplots(figsize=(14, 8))

# Plotting the bars for vitamin content
bars = ax1.bar(fruits, vitamin_content, color="limegreen", edgecolor='black', linewidth=0.8)

# Adding labels above each bar
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 2, f'{yval} mg', ha='center', va='bottom', color='black', fontsize=10, weight='bold')

ax1.set_xlabel('Fruits', fontsize=13)
ax1.set_ylabel('Vitamin C Content (mg per 100g)', fontsize=13)
ax1.set_title('Vitamin C Content and Consumer Ratings of Different Fruits', fontsize=15, fontweight='bold', pad=20)
ax1.grid(True, linestyle='--', alpha=0.7)

# Plotting the line chart for average ratings
ax2 = ax1.twinx()
ax2.plot(fruits, avg_rating, color="blue", marker='o', linestyle='-', linewidth=2.5, markersize=10, label='Average Rating (out of 10)')

# Adding ratings labels
for i, rating in enumerate(avg_rating):
    ax2.text(i, rating + 0.2, f'{rating}', ha='center', va='bottom', color='blue', fontsize=10)

ax2.set_ylabel('Average Rating (out of 10)', fontsize=13, color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

# Adding legends
lines_labels = [ax2.get_lines()[0]]
labels = [line.get_label() for line in lines_labels]
ax2.legend(lines_labels, labels, loc='upper left', bbox_to_anchor=(0.1, 0.9), fontsize=12)

# Adjust layout to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()
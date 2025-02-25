import matplotlib.pyplot as plt
import numpy as np

# Data
fruits = ["Apple", "Banana", "Orange", "Blueberry", "Strawberry", "Grapes", "Kiwi", "Watermelon"]
vitamin_content = [6, 10, 70, 9, 32, 10, 92, 8]
avg_rating = [7.5, 8.0, 9.0, 8.5, 9.5, 7.0, 8.5, 7.0]

fig, ax1 = plt.subplots(figsize=(14, 8))

# Plotting the bars with modified style
bars = ax1.bar(fruits, vitamin_content, color="orange", edgecolor='gray', linewidth=1.5)

# Labels above each bar
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 2, f'{yval} mg', ha='center', va='bottom', color='darkred', fontsize=11, weight='normal')

ax1.set_xlabel('Fruits', fontsize=14)
ax1.set_ylabel('Vitamin C Content (mg per 100g)', fontsize=14)
ax1.set_title('Vitamin C Content and Consumer Ratings of Different Fruits', fontsize=16, fontweight='bold', pad=20)

# Modified grid style
ax1.grid(True, linestyle='-.', color='grey', alpha=0.5)

# Plotting the line chart with modified markers
ax2 = ax1.twinx()
ax2.plot(fruits, avg_rating, color="purple", marker='s', linestyle='--', linewidth=3, markersize=8, label='Average Rating (out of 10)')

# Labels for ratings
for i, rating in enumerate(avg_rating):
    ax2.text(i, rating + 0.2, f'{rating}', ha='center', va='bottom', color='purple', fontsize=10)

ax2.set_ylabel('Average Rating (out of 10)', fontsize=14, color='purple')
ax2.tick_params(axis='y', labelcolor='purple')

# Modified legend
ax2.legend(loc='lower right', fontsize=12)

# Adjust layout 
plt.tight_layout()

# Display the plot
plt.show()
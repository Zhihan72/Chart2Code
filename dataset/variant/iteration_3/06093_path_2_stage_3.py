import matplotlib.pyplot as plt
import numpy as np

# Stages and data
stages = ["Awareness", "Consideration", "Subscription", "Retention"]
user_counts = [20000, 15000, 6000, 2500]
average_ratings = [3.5, 4.0, 4.5, 4.8]
colors = ['#ff9999', '#66b3ff', '#ffcc99', '#c2c2f0']

# Create figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
fig.suptitle('Customer Acquisition Journey for a New Fitness App in 2023', fontsize=18, fontweight='bold')
plt.subplots_adjust(wspace=0.4)

# Horizontal Bar Chart for User Counts
ax1.barh(stages, user_counts, color=colors, edgecolor='black', linestyle='-.', linewidth=1.5)
ax1.set_xlim(0, max(user_counts) + 2000)
ax1.set_xlabel('User Count', fontsize=12)
ax1.set_yticks(range(len(stages)))
ax1.set_yticklabels(stages, fontsize=10, fontweight='bold')
ax1.set_title('User Counts at Each Stage', fontsize=14, fontweight='bold')
ax1.grid(True, linestyle='--', alpha=0.7)
for i, count in enumerate(user_counts):
    ax1.text(count + 500, i, f'{count}', va='center', fontsize=10, fontweight='bold')

# Horizontal Bar Chart for Average Ratings
ax2.barh(stages, average_ratings, color=colors, edgecolor='black', linestyle=':', linewidth=2)
ax2.set_xlim(0, 5)
ax2.set_xlabel('Average Rating (out of 5)', fontsize=12)
ax2.set_yticks(range(len(stages)))
ax2.set_yticklabels(stages, fontsize=10, fontweight='bold')
ax2.set_title('Average Ratings at Each Stage', fontsize=14, fontweight='bold')
ax2.grid(True, linestyle='--', alpha=0.5)
for i, v in enumerate(average_ratings):
    ax2.text(v + 0.1, i, f"{v:.1f}", va='center', fontsize=10, fontweight='bold')

# Add custom legend to explain color coding
ax2.legend(['Stage Ratings'], loc='lower right', fontsize=10)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
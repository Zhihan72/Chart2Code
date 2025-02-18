import matplotlib.pyplot as plt
import numpy as np

# Funnel stages and user data
stages = ["Awareness", "Consideration", "Trial", "Subscription", "Retention"]
user_counts = [20000, 15000, 10000, 6000, 2500]
average_ratings = [3.5, 4.0, 4.2, 4.5, 4.8]

# Colors for the stages
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
plt.subplots_adjust(wspace=0.4)

# Horizontal Bar Chart for User Counts
ax1.barh(stages, user_counts, color=colors)
ax1.set_xlabel('User Counts', fontsize=12)
ax1.set_xlim(0, max(user_counts) + 2000)
for i, count in enumerate(user_counts):
    ax1.text(count + 500, i, f'{count}', va='center', fontsize=10)

# Horizontal Bar Chart for Average Ratings
ax2.barh(stages, average_ratings, color=colors)
ax2.set_xlabel('Average Rating (out of 5)', fontsize=12)
ax2.set_xlim(0, 5)
for i, rating in enumerate(average_ratings):
    ax2.text(rating + 0.1, i, f"{rating:.1f}", va='center', fontsize=10)

plt.show()
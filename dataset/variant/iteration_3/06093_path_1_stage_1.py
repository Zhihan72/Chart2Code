import matplotlib.pyplot as plt
import matplotlib.patches as patches
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

# Funnel Plot
ax1.set_xlim(0, max(user_counts) + 2000)
ax1.set_ylim(0, len(stages))
for i in range(len(stages) - 1):
    left = (max(user_counts) - user_counts[i]) / 2
    width_top = user_counts[i]
    width_bottom = user_counts[i + 1]
    trapezoid = patches.Polygon(
        [
            (left, i),
            (left + width_top, i),
            (left + (width_top + width_bottom) / 2, i + 1),
            (left + (width_top - width_bottom) / 2, i + 1)
        ],
        closed=True, color=colors[i]
    )
    ax1.add_patch(trapezoid)
left = (max(user_counts) - user_counts[-1]) / 2
rectangle = patches.Rectangle(
    (left, len(stages) - 1), user_counts[-1], 1, color=colors[-1]
)
ax1.add_patch(rectangle)
for i, (stage, count) in enumerate(zip(stages, user_counts)):
    ax1.text(max(user_counts) / 2, i + 0.5, f'{stage}: {count}', va='center', ha='center',
             color='black', fontsize=12)
ax1.set_xticks([])
ax1.set_yticks([])
for spine in ax1.spines.values():
    spine.set_visible(False)

# Bar Chart for Average Ratings
ax2.barh(stages, average_ratings, color=colors)
ax2.set_xlim(0, 5)
ax2.set_xlabel('Average Rating (out of 5)', fontsize=12)
ax2.set_yticks(range(len(stages)))
ax2.set_yticklabels(stages, fontsize=10)
for i, v in enumerate(average_ratings):
    ax2.text(v + 0.1, i, f"{v:.1f}", va='center', fontsize=10)

plt.show()
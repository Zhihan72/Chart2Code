import matplotlib.pyplot as plt
import numpy as np

# Data for each household (in dollars)
household_a_spending = [500, 450, 400, 150, 200, 450, 320, 100, 350, 420, 280, 370]
household_b_spending = [520, 460, 390, 160, 210, 460, 310, 90, 340, 430, 270, 365]
household_c_spending = [495, 445, 395, 145, 195, 455, 325, 95, 345, 415, 275, 360]
household_d_spending = [480, 470, 410, 155, 205, 445, 330, 105, 360, 425, 285, 375]

# Aggregate data for box plot
aggregate_spending = [household_a_spending, household_b_spending, household_c_spending, household_d_spending]

# Create a horizontal box plot
fig, ax = plt.subplots(figsize=(12, 8))
box = ax.boxplot(aggregate_spending, vert=False, patch_artist=True, 
                 labels=['Household A', 'Household B', 'Household C', 'Household D'], 
                 notch=False, whis=2.0)

# Custom colors for each box
colors = ['#FF69B4', '#8A2BE2', '#5F9EA0', '#F4A460']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Set title and labels
ax.set_title('Monthly Spending Analysis Across Four Households', fontsize=15, fontweight='normal')
ax.set_xlabel('Spending Amount (in Dollars)', fontsize=11)
ax.set_ylabel('Households', fontsize=11)
ax.grid(axis='y', linestyle='-.', alpha=0.5)

# Customize whiskers and caps
for whisker, cap in zip(box['whiskers'], box['caps']):
    whisker.set(color='darkred', linewidth=1)
    cap.set(color='darkred', linewidth=1)

# Customize medians
for median in box['medians']:
    median.set(color='green', linewidth=2.5)

# Updated data for category spending for Household A
food_spending_a = [500, 520, 495, 480]
utilities_spending_a = [450, 460, 445, 470]
entertainment_spending_a = [400, 390, 395, 410]
healthcare_spending_a = [150, 160, 145, 155]
data_category_a = [food_spending_a, utilities_spending_a, entertainment_spending_a, healthcare_spending_a]

# Create a second subplot for category spending of Household A
fig, ax2 = plt.subplots(figsize=(12, 6))
ax2.boxplot(data_category_a, vert=False, patch_artist=True, 
            labels=['Food', 'Utilities', 'Entertainment', 'Healthcare'], notch=False, widths=0.4)

# Custom colors for each category
category_colors = ['#DA70D6', '#32CD32', '#FFD700', '#4682B4']
boxes = ax2.patches
for patch, color in zip(boxes, category_colors):
    patch.set_facecolor(color)

# Title and labels
ax2.set_title('Category Spending Analysis for Selected Items', fontsize=15, fontweight='normal', color='purple')
ax2.set_xlabel('Spending Amount (in Dollars)', fontsize=11)
ax2.set_ylabel('Spending Categories', fontsize=11)
ax2.grid(axis='y', linestyle='-.', alpha=0.5)

plt.tight_layout()
plt.show()
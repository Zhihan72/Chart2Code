import matplotlib.pyplot as plt
import numpy as np

# Data for each household
household_a_spending = [500, 450, 400, 150, 200, 450, 320, 100, 350, 420, 280, 370]
household_b_spending = [520, 460, 390, 160, 210, 460, 310, 90, 340, 430, 270, 365]
household_c_spending = [495, 445, 395, 145, 195, 455, 325, 95, 345, 415, 275, 360]

# Aggregate data for box plot
spending_data = [household_a_spending, household_b_spending, household_c_spending]

# Combine category spending data for box plot
food_spending = [500, 520, 495]
utilities_spending = [450, 460, 445]
entertainment_spending = [400, 390, 395]
healthcare_spending = [150, 160, 145]
aggregate_spending = [household_a_spending, household_b_spending, household_c_spending]

# Create a horizontal box plot
fig, ax = plt.subplots(figsize=(12, 8))
box = ax.boxplot(aggregate_spending, vert=False, patch_artist=True, 
                 labels=['Family One', 'Group B', 'C Household'], 
                 notch=True, whis=1.5)

# Set custom colors for each box
colors = ['#87CEEB', '#FFA07A', '#98FB98']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Set title and labels
ax.set_title('Spending Comparison Across Families', fontsize=16, fontweight='bold')
ax.set_xlabel('Amount Spent (USD)', fontsize=12)
ax.set_ylabel('Different Homes', fontsize=12)

# Add grid for better readability
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Customize whiskers and caps
for whisker, cap in zip(box['whiskers'], box['caps']):
    whisker.set(color='gray', linewidth=1.5)
    cap.set(color='gray', linewidth=1.5)

# Customize medians
for median in box['medians']:
    median.set(color='blue', linewidth=2)

# Create a second subplot for category spending of Household A
fig, ax2 = plt.subplots(figsize=(12, 6))
data_category = [food_spending, utilities_spending, entertainment_spending, healthcare_spending]
ax2.boxplot(data_category, vert=False, patch_artist=True, 
            labels=['Groceries', 'Essentials', 'Fun', 'Health'], notch=True, widths=0.5)

# Customize the colors for each category
category_colors = ['#FF6347', '#FFD700', '#4682B4', '#ADFF2F']
boxes = ax2.patches
for patch, color in zip(boxes, category_colors):
    patch.set_facecolor(color)

# Set the y-ticks and labels
ax2.set_yticks(np.arange(1, len(data_category) + 1))
ax2.set_yticklabels(['Groceries', 'Essentials', 'Fun', 'Health'])

# Title and labels
ax2.set_title('Spending in Departments of Family A', fontsize=16, fontweight='bold', color='navy')
ax2.set_xlabel('Amount in USD', fontsize=12)
ax2.set_ylabel('Categories', fontsize=12)

# Add grid for better readability
ax2.grid(axis='x', linestyle='--', alpha=0.7)

# Avoid overlapping and ensure the layout is tight
plt.tight_layout()

# Display the plot
plt.show()
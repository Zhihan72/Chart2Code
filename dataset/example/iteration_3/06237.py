import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# Community gardeners in Urbanville participated in a survey on their favorite vegetables to grow. 
# This chart displays the number of gardeners growing each type of vegetable. Additionally, 
# it highlights the growth in the number of gardeners over the past year to demonstrate the rising trend and interest in urban gardening.

# Data
vegetables = ['Tomatoes', 'Carrots', 'Lettuce', 'Peppers', 'Cucumbers', 'Zucchini', 'Spinach', 'Beans']
gardeners = [120, 85, 60, 95, 100, 70, 65, 55]  # Number of gardeners growing each vegetable
growth = [15, 10, 5, 12, 14, 7, 3, 8]  # Growth in the number of gardeners over the past year

# Define colors for the bars
colors = ['#E57373', '#FFD54F', '#81C784', '#FF8A65', '#64B5F6', '#A1887F', '#4DD0E1', '#9575CD']

# Set up the plot layout
fig, ax = plt.subplots(2, 1, figsize=(12, 10))

# Bar chart for the number of gardeners
ax[0].bar(vegetables, gardeners, color=colors, alpha=0.8)
ax[0].set_title("Community Gardeners' Favorite Vegetables", fontsize=16, fontweight='bold', pad=20)
ax[0].set_ylabel('Number of Gardeners', fontsize=14)
ax[0].set_xlabel('Vegetable Types', fontsize=14)
ax[0].tick_params(axis='x', rotation=45, labelsize=12)
ax[0].tick_params(axis='y', labelsize=12)

# Bar chart for growth rates with color coding based on positive/negative growth
growth_colors = ['#76FF03' if g > 0 else '#F44336' for g in growth]
ax[1].bar(vegetables, growth, color=growth_colors, alpha=0.8)
ax[1].set_title("Growth in the Number of Gardeners Over the Past Year", fontsize=16, fontweight='bold', pad=20)
ax[1].set_ylabel('Growth in Number of Gardeners', fontsize=14)
ax[1].set_xlabel('Vegetable Types', fontsize=14)
ax[1].tick_params(axis='x', rotation=45, labelsize=12)
ax[1].tick_params(axis='y', labelsize=12)

# Adding annotations on the growth bars
for i, v in enumerate(growth):
    ax[1].text(i, v + (1 if v > 0 else -1), f"{v}", ha='center', va='bottom' if v > 0 else 'top', fontsize=12, color='black')

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()
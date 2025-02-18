import matplotlib.pyplot as plt
import numpy as np

# Data Labels for Vegetables
vegetables = ['Lettuce', 'Beans', 'Spinach', 'Carrots', 'Zucchini', 'Peppers', 'Cucumbers', 'Tomatoes']
gardeners = [60, 55, 65, 85, 70, 95, 100, 120]
growth = [5, 8, 3, 10, 7, 12, 14, 15]

# Define colors for the bars
colors = ['#81C784', '#9575CD', '#4DD0E1', '#FFD54F', '#A1887F', '#FF8A65', '#64B5F6', '#E57373']

# Set up the plot layout with a different number of rows and columns
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Bar chart for the number of gardeners
ax[0].bar(vegetables, gardeners, color=colors, alpha=0.8)
ax[0].set_title("Preferred Vegetables by Urban Growers", fontsize=16, fontweight='bold', pad=20)
ax[0].set_ylabel('Gardeners Count', fontsize=14)
ax[0].set_xlabel('Types of Veggies', fontsize=14)
ax[0].tick_params(axis='x', rotation=45, labelsize=12)
ax[0].tick_params(axis='y', labelsize=12)

# Bar chart for growth rates with color coding for positive growth
growth_colors = ['#76FF03' if g > 0 else '#F44336' for g in growth]
ax[1].bar(vegetables, growth, color=growth_colors, alpha=0.8)
ax[1].set_title("Yearly Increase in Gardener Numbers", fontsize=16, fontweight='bold', pad=20)
ax[1].set_ylabel('Gardener Growth', fontsize=14)
ax[1].set_xlabel('Veggie Varieties', fontsize=14)
ax[1].tick_params(axis='x', rotation=45, labelsize=12)
ax[1].tick_params(axis='y', labelsize=12)

# Adding annotations on the growth bars
for i, v in enumerate(growth):
    ax[1].text(i, v + (1 if v > 0 else -1), f"{v}", ha='center', va='bottom' if v > 0 else 'top', fontsize=12, color='black')

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()
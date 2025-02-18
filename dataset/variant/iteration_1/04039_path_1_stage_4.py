import matplotlib.pyplot as plt
import numpy as np

# Define the e-commerce sector growth data after removing Digital Services
food_delivery = np.array([3, 5, 7, 9, 12])
online_retail = np.array([15, 25, 35, 45, 60])

# Group remaining data into a 2D array
ecommerce_data = [food_delivery, online_retail]

# Initialize the plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Create the boxplot
boxprops_set = [
    dict(facecolor='#ffcc00', color='black'),  # Food Delivery color
    dict(facecolor='#ff6f69', color='black')   # Online Retail color
]

bp = ax1.boxplot(ecommerce_data, vert=False, patch_artist=True,
                 labels=['Food Delivery', 'Online Retail'],
                 whiskerprops=dict(color='black'),
                 capprops=dict(color='black'),
                 medianprops=dict(color='red'))

# Apply colors to each box
for patch, color_props in zip(bp['boxes'], boxprops_set):
    patch.set(**color_props)

# Customize the plot with titles and labels
ax1.set_title("E-commerce Sector Growth (2019-2023)", fontsize=16, fontweight='bold')
ax1.set_xlabel('Revenue (Billions of Dollars)', fontsize=14)
ax1.set_ylabel('Sector', fontsize=14)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()
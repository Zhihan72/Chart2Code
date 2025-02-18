import matplotlib.pyplot as plt
import numpy as np

# Define the e-commerce sector growth data
food_delivery = np.array([3, 5, 7, 9, 12])
online_retail = np.array([15, 25, 35, 45, 60])
digital_services = np.array([6, 10, 15, 20, 25])

# Group all data into a 2D array for horizontal box plot
ecommerce_data = [food_delivery, online_retail, digital_services]

# Initialize the plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Use a horizontal boxplot with shuffled colors
boxprops_set = [
    dict(facecolor='#ffcc00', color='black'),  # Changed color for Food Delivery
    dict(facecolor='#ff6f69', color='black'),  # Changed color for Online Retail
    dict(facecolor='#8dd3c7', color='black')   # Retained color for Digital Services
]

# Create the boxplot with the shuffled colors
bp = ax1.boxplot(ecommerce_data, vert=False, patch_artist=True,
                 labels=['Food Delivery', 'Online Retail', 'Digital Services'],
                 whiskerprops=dict(color='black'),
                 capprops=dict(color='black'),
                 medianprops=dict(color='red'))

# Apply different colors to each box
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
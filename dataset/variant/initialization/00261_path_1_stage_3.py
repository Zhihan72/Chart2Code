import matplotlib.pyplot as plt
import numpy as np

# Define categories and household data
categories = ['Energy Consumption', 'Waste Reduction', 'Water Usage', 'Transport Habits', 'Green Purchases']
household_data = {
    'Household A': [9, 6, 8, 7, 7],
    'Household B': [8, 7, 6, 8, 9],
    'Household C': [9, 6, 7, 6, 8],
    'Household D': [8, 6, 9, 7, 5],
}

# Calculate average data for each category
average_data = np.mean(list(household_data.values()), axis=0)

# Sort the average data and corresponding categories
sorted_indices = np.argsort(average_data)  # Ascending order
sorted_categories = [categories[i] for i in sorted_indices]
sorted_average_data = average_data[sorted_indices]

# Plot a bar chart with sorted average data
plt.figure(figsize=(10, 6))
plt.barh(sorted_categories, sorted_average_data, color='skyblue')
plt.xlabel('Average Score')
plt.title('Sorted Bar Chart of Household Data')
plt.tight_layout()
plt.show()
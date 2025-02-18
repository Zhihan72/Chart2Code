import matplotlib.pyplot as plt
import numpy as np

categories = ['Water Consumption', 'Transport Reduction', 'Energy Usage', 'Purchasing Habits', 'Waste Management']
household_data = {
    'Family X': [8, 7, 9, 6, 7], 
    'Family Y': [7, 9, 6, 8, 7], 
    'Family Z': [6, 7, 9, 8, 6],
    'Family W': [5, 9, 7, 6, 8], 
}

average_data = np.mean([list(household_data.values())[i] for i in range(len(household_data))], axis=0).tolist()

sorted_indices = np.argsort(average_data)
sorted_categories = [categories[i] for i in sorted_indices]
sorted_averages = [average_data[i] for i in sorted_indices]

plt.figure(figsize=(10, 6))
plt.bar(sorted_categories, sorted_averages, color='lightblue')
plt.xlabel('Categories', fontsize=12)
plt.ylabel('Average Values', fontsize=12)
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Original data
consumption_percentages = [25, 20, 15, 25, 15]
single_color = '#6db33f'
years = ['2018', '2019', '2020', '2021', '2022']

# Sorting the consumption percentages in descending order
sorted_indexes = sorted(range(len(consumption_percentages)), key=lambda k: consumption_percentages[k], reverse=True)
sorted_percentages = [consumption_percentages[i] for i in sorted_indexes]
sorted_years = [years[i] for i in sorted_indexes]

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot sorted bar chart
ax.bar(sorted_years, sorted_percentages, color=single_color, alpha=0.7)

# Set labels and a title
ax.set_ylabel('Consumption Percentage')
ax.set_xlabel('Years')
ax.set_title('Sorted Bar Chart of Consumption Percentages (Descending)')

plt.tight_layout()
plt.show()
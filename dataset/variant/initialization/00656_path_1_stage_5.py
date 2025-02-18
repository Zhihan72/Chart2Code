import matplotlib.pyplot as plt
import numpy as np

cities = ['NY', 'LDN', 'TKY', 'SYD']
years = np.arange(2010, 2020)
ucri_scores = np.array([
    [68, 70, 72, 75, 77, 80, 83, 85, 86, 88],
    [65, 67, 69, 72, 74, 76, 78, 80, 82, 84],
    [74, 76, 77, 78, 80, 82, 83, 85, 87, 90],
    [70, 73, 75, 78, 81, 84, 86, 87, 88, 90]
])

# Find the average UCRI score for each city to represent in the bar chart
average_ucri_scores = ucri_scores.mean(axis=1)

fig, ax = plt.subplots(figsize=(10, 8))

# Create a horizontal bar chart
ax.barh(cities, average_ucri_scores, color='skyblue')

# Adding data labels to the bars
for i in range(len(cities)):
    ax.text(average_ucri_scores[i], i, f"{average_ucri_scores[i]:.1f}",
            va='center', ha='left', color='black', fontsize=10)

# Add titles and labels
ax.set_xlabel('Average UCRI Score (2010-2019)')
ax.set_title('Average UCRI Scores of Cities from 2010 to 2019')

plt.tight_layout()
plt.show()
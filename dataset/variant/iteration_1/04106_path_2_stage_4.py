import matplotlib.pyplot as plt
import numpy as np

# Define the age groups and hobbies
age_groups = ['40s', '50+', '20s', '30s']  # shuffled age groups
hobbies = ['Gaming', 'Cooking', 'Exercising', 'Reading', 'Gardening']  # shuffled hobbies

# Altered data corresponding to the shuffled age groups and hobbies
data = {
    '40s':         [45, 20, 20, 12, 15],  # previously '20s'
    '50+':         [30, 25, 30, 20, 20],  # previously '30s'
    '20s':         [15, 30, 25, 30, 25],  # previously '40s'
    '30s':         [35, 35, 20, 35, 10],  # previously '50+'
}

fig, ax = plt.subplots(figsize=(14, 8))
indices = np.arange(len(hobbies))
bottom_values = np.zeros(len(hobbies))
colors = ['#FFCC99', '#FF6666', '#66B3FF', '#99FF99']  # shuffled colors

# Plotting the stacked bars for each age group
for i, age_group in enumerate(age_groups):
    ax.bar(indices, data[age_group], label=age_group, bottom=bottom_values, color=colors[i])
    bottom_values += np.array(data[age_group])

# Altered labels and title
ax.set_xlabel('Leisure Activities', fontsize=14)  # altered text
ax.set_ylabel('Hours Allocated', fontsize=14)  # altered text
ax.set_title('Time Invested in Hobbies:\nAge Group Analysis for Sep 2023', fontsize=16, weight='bold')  # altered text
ax.set_xticks(indices)
ax.set_xticklabels(hobbies, fontsize=12)
ax.legend(title='Demographics', loc='upper right')  # altered text

# Adding exact data labels on each segment of the stack
for i, age_group in enumerate(age_groups):
    cumulative_values = np.zeros(len(hobbies))
    for j, value in enumerate(data[age_group]):
        cumulative_values[j] = bottom_values[j] - data[age_group][j]
        ax.text(indices[j], cumulative_values[j] + value / 2, str(value),
                ha='center', va='center', fontsize=10, color='black', fontweight='bold')

ax.yaxis.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
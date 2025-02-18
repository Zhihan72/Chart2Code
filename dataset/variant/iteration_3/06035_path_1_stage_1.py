import matplotlib.pyplot as plt
import numpy as np

# Define the years for the dataset
years = np.array([2018, 2019, 2020, 2021, 2022])

# Altered average screen time data for different age groups (in hours)
screen_time_data = {
    '12-13 years': np.array([3.4, 4.5, 3.2, 4.0, 4.2]),  # Randomized within original values
    '14-15 years': np.array([4.5, 3.5, 3.7, 4.8, 4.3]),  # Randomized within original values
    '16-17 years': np.array([4.2, 4.7, 5.2, 4.9, 4.0])   # Randomized within original values
}

# Error margins representing uncertainty in screen time data (in hours)
error_margins = {
    '12-13 years': np.array([0.3, 0.3, 0.4, 0.4, 0.5]),
    '14-15 years': np.array([0.3, 0.3, 0.4, 0.4, 0.5]),
    '16-17 years': np.array([0.3, 0.3, 0.4, 0.4, 0.5])
}

# Initialize the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Define bar width and positions for clustered bars
bar_width = 0.25
positions = np.arange(len(years))

# Iterating over each age group to plot the bars with error bars
colors = ['#ff9999','#66b3ff','#99ff99']
for i, (age_group, data) in enumerate(screen_time_data.items()):
    ax.bar(positions + i * bar_width, data, bar_width,
           label=age_group, yerr=error_margins[age_group], capsize=5, color=colors[i], alpha=0.7)

# Adding labels, title, and legend
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Average Screen Time (Hours per Day)', fontsize=12)
ax.set_title('Average Daily Screen Time of Teenagers (2018-2022)', fontsize=14, fontweight='bold')
ax.set_xticks(positions + bar_width)
ax.set_xticklabels(years)
ax.legend(title='Age Group', loc='upper left')

# Adding gridlines and tight layout adjustment
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
plt.tight_layout()

# Show the plot
plt.show()
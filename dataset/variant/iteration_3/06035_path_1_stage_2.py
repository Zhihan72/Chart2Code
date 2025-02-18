import matplotlib.pyplot as plt
import numpy as np

# Define the years for the dataset
years = np.array([2018, 2019, 2020, 2021, 2022])

# Altered average screen time data for different age groups
screen_time_data = {
    '12-13 years': np.array([3.4, 4.5, 3.2, 4.0, 4.2]), 
    '14-15 years': np.array([4.5, 3.5, 3.7, 4.8, 4.3]),
    '16-17 years': np.array([-4.2, -4.7, -5.2, -4.9, -4.0])  # Inverted for diverging effect
}

# Initialize the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Define bar width
bar_width = 0.35

# Create diverging bars, stacking the negative values downwards
for i, (age_group, data) in enumerate(screen_time_data.items()):
    ax.barh(years if i == 0 else -years, data, bar_width, label=age_group, color=f'C{i}', alpha=0.7)

# Adding labels, title, and legend
ax.set_xlabel('Average Screen Time (Hours per Day)', fontsize=12)
ax.set_ylabel('Year', fontsize=12)
ax.set_title('Diverging Average Daily Screen Time of Teenagers (2018-2022)', fontsize=14, fontweight='bold')
ax.set_yticks(years)
ax.set_yticklabels(years)
ax.legend(title='Age Group', loc='upper left')

# Adding gridlines and tight layout adjustment
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
plt.axvline(0, color='black', linewidth=0.8)  # Central axis for divergence
plt.tight_layout()

# Show the plot
plt.show()
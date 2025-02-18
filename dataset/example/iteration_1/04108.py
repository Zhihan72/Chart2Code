import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The city of Techville has launched a new tech initiative focusing on increasing diversity in tech education.
# This chart shows the percentage enrollment of various demographics in tech courses over five years.

# Define the years and demographics
years = ['2018', '2019', '2020', '2021', '2022']
demographics = ['Women', 'Men', 'Non-Binary', 'Underrepresented Minorities', 'Others']

# Enrollment data (percentage)
data = {
    'Women': [30, 32, 35, 38, 40],
    'Men': [50, 48, 45, 40, 38],
    'Non-Binary': [2, 4, 6, 8, 10],
    'Underrepresented Minorities': [15, 16, 18, 20, 22],
    'Others': [3, 3.5, 4, 4.5, 5]
}

# Colors for each demographic
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Prepare the data for stacked bar chart
def prepare_data(data, years):
    n_years = len(years)
    n_groups = len(data)
    y_offsets = np.zeros(n_years)
    y_data = []
    
    for key, values in data.items():
        y_data.append((y_offsets.copy(), values, key))
        y_offsets += values
    return y_data

y_data = prepare_data(data, years)

# Plot setup
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each group as a stacked bar
for y_offset, values, label in y_data:
    ax.bar(years, values, bottom=y_offset, label=label, color=colors.pop(0), edgecolor='black')

# Title and axis labels
ax.set_title('Techville Diversity in Tech Education Enrollment (2018-2022)', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Percentage Enrollment (%)', fontsize=12, weight='bold')
ax.set_xlabel('Year', fontsize=12, weight='bold')

# Add legend
ax.legend(title='Demographics', loc='upper left', bbox_to_anchor=(1, 1))

# Adding data labels to each segment
for i, year in enumerate(years):
    for y_offset, values, label in y_data:
        ax.text(i, y_offset[i] + values[i] / 2, f'{values[i]}%', ha='center', va='center', 
                color='black', fontsize=9, weight='bold')

# Adding a note text box
ax.text(4.5, 100, 'Note: Focus on increasing diversity in tech education\nhas shown positive impact over the years.',
        fontsize=12, style='italic', ha='right', va='center',
        bbox={'facecolor': 'lightgray', 'alpha': 0.5, 'pad': 5})

# Enable grid lines for the y-axis
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Show plot
plt.show()
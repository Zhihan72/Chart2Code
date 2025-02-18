import matplotlib.pyplot as plt
import numpy as np

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

# Prepare the stacked bar chart data
def prepare_data(data, years):
    n_years = len(years)
    y_offsets = np.zeros(n_years)
    y_data = []
    
    for _, values in data.items():
        y_data.append((y_offsets.copy(), values))
        y_offsets += values
    return y_data

y_data = prepare_data(data, years)

# Plot setup
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each group as a stacked bar
for y_offset, values in y_data:
    ax.bar(years, values, bottom=y_offset, color=colors.pop(0), edgecolor='black')

# Enable grid lines for the y-axis
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Show plot
plt.show()
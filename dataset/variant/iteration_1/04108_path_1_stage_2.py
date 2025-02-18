import matplotlib.pyplot as plt
import numpy as np

# Define the years and demographics
years = ['2018', '2019', '2020', '2021', '2022']
demographics = ['Women', 'Men', 'Non-Binary', 'Underrepresented Minorities', 'Others']

# Altered enrollment data (percentage) to simulate randomness while maintaining structure
data = {
    'Women': [35, 32, 30, 40, 38],
    'Men': [45, 48, 50, 38, 40],
    'Non-Binary': [6, 4, 10, 2, 8],
    'Underrepresented Minorities': [18, 20, 15, 22, 16],
    'Others': [4, 3.5, 5, 4.5, 3]
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

plt.tight_layout()
plt.show()
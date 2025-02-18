import matplotlib.pyplot as plt
import numpy as np

# Define the years and demographics
years = ['2018', '2019', '2020', '2021', '2022']
demographics = ['Women', 'Men', 'Non-Binary', 'Underrepresented Minorities', 'Others']

# Altered enrollment data (percentage)
data = {
    'Women': [35, 32, 30, 40, 38],
    'Men': [-45, -48, -50, -38, -40],
    'Non-Binary': [6, 4, 10, 2, 8],
    'Underrepresented Minorities': [-18, -20, -15, -22, -16],
    'Others': [4, 3.5, 5, 4.5, 3]
}

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

fig, ax = plt.subplots(figsize=(12, 8))

# Prepare and plot diverging stacked bar chart
for i, category in enumerate(demographics):
    values = data[category]
    ax.bar(years, values, label=category, color=colors[i], edgecolor='black')

# Add a central vertical line
ax.axhline(0, color='black', linewidth=0.8)

# Enable grid lines for the x-axis
ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

ax.set_ylabel('Percentage')
ax.set_title('Diverging Bar Chart of Enrollment Data')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()
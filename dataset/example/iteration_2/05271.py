import matplotlib.pyplot as plt
import numpy as np

# Backstory: Examining Monthly Revenue Streams from Subsidiary Companies
# Company ABC is analyzing its monthly revenue contributions from four major subsidiary companies over a year.

# Define the Months and Companies
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
companies = ['Company X', 'Company Y', 'Company Z', 'Company W']

# Create fictional revenue data for each company over the months
# Revenue in thousands of dollars
company_x = [55, 60, 58, 62, 65, 68, 70, 72, 75, 78, 82, 85]
company_y = [40, 42, 45, 47, 50, 51, 53, 55, 58, 60, 62, 64]
company_z = [30, 35, 32, 37, 38, 40, 41, 43, 45, 47, 49, 50]
company_w = [25, 27, 29, 30, 32, 34, 36, 37, 38, 39, 40, 41]

# Stack the data for each month
revenue_data = [company_x, company_y, company_z, company_w]

# Colors for each company
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']

# Create the stacked bar chart
fig, ax = plt.subplots(figsize=(14, 9))

# Width of each bar
bar_width = 0.7
x_indexes = np.arange(len(months))

# Plotting each company's revenue as a stacked component
for i, revenue in enumerate(revenue_data):
    bottom = np.zeros(len(months)) if i == 0 else sum(revenue_data[i])
    ax.bar(x_indexes, revenue, width=bar_width, label=companies[i], color=colors[i], alpha=0.8, bottom=bottom)

# Title and labels
ax.set_title('Monthly Revenue Contributions from Subsidiary Companies in 2022\nCompany ABC Financial Overview', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Revenue (in thousands of dollars)', fontsize=14)

# Customize ticks
plt.xticks(ticks=x_indexes, labels=months, rotation=45, ha='right')
plt.yticks(np.arange(0, 300, 20))

# Legend
ax.legend(title='Subsidiary Companies', loc='upper left', bbox_to_anchor=(1, 1), fontsize=12, title_fontsize='13')

# Add grid for improved readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust the layout to fit everything nicely
plt.tight_layout()

# Show the plot
plt.show()
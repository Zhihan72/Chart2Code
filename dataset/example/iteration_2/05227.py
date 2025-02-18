import matplotlib.pyplot as plt
import numpy as np

# Backstory: The goal here is to study the growth trend in the tech industry 
# by comparing the number of startups founded per year over a recent 10-year period.
years = np.arange(2012, 2022)
startups_founded = [50, 55, 60, 85, 120, 135, 150, 170, 200, 220]

# Data for a second subplot (line chart) showing the number of employees in the industry
years_line = np.arange(2012, 2022)
employees = [1000, 1100, 1050, 1300, 1400, 1600, 1750, 1800, 2100, 2300]

# Create the figure and two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 2]})

# Bar chart in the top subplot
bars = ax1.bar(years, startups_founded, color=plt.cm.tab20c(np.linspace(0, 1, len(startups_founded))), edgecolor='black')

# Customize the bar chart
ax1.set_title('Growth of Tech Startups Over the Last Decade', fontsize=18, weight='bold', loc='left', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Number of Startups Founded', fontsize=14)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)
ax1.set_xlim(2011, 2022)

# Annotate each bar with the number of startups
for bar, value in zip(bars, startups_founded):
    ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 3, f'{value}', ha='center', va='bottom', fontsize=12, color='black')

# Line chart in the bottom subplot
ax2.plot(years_line, employees, marker='o', color='skyblue', markerfacecolor='blue', markersize=9, linewidth=3)

# Customize the line chart
ax2.set_title('Increase in Tech Industry Employment', fontsize=18, weight='bold', loc='left', pad=20)
ax2.set_xlabel('Year', fontsize=14)
ax2.set_ylabel('Number of Employees (in thousands)', fontsize=14)
ax2.yaxis.grid(True, linestyle='--', alpha=0.7)
ax2.set_xlim(2011, 2022)
ax2.set_ylim(900, 2500)

# Annotate each point in the line chart with the number of employees
for i in range(len(years_line)):
    ax2.annotate(f'{employees[i]}k', (years_line[i], employees[i] + 50), fontsize=12, ha='center')

# Adjust layout to prevent overlap and regenerate the grid
fig.tight_layout(pad=3.0)

# Add a common super title for the entire figure
fig.suptitle('The Evolution of Tech Startups and Employment (2012-2021)', fontsize=20, weight='bold')

# Display the plot
plt.show()
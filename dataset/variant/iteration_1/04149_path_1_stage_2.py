import matplotlib.pyplot as plt
import numpy as np

# Data: Quarters and GDP values in billion Planet X credits
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
agriculture_gdp = [5.5, 6.0, 6.8, 7.2]
manufacturing_gdp = [4.4, 4.9, 5.5, 6.1]
technology_gdp = [8.0, 8.5, 9.2, 10.0]
services_gdp = [6.2, 6.7, 7.1, 7.5]

# Cumulative GDP calculation
cumulative_gdp = np.cumsum([sum(x) for x in zip(agriculture_gdp, manufacturing_gdp, technology_gdp, services_gdp)])

# Set up the figure and axis
fig, ax1 = plt.subplots(figsize=(14, 7))

# Bar widths
width = 0.2

# Bar positions
x_indices = np.arange(len(quarters))

# Apply a single color across all bars
single_color = 'tab:gray'

# Plotting individual bars for each sector with the same color
ax1.bar(x_indices - width*1.5, agriculture_gdp, width=width, color=single_color)
ax1.bar(x_indices - width/2, manufacturing_gdp, width=width, color=single_color)
ax1.bar(x_indices + width/2, technology_gdp, width=width, color=single_color)
ax1.bar(x_indices + width*1.5, services_gdp, width=width, color=single_color)

# Titles and labels
ax1.set_title('Planet X Quarterly GDP Report (2023)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Quarter', fontsize=12)
ax1.set_ylabel('GDP (billion credits)', fontsize=12)
ax1.set_xticks(x_indices)
ax1.set_xticklabels(quarters)

# Cumulative GDP Plot
ax2 = ax1.twinx()
ax2.plot(x_indices, cumulative_gdp, color='black', marker='o', linestyle='-', linewidth=2)

# Annotate the cumulative GDP plot
for i, val in enumerate(cumulative_gdp):
    ax2.text(i, val, f'{val:.1f}', color='black', fontsize=10, ha='center', va='bottom')

# Ensure the layout is tight and avoids overlap
plt.tight_layout()

# Display the plot
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Data: Quarters and GDP values in billion Planet X credits
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
agriculture_gdp = [5.5, 6.0, 6.8, 7.2]
manufacturing_gdp = [4.4, 4.9, 5.5, 6.1]
services_gdp = [6.2, 6.7, 7.1, 7.5]

# Cumulative GDP calculation
cumulative_gdp = np.cumsum([sum(x) for x in zip(agriculture_gdp, manufacturing_gdp, services_gdp)])

# Set up the figure and axis
fig, ax1 = plt.subplots(figsize=(14, 7))

# Bar heights
height = 0.2

# Bar positions
y_indices = np.arange(len(quarters))

# Apply a single color across all bars
single_color = 'tab:gray'

# Plotting individual bars for each sector with the same color
ax1.barh(y_indices - height, agriculture_gdp, height=height, color=single_color)
ax1.barh(y_indices, manufacturing_gdp, height=height, color=single_color)
ax1.barh(y_indices + height, services_gdp, height=height, color=single_color)

# Titles and labels
ax1.set_title('Planet X Quarterly GDP Report (2023)', fontsize=16, fontweight='bold', pad=20)
ax1.set_ylabel('Quarter', fontsize=12)
ax1.set_xlabel('GDP (billion credits)', fontsize=12)
ax1.set_yticks(y_indices)
ax1.set_yticklabels(quarters)

# Cumulative GDP Plot
ax2 = ax1.twiny()
ax2.plot(cumulative_gdp, y_indices, color='black', marker='o', linestyle='-', linewidth=2)

# Annotate the cumulative GDP plot
for i, val in enumerate(cumulative_gdp):
    ax2.text(val, i, f'{val:.1f}', color='black', fontsize=10, va='center', ha='left')

# Ensure the layout is tight and avoids overlap
plt.tight_layout()

# Display the plot
plt.show()
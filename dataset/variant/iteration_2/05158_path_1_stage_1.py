import matplotlib.pyplot as plt
import numpy as np

# Months
months = np.array([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])

# Electricity consumption data (in kWh) for the current and previous year
consumption_current_year = np.array([150, 160, 155, 140, 170, 200, 210, 220, 190, 180, 175, 165])
consumption_previous_year = np.array([145, 150, 150, 138, 165, 195, 205, 215, 185, 175, 170, 160])

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plot data for the current year
ax.plot(months, consumption_current_year, marker='o', markersize=8, linestyle='-', color='blue')

# Plot data for the previous year
ax.plot(months, consumption_previous_year, marker='s', markersize=8, linestyle='--', color='green')

# Adding titles and labels
ax.set_title('Monthly Household Electricity Consumption: A Yearly Comparison', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Electricity Consumption (kWh)', fontsize=14)

# Removing plot borders (spines)
for spine in ax.spines.values():
    spine.set_visible(False)

# Annotating peak consumption points
peak_current = months[np.argmax(consumption_current_year)]
peak_previous = months[np.argmax(consumption_previous_year)]
ax.annotate(f'Peak: {peak_current} ({max(consumption_current_year)} kWh)', 
            xy=(peak_current, max(consumption_current_year)), 
            xytext=(peak_current, max(consumption_current_year) + 20),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=12, color='blue')
ax.annotate(f'Peak: {peak_previous} ({max(consumption_previous_year)} kWh)', 
            xy=(peak_previous, max(consumption_previous_year)), 
            xytext=(peak_previous, max(consumption_previous_year) + 20),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=12, color='green')

# Ensuring that the x-axis labels do not overlap
plt.xticks(rotation=45)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()
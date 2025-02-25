import matplotlib.pyplot as plt
import numpy as np

# Months
months = np.array([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])

# Altered electricity consumption data (in kWh) for the current and previous year
consumption_current_year = np.array([160, 155, 140, 150, 200, 170, 190, 220, 210, 180, 165, 175])
consumption_previous_year = np.array([150, 145, 165, 138, 160, 195, 185, 215, 205, 175, 160, 170])

fig, ax = plt.subplots(figsize=(14, 8))

# Plot altered data for the current year
ax.plot(months, consumption_current_year, marker='o', markersize=8, linestyle='-', color='blue')

# Plot altered data for the previous year
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

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
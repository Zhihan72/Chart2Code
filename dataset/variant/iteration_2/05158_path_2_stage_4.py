import matplotlib.pyplot as plt
import numpy as np

months = np.array([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])

consumption_current_year = np.array([160, 150, 145, 175, 180, 200, 220, 170, 190, 210, 165, 155])
consumption_previous_year = np.array([145, 150, 150, 138, 165, 195, 205, 215, 185, 175, 170, 160])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(months, consumption_current_year, marker='o', markersize=8, linestyle='-', color='green')
ax.plot(months, consumption_previous_year, marker='s', markersize=8, linestyle='--', color='blue')

ax.set_title('Household Electricity: Yearly', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Consumption (kWh)', fontsize=14)

peak_current = months[np.argmax(consumption_current_year)]
peak_previous = months[np.argmax(consumption_previous_year)]
ax.annotate(f'Peak: {peak_current}', 
            xy=(peak_current, max(consumption_current_year)), 
            xytext=(peak_current, max(consumption_current_year) + 20),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=12, color='green')
ax.annotate(f'Peak: {peak_previous}', 
            xy=(peak_previous, max(consumption_previous_year)), 
            xytext=(peak_previous, max(consumption_previous_year) + 20),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=12, color='blue')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
temperatures = [18.0, 16.1, 15.4, 27.5, 23.2, 20.5, 15.0, 27.0, 18.3, 21.2, 25.3, 25.7]
rainfall = [20, 110, 18, 55, 60, 78, 42, 40, 30, 90, 25, 120]

fig, ax1 = plt.subplots(figsize=(12, 8))

# Set a single color for both temperature and rainfall plot lines
consistent_color = 'tab:blue'

ax1.plot(months, temperatures, color=consistent_color, marker='x', linestyle='-.', linewidth=2.5, label='Avg Temperature (°C)')
ax1.set_xlabel('Months', fontsize=12)
ax1.set_ylabel('Average Temperature (°C)', fontsize=12, color=consistent_color)
ax1.tick_params(axis='y', labelcolor=consistent_color)

ax2 = ax1.twinx()

ax2.plot(months, rainfall, color=consistent_color, marker='d', linestyle='-', linewidth=1.5, label='Total Rainfall (mm)')
ax2.set_ylabel('Total Rainfall (mm)', fontsize=12, color=consistent_color)
ax2.tick_params(axis='y', labelcolor=consistent_color)
ax2.grid(axis='y', linestyle='-', color='gray', alpha=0.4)

plt.title("Monthly Climate Analysis\nTemperature and Rainfall Trends", fontsize=14, fontweight='bold')

ax1.legend(loc='lower left')
ax2.legend(loc='lower right')

plt.tight_layout()
plt.show()
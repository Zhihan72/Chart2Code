import matplotlib.pyplot as plt
import numpy as np

# Years for the data (2010-2020)
years = np.arange(2010, 2021)

# Artificial data representing average monthly measurements for different river health parameters
dissolved_oxygen = [7.5, 7.2, 6.9, 6.7, 6.5, 6.2, 6.0, 5.8, 5.6, 5.5, 5.2]
ph_level = [7.0, 6.9, 6.8, 6.7, 6.5, 6.4, 6.3, 6.1, 6.0, 6.0, 5.9]
nitrate_concentration = [5, 5.5, 6, 6.2, 6.5, 7, 7.3, 7.5, 8, 8.2, 8.5]

# Create subplots
fig, ax1 = plt.subplots(figsize=(14, 7))

# Use secondary y-axis for nitrate concentration
ax2 = ax1.twinx()

# Plot the line chart for dissolved oxygen and pH level
ax1.plot(years, dissolved_oxygen, label='Dissolved Oxygen (mg/L)', color='black', marker='o', linewidth=2)
ax1.plot(years, ph_level, label='pH Level', color='black', marker='^', linewidth=2)

# Plot the nitrate concentration on a secondary y-axis
ax2.plot(years, nitrate_concentration, label='Nitrate Concentration (mg/L)', color='black', marker='s', linewidth=2)

# Adding labels and title
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Dissolved Oxygen (mg/L) / pH Level', fontsize=12, color='black')
ax2.set_ylabel('Nitrate Concentration (mg/L)', fontsize=12, color='black')
plt.title('Decadal Health Monitoring of River (2010-2020)', fontsize=16, fontweight='bold')

# Adding grid for better readability
ax1.grid(visible=True, which='both', linestyle='--', linewidth=0.7, color='grey', alpha=0.5)

# Customizing ticks and legends
ax1.tick_params(axis='y', colors='black')
ax2.tick_params(axis='y', colors='black')
fig.tight_layout()  # Adjust the layout

# Adding legends
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9), fontsize=10, title='Parameters')

# Display the plot
plt.show()
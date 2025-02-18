import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking the rise in renewable energy production over the recent decade
# Insight: Analyze the yearly production of Solar and Wind energy, along with total renewable energy production

# Years of observation
years = np.arange(2010, 2021)

# Artificial data for renewable energy production (in Terawatt-hours)
solar_energy = [10, 25, 45, 65, 90, 120, 150, 180, 220, 250, 300]  # Rising solar power production
wind_energy = [40, 60, 75, 95, 120, 145, 170, 195, 210, 240, 280]  # Steady increase in wind power

# Total renewable energy production (Solar + Wind)
total_renewable = [s + w for s, w in zip(solar_energy, wind_energy)]

# Initialize the plot
fig, ax1 = plt.subplots(figsize=(14, 9))

# Plot Solar and Wind energy on the primary y-axis
ax1.plot(years, solar_energy, color='orange', linestyle='-', linewidth=2, marker='o', label='Solar Energy')
ax1.plot(years, wind_energy, color='blue', linestyle='--', linewidth=2, marker='s', label='Wind Energy')

# Grid and layout adjustments
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add a secondary y-axis for total renewable energy production
ax2 = ax1.twinx()
ax2.plot(years, total_renewable, color='green', linestyle='-', linewidth=2, marker='x', label='Total Renewable')

# Set titles and labels
ax1.set_title('Decade-long Progress in Renewable Energy Production\nFocus on Solar and Wind Energy (2010-2020)', fontsize=16, weight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Individual Production (TWh)', fontsize=14, color='black')
ax2.set_ylabel('Total Production (TWh)', fontsize=14, color='black')

# Add trend lines
z_solar = np.polyfit(years, solar_energy, 1)
p_solar = np.poly1d(z_solar)
ax1.plot(years, p_solar(years), color='orange', linestyle=':', alpha=0.5, linewidth=1)

z_wind = np.polyfit(years, wind_energy, 1)
p_wind = np.poly1d(z_wind)
ax1.plot(years, p_wind(years), color='blue', linestyle=':', alpha=0.5, linewidth=1)

z_total = np.polyfit(years, total_renewable, 1)
p_total = np.poly1d(z_total)
ax2.plot(years, p_total(years), color='green', linestyle=':', alpha=0.5, linewidth=1)

# Annotations and highlights
ax1.annotate('Rapid Growth in Solar', xy=(2015, solar_energy[5]), xytext=(2013, 50),
             arrowprops=dict(facecolor='orange', arrowstyle='->'),
             fontsize=12, ha='center')

highlight_year = 2018
ax1.axvline(x=highlight_year, color='red', linestyle='--', linewidth=1, alpha=0.8)
ax1.text(highlight_year + 0.2, 200, 'Milestone in 2018', color='red', fontsize=12, rotation=90)

# Legends
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left', fontsize=12)

# Adjust layout for clarity
plt.tight_layout()

# Display the plot
plt.show()
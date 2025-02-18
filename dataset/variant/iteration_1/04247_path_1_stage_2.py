import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

# Data: Renewable energy consumption in Terawatt-hours (TWh)
solar = [
    1.1, 1.4, 1.8, 2.3, 3.0, 3.8, 5.0, 6.2, 8.0, 10.1, 13.2, 17.0, 
    21.5, 27.0, 34.1, 39.6, 45.0, 52.2, 61.2, 71.3, 83.0
]
wind = [
    4.5, 5.2, 6.1, 7.4, 9.1, 11.0, 13.5, 16.5, 21.2, 26.0, 32.0, 
    38.8, 45.6, 53.2, 61.8, 70.0, 81.0, 94.0, 108.0, 120.0, 135.0
]
hydro = [
    50.0, 51.0, 52.0, 54.0, 55.0, 57.0, 59.5, 62.0, 65.0, 68.0, 71.0, 
    74.0, 77.0, 80.5, 84.0, 88.0, 92.0, 96.0, 100.0, 104.0, 109.0
]

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot data for each renewable energy source with varied stylistic elements
ax.plot(years, solar, label='Solar Energy', marker='x', color='purple', linewidth=1.5, linestyle='--')
ax.plot(years, wind, label='Wind Energy', marker='d', color='green', linewidth=1.5, linestyle=':')
ax.plot(years, hydro, label='Hydroelectric Energy', marker='p', color='blue', linewidth=1.5, linestyle='-.')

# Annotate key milestones (altered positions and colors)
ax.annotate('Rapid Solar Growth', xy=(2013, 27.0), xytext=(2010, 55),
            arrowprops=dict(facecolor='darkgrey', arrowstyle='->'), fontsize=10, ha='center', color='purple')
ax.annotate('Stable Increase in Hydro', xy=(2009, 68.0), xytext=(2003, 85),
            arrowprops=dict(facecolor='grey', arrowstyle='->'), fontsize=10, ha='center', color='blue')

# Annotate each data point with its value for clarity
for i, txt in enumerate(solar):
    ax.text(years[i], solar[i] + 1.5, str(txt), fontsize=8, ha='center', color='purple')
for i, txt in enumerate(wind):
    ax.text(years[i], wind[i] + 1.5, str(txt), fontsize=8, ha='center', color='green')
for i, txt in enumerate(hydro):
    ax.text(years[i], hydro[i] - 4, str(txt), fontsize=8, ha='center', color='blue')

# Set title and labels
ax.set_title("Rising Consumption of Renewable Energy\n(2000-2020)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Energy Consumption (TWh)", fontsize=12)

# Add legend
ax.legend(title='Energy Sources', loc='lower right', fontsize=9)

# Add grid for readability
ax.grid(True, linestyle='-', linewidth=0.3, alpha=0.9)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
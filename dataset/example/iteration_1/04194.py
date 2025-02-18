import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking the Growth of Renewable Energy Production (in MegaWatts) Across Different Countries from 2000 to 2020

# Years from 2000 to 2020
years = np.arange(2000, 2021)

# Artificial data for renewable energy production (MegaWatts) for three countries
country_data = {
    'EcoLand': [50, 55, 60, 70, 80, 95, 110, 125, 145, 170, 200, 235, 275, 320, 370, 425, 490, 565, 650, 745, 850],
    'GreenVille': [40, 45, 50, 55, 65, 80, 95, 110, 130, 155, 185, 220, 260, 305, 355, 410, 475, 545, 620, 705, 800],
    'Sustainia': [30, 35, 40, 45, 55, 70, 85, 100, 120, 145, 175, 210, 250, 295, 345, 400, 465, 535, 610, 695, 790]
}

# Trend data for global renewable energy growth rate based on total production
global_growth_rate = np.array([40, 43, 46, 50, 55, 60, 66, 72, 79, 87, 96, 105, 115, 126, 138, 151, 165, 180, 196, 213, 231])

# Convert the dictionary to a list of values for plotting
values = list(country_data.values())

# Create the figure and axis objects
fig, ax1 = plt.subplots(figsize=(14, 8))

# Define colors for each country
colors = ['#ff9999', '#66b3ff', '#99ff99']

# Plot the line chart for each country's production
for country, color in zip(country_data.keys(), colors):
    ax1.plot(years, country_data[country], color=color, linewidth=2.5, label=country)

# Adding a secondary y-axis for the global growth rate
ax2 = ax1.twinx()
ax2.plot(years, global_growth_rate, color='black', linestyle='--', linewidth=2, label='Global Growth Rate')
 
# Set titles and labels
ax1.set_title("Tracking Renewable Energy Production Growth\nAcross Countries (2000-2020)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Production in MegaWatts', fontsize=12)
ax2.set_ylabel('Global Growth Rate Index', fontsize=12, color='black')

# Customize x-axis
ax1.set_xticks(np.arange(2000, 2021, 2))
ax1.set_xticklabels(np.arange(2000, 2021, 2), fontsize=10, rotation=45)

# Add legends
ax1.legend(loc='upper left', fontsize=10, title='Country Data')
ax2.legend(loc='upper right', fontsize=10, title='Growth Rate')

# Adding grid lines for readability
ax1.grid(True, linestyle='--', which='both', axis='both', alpha=0.6)

# Annotate significant milestones
milestones = {
    2008: 'EcoLand exceeds 100MW',
    2016: 'GreenVille reaches 400MW',
    2020: 'Sustainia approaches 800MW'
}

for year, text in milestones.items():
    ax1.annotate(text, 
                xy=(year, country_data['EcoLand'][year-2000]), 
                xytext=(year-3, country_data['EcoLand'][year-2000]+50),
                arrowprops=dict(facecolor='black', arrowstyle='->'),
                fontsize=10, color='brown')

# Auto-adjust layout
plt.tight_layout()

# Show the plot
plt.show()
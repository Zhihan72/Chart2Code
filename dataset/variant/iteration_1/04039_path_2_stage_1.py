import matplotlib.pyplot as plt
import numpy as np

# Define the years of observation
years = np.arange(2019, 2024)

# E-commerce sector growth during the pandemic (in billions of dollars)
food_delivery = np.array([3, 5, 7, 9, 12])
online_retail = np.array([15, 25, 35, 45, 60])
digital_services = np.array([6, 10, 15, 20, 25])

# Create aggregate data for the area plot
ecommerce_data = np.vstack([food_delivery, online_retail, digital_services])

# Initialize the plot
fig, (ax1) = plt.subplots(figsize=(14, 8))

# Define a single color for the plot
single_color = '#87ceeb'

# Plot the stacked area chart with a single color
ax1.stackplot(years, ecommerce_data, labels=['Food Delivery', 'Online Retail', 'Digital Services'], colors=[single_color] * len(ecommerce_data), alpha=0.85)

# Customize the plot with titles and labels
ax1.set_title("E-commerce Growth during and after COVID-19 Pandemic\n(2019-2023)", fontsize=18, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Revenue (Billions of Dollars)', fontsize=14)

# Add legend and grid for readability
ax1.legend(loc='upper left', fontsize=12, title='Sector', frameon=False)
ax1.grid(linestyle='--', alpha=0.6)

# Annotate significant transitions
ax1.annotate('Surge in\nFood Delivery', xy=(2020, 5), xytext=(2020.5, 18),
             arrowprops=dict(facecolor='green', arrowstyle='->', lw=1.5),
             fontsize=13, color='green')

ax1.annotate('Boom in\nOnline Retail', xy=(2021, 35), xytext=(2021.5, 60),
             arrowprops=dict(facecolor='yellow', arrowstyle='->', lw=1.5),
             fontsize=13, color='yellow')

# Add a descriptive text box for context
props = dict(boxstyle='round', facecolor='lightgray', alpha=0.3)
textstr = ('E-commerce experienced remarkable\n'
           'growth during the pandemic, driving\n'
           'innovation in food delivery, retail, and\n'
           'digital services.')
ax1.text(0.03, 0.97, textstr, transform=ax1.transAxes, fontsize=12,
         verticalalignment='top', bbox=props)

# Highlight start and end values for each sector
for idx, sector in enumerate(['Food Delivery', 'Online Retail', 'Digital Services']):
    ax1.annotate(f'{ecommerce_data[idx, 0]}', (2019, ecommerce_data[idx, 0]),
                 textcoords="offset points", xytext=(-10, 5), ha='center')
    ax1.annotate(f'{ecommerce_data[idx, -1]}', (2023, ecommerce_data[idx, -1] + np.sum(ecommerce_data[:idx, -1])),
                 textcoords="offset points", xytext=(-15, -10), ha='center')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()
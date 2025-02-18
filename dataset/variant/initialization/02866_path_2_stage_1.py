import matplotlib.pyplot as plt
import numpy as np

# Define months for the chart
months = ["January", "February", "March", "April", "May", "June"]

# Define production and consumption data
craft_beer_production = [120, 135, 150, 160, 180, 190]
herbal_tea_production = [110, 130, 125, 140, 145, 155]
organic_coffee_production = [140, 150, 160, 155, 170, 175]

craft_beer_consumption = [100, 120, 130, 140, 160, 170]
herbal_tea_consumption = [90, 110, 115, 120, 130, 145]
organic_coffee_consumption = [130, 145, 150, 140, 160, 165]

# Calculate leftover and efficiency
craft_beer_leftover = np.array(craft_beer_production) - np.array(craft_beer_consumption)
herbal_tea_leftover = np.array(herbal_tea_production) - np.array(herbal_tea_consumption)
organic_coffee_leftover = np.array(organic_coffee_production) - np.array(organic_coffee_consumption)

craft_beer_efficiency = np.array(craft_beer_consumption) / np.array(craft_beer_production)
herbal_tea_efficiency = np.array(herbal_tea_consumption) / np.array(herbal_tea_production)
organic_coffee_efficiency = np.array(organic_coffee_consumption) / np.array(organic_coffee_production)

# Initialize plot with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Subplot 1: Stacked bar chart
bar_width = 0.6

ax1.bar(months, craft_beer_consumption, label='Craft Beer Consumed', color='dodgerblue', alpha=0.85)
ax1.bar(months, herbal_tea_consumption, bottom=craft_beer_consumption, label='Herbal Tea Consumed', color='mediumseagreen', alpha=0.85)
ax1.bar(months, organic_coffee_consumption, bottom=np.array(craft_beer_consumption) + np.array(herbal_tea_consumption), label='Organic Coffee Consumed', color='goldenrod', alpha=0.85)

ax1.bar(months, craft_beer_leftover, bottom=craft_beer_consumption, label='Craft Beer Leftover', color='lightblue', alpha=0.6, hatch='//')
ax1.bar(months, herbal_tea_leftover, bottom=np.array(craft_beer_consumption) + np.array(herbal_tea_consumption), label='Herbal Tea Leftover', color='lightgreen', alpha=0.6, hatch='//')
ax1.bar(months, organic_coffee_leftover, bottom=np.array(craft_beer_consumption) + np.array(herbal_tea_consumption) + np.array(organic_coffee_consumption), label='Organic Coffee Leftover', color='khaki', alpha=0.6, hatch='//')

ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.tick_params(axis='x', rotation=45)

# Subplot 2: Line plot for efficiency
ax2.plot(craft_beer_efficiency, marker='o', label='Craft Beer Efficiency', color='dodgerblue')
ax2.plot(herbal_tea_efficiency, marker='s', label='Herbal Tea Efficiency', color='mediumseagreen')
ax2.plot(organic_coffee_efficiency, marker='^', label='Organic Coffee Efficiency', color='goldenrod')

ax2.grid(axis='y', linestyle='--', alpha=0.7)
ax2.tick_params(axis='x', rotation=45)

# Adjust layout for better visualization
plt.tight_layout()

# Display the plots
plt.show()
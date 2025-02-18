import matplotlib.pyplot as plt
import numpy as np

months = ["January", "February", "March", "April", "May", "June"]

craft_beer_production = [120, 135, 150, 160, 180, 190]
herbal_tea_production = [110, 130, 125, 140, 145, 155]
organic_coffee_production = [140, 150, 160, 155, 170, 175]

craft_beer_consumption = [100, 120, 130, 140, 160, 170]
herbal_tea_consumption = [90, 110, 115, 120, 130, 145]
organic_coffee_consumption = [130, 145, 150, 140, 160, 165]

craft_beer_leftover = np.array(craft_beer_production) - np.array(craft_beer_consumption)
herbal_tea_leftover = np.array(herbal_tea_production) - np.array(herbal_tea_consumption)
organic_coffee_leftover = np.array(organic_coffee_production) - np.array(organic_coffee_consumption)

craft_beer_efficiency = np.array(craft_beer_consumption) / np.array(craft_beer_production)
herbal_tea_efficiency = np.array(herbal_tea_consumption) / np.array(herbal_tea_production)
organic_coffee_efficiency = np.array(organic_coffee_consumption) / np.array(organic_coffee_production)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

bar_width = 0.6

ax1.bar(months, craft_beer_consumption, label='Craft Beer Consumed', color='#1f77b4', alpha=0.75, edgecolor='black')
ax1.bar(months, herbal_tea_consumption, bottom=craft_beer_consumption, label='Herbal Tea Consumed', color='#ff7f0e', alpha=0.75, edgecolor='black')
ax1.bar(months, organic_coffee_consumption, bottom=np.array(craft_beer_consumption) + np.array(herbal_tea_consumption), label='Organic Coffee Consumed', color='#2ca02c', alpha=0.75, edgecolor='black')

ax1.bar(months, craft_beer_leftover, bottom=craft_beer_consumption, label='Craft Beer Leftover', color='#aec7e8', alpha=0.5, hatch='x', edgecolor='black')
ax1.bar(months, herbal_tea_leftover, bottom=np.array(craft_beer_consumption) + np.array(herbal_tea_consumption), label='Herbal Tea Leftover', color='#ffbb78', alpha=0.5, hatch='x', edgecolor='black')
ax1.bar(months, organic_coffee_leftover, bottom=np.array(craft_beer_consumption) + np.array(herbal_tea_consumption) + np.array(organic_coffee_consumption), label='Organic Coffee Leftover', color='#98df8a', alpha=0.5, hatch='x', edgecolor='black')

ax1.grid(axis='y', linestyle='-.', alpha=0.5)
ax1.tick_params(axis='x', rotation=30)

ax2.plot(craft_beer_efficiency, marker='d', label='Craft Beer Efficiency', color='#1f77b4', linestyle='--')
ax2.plot(herbal_tea_efficiency, marker='*', label='Herbal Tea Efficiency', color='#ff7f0e', linestyle='--')
ax2.plot(organic_coffee_efficiency, marker='x', label='Organic Coffee Efficiency', color='#2ca02c', linestyle='--')

ax2.grid(axis='x', linestyle='-', alpha=0.5)
ax2.tick_params(axis='x', rotation=30)

fig.suptitle("Production and Consumption Analysis", fontsize=16)
ax1.set_title("Monthly Consumption and Leftover")
ax2.set_title("Efficiency Over Time")

ax1.legend(loc='upper left', frameon=False)
ax2.legend(loc='lower left', frameon=False)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()
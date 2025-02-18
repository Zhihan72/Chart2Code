import matplotlib.pyplot as plt
import numpy as np

months = ["January", "February", "March", "April", "May", "June"]

craft_beer_production = [120, 135, 150, 160, 180, 190]
herbal_tea_production = [110, 130, 125, 140, 145, 155]
organic_coffee_production = [140, 150, 160, 155, 170, 175]
vegan_smoothie_production = [100, 120, 140, 150, 160, 170]

craft_beer_consumption = [100, 120, 130, 140, 160, 170]
herbal_tea_consumption = [90, 110, 115, 120, 130, 145]
organic_coffee_consumption = [130, 145, 150, 140, 160, 165]
vegan_smoothie_consumption = [80, 100, 120, 130, 140, 150]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))
bar_width = 0.2
bar_positions = np.arange(len(months))

ax1.bar(bar_positions, craft_beer_consumption, bar_width, label='Craft Beer Consumed', color='#1f77b4', edgecolor='black')
ax1.bar(bar_positions + bar_width, herbal_tea_consumption, bar_width, label='Herbal Tea Consumed', color='#ff7f0e', edgecolor='black')
ax1.bar(bar_positions + 2*bar_width, organic_coffee_consumption, bar_width, label='Organic Coffee Consumed', color='#2ca02c', edgecolor='black')
ax1.bar(bar_positions + 3*bar_width, vegan_smoothie_consumption, bar_width, label='Vegan Smoothie Consumed', color='#d62728', edgecolor='black')

ax1.set_xticks(bar_positions + 1.5*bar_width)
ax1.set_xticklabels(months)
ax1.grid(axis='y', linestyle='-.', alpha=0.5)
ax1.tick_params(axis='x', rotation=30)

craft_beer_efficiency = np.array(craft_beer_consumption) / np.array(craft_beer_production)
herbal_tea_efficiency = np.array(herbal_tea_consumption) / np.array(herbal_tea_production)
organic_coffee_efficiency = np.array(organic_coffee_consumption) / np.array(organic_coffee_production)
vegan_smoothie_efficiency = np.array(vegan_smoothie_consumption) / np.array(vegan_smoothie_production)

ax2.plot(craft_beer_efficiency, marker='d', label='Craft Beer Efficiency', color='#1f77b4', linestyle='--')
ax2.plot(herbal_tea_efficiency, marker='*', label='Herbal Tea Efficiency', color='#ff7f0e', linestyle='--')
ax2.plot(organic_coffee_efficiency, marker='x', label='Organic Coffee Efficiency', color='#2ca02c', linestyle='--')
ax2.plot(vegan_smoothie_efficiency, marker='o', label='Vegan Smoothie Efficiency', color='#d62728', linestyle='--')

ax2.grid(axis='x', linestyle='-', alpha=0.5)
ax2.tick_params(axis='x', rotation=30)

fig.suptitle("Production and Consumption Analysis", fontsize=16)
ax1.set_title("Monthly Consumption")
ax1.set_ylabel("Quantity")
ax2.set_title("Efficiency Over Time")

ax1.legend(loc='upper left', frameon=False)
ax2.legend(loc='lower left', frameon=False)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()
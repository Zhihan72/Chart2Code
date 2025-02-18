import matplotlib.pyplot as plt
import numpy as np

months = ["January", "February", "March", "April", "May", "June"]

craft_beer_production = [120, 135, 150, 160, 180, 190]
herbal_tea_production = [110, 130, 125, 140, 145, 155]
organic_coffee_production = [140, 150, 160, 155, 170, 175]
ginger_ale_production = [100, 110, 120, 130, 150, 160]

craft_beer_consumption = [100, 120, 130, 140, 160, 170]
herbal_tea_consumption = [90, 110, 115, 120, 130, 145]
organic_coffee_consumption = [130, 145, 150, 140, 160, 165]
ginger_ale_consumption = [80, 95, 105, 115, 125, 145]

craft_beer_leftover = np.array(craft_beer_production) - np.array(craft_beer_consumption)
herbal_tea_leftover = np.array(herbal_tea_production) - np.array(herbal_tea_consumption)
organic_coffee_leftover = np.array(organic_coffee_production) - np.array(organic_coffee_consumption)
ginger_ale_leftover = np.array(ginger_ale_production) - np.array(ginger_ale_consumption)

craft_beer_efficiency = np.array(craft_beer_consumption) / np.array(craft_beer_production)
herbal_tea_efficiency = np.array(herbal_tea_consumption) / np.array(herbal_tea_production)
organic_coffee_efficiency = np.array(organic_coffee_consumption) / np.array(organic_coffee_production)
ginger_ale_efficiency = np.array(ginger_ale_consumption) / np.array(ginger_ale_production)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12))
bar_width = 0.6

single_color = 'skyblue'

ax1.bar(months, craft_beer_consumption, bar_width, color=single_color, alpha=0.85)
ax1.bar(months, herbal_tea_consumption, bar_width, bottom=craft_beer_consumption, color=single_color, alpha=0.85)
ax1.bar(months, organic_coffee_consumption, bar_width, bottom=np.array(craft_beer_consumption) + np.array(herbal_tea_consumption), color=single_color, alpha=0.85)
ax1.bar(months, ginger_ale_consumption, bar_width, bottom=np.array(craft_beer_consumption) + np.array(herbal_tea_consumption) + np.array(organic_coffee_consumption), color=single_color, alpha=0.85)

ax1.bar(months, craft_beer_leftover, bar_width, bottom=craft_beer_consumption, color=single_color, alpha=0.6, hatch='//')
ax1.bar(months, herbal_tea_leftover, bar_width, bottom=np.array(craft_beer_consumption) + np.array(herbal_tea_consumption), color=single_color, alpha=0.6, hatch='//')
ax1.bar(months, organic_coffee_leftover, bar_width, bottom=np.array(craft_beer_consumption) + np.array(herbal_tea_consumption) + np.array(organic_coffee_consumption), color=single_color, alpha=0.6, hatch='//')
ax1.bar(months, ginger_ale_leftover, bar_width, bottom=np.array(craft_beer_consumption) + np.array(herbal_tea_consumption) + np.array(organic_coffee_consumption) + np.array(ginger_ale_consumption), color=single_color, alpha=0.6, hatch='//')

ax1.set_title("Artisan Beverage Trends:\nProduction vs. Consumption", fontsize=14, fontweight='bold')
ax1.set_xlabel("Months", fontsize=12)
ax1.set_ylabel("Volume (Liters)", fontsize=12)
ax1.tick_params(axis='x', rotation=45)

ax2.plot(months, craft_beer_efficiency, marker='o', color=single_color)
ax2.plot(months, herbal_tea_efficiency, marker='s', color=single_color)
ax2.plot(months, organic_coffee_efficiency, marker='^', color=single_color)
ax2.plot(months, ginger_ale_efficiency, marker='D', color=single_color)

ax2.set_title("Efficiency Trends:\nConsumption/Production Ratio", fontsize=14, fontweight='bold')
ax2.set_xlabel("Months", fontsize=12)
ax2.set_ylabel("Efficiency Ratio", fontsize=12)
ax2.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
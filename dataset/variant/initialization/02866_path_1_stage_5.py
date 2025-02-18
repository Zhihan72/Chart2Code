import matplotlib.pyplot as plt
import numpy as np

months = ["January", "February", "March", "April", "May", "June"]

craft_beer_production = np.array([120, 135, 150, 160, 180, 190])
herbal_tea_production = np.array([110, 130, 125, 140, 145, 155])
organic_coffee_production = np.array([140, 150, 160, 155, 170, 175])
ginger_ale_production = np.array([100, 110, 120, 130, 150, 160])

craft_beer_consumption = np.array([100, 120, 130, 140, 160, 170])
herbal_tea_consumption = np.array([90, 110, 115, 120, 130, 145])
organic_coffee_consumption = np.array([130, 145, 150, 140, 160, 165])
ginger_ale_consumption = np.array([80, 95, 105, 115, 125, 145])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12))
bar_width = 0.2

# Diverging bar chart
ax1.bar(months, craft_beer_production, bar_width, label='Craft Beer Production', color='blue', bottom=-craft_beer_consumption)
ax1.bar(months, herbal_tea_production, bar_width, label='Herbal Tea Production', color='green', bottom=-herbal_tea_consumption)
ax1.bar(months, organic_coffee_production, bar_width, label='Organic Coffee Production', color='red', bottom=-organic_coffee_consumption)
ax1.bar(months, ginger_ale_production, bar_width, label='Ginger Ale Production', color='purple', bottom=-ginger_ale_consumption)

ax1.bar(months, -craft_beer_consumption, bar_width, color='gray', alpha=0.6, edgecolor='black', bottom=0)
ax1.bar(months, -herbal_tea_consumption, bar_width, color='gray', alpha=0.6, edgecolor='black', bottom=0)
ax1.bar(months, -organic_coffee_consumption, bar_width, color='gray', alpha=0.6, edgecolor='black', bottom=0)
ax1.bar(months, -ginger_ale_consumption, bar_width, color='gray', alpha=0.6, edgecolor='black', bottom=0)

ax1.axhline(0, color='black', linewidth=0.8)
ax1.set_title("Production vs. Consumption Diverging Bar Chart", fontsize=14, fontweight='bold')
ax1.set_xlabel("Months", fontsize=12)
ax1.set_ylabel("Volume (Liters)", fontsize=12)
ax1.tick_params(axis='x', rotation=45)
ax1.legend()

# Keep the efficiency subplot unchanged
craft_beer_efficiency = craft_beer_consumption / craft_beer_production
herbal_tea_efficiency = herbal_tea_consumption / herbal_tea_production
organic_coffee_efficiency = organic_coffee_consumption / organic_coffee_production
ginger_ale_efficiency = ginger_ale_consumption / ginger_ale_production

ax2.plot(months, craft_beer_efficiency, marker='o', label='Craft Beer Efficiency', color='blue')
ax2.plot(months, herbal_tea_efficiency, marker='s', label='Herbal Tea Efficiency', color='green')
ax2.plot(months, organic_coffee_efficiency, marker='^', label='Organic Coffee Efficiency', color='red')
ax2.plot(months, ginger_ale_efficiency, marker='D', label='Ginger Ale Efficiency', color='purple')

ax2.set_title("Efficiency Trends: Consumption/Production Ratio", fontsize=14, fontweight='bold')
ax2.set_xlabel("Months", fontsize=12)
ax2.set_ylabel("Efficiency Ratio", fontsize=12)
ax2.tick_params(axis='x', rotation=45)
ax2.legend()

plt.tight_layout()
plt.show()
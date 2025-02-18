import matplotlib.pyplot as plt
import numpy as np

coffee_brands = ['BrewLove', 'JoltJava', 'CaféCraft', 'BeanBonanza', 'MugMagic', 'EspressoExpress']
market_shares = [40, 25, 20, 10, 4, 1]
explode = [0.1, 0, 0.1, 0.5, 0, 0]
customer_satisfaction = [85, 78, 88, 70, 65, 60]
single_color = '#66B2FF'

fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# Donut Pie Chart for Market Shares
wedges, _ = axs[0].pie(
    market_shares, 
    explode=explode, 
    labels=None, 
    autopct=None, 
    startangle=90, 
    colors=[single_color] * len(market_shares), 
    wedgeprops={'edgecolor': '#4B0082', 'linewidth': 2.0},
    shadow=False
)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
axs[0].add_artist(centre_circle)

# Bar Chart for Customer Satisfaction Rates
bars = axs[1].bar(coffee_brands, customer_satisfaction, color=single_color, edgecolor='#4B0082', hatch='//')

axs[1].set_xticklabels([])  # Removes the x-tick labels
axs[1].set_yticklabels([])  # Removes the y-tick labels
axs[1].yaxis.grid(False)    # Removes the grid lines

plt.tight_layout()

plt.show()
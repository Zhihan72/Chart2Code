import matplotlib.pyplot as plt
import numpy as np

coffee_brands = ['BrewLove', 'JoltJava', 'CaféCraft', 'BeanBonanza', 'MugMagic', 'EspressoExpress']
market_shares = [40, 25, 20, 10, 4, 1]
explode = [0.1, 0, 0.1, 0.5, 0, 0]
customer_satisfaction = [85, 78, 88, 70, 65, 60]
single_color = '#66B2FF'

fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# Donut Pie Chart for Market Shares
wedges, texts, autotexts = axs[0].pie(
    market_shares, 
    explode=explode, 
    labels=coffee_brands, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=[single_color] * len(market_shares), 
    wedgeprops={'edgecolor': '#4B0082', 'linewidth': 2.0},
    shadow=False
)

# Draw a circle at the center of the pie to make it a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
axs[0].add_artist(centre_circle)

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontweight('normal')
    autotext.set_fontsize(10)

axs[0].set_title('Market Share of Coffee Brands\nin Fictional Country (2023)', fontsize=14, fontweight='normal', pad=10)

# Bar Chart for Customer Satisfaction Rates
bars = axs[1].bar(coffee_brands, customer_satisfaction, color=single_color, edgecolor='#4B0082', hatch='//')

for bar in bars:
    height = bar.get_height()
    axs[1].text(bar.get_x() + bar.get_width() / 2, height - 5, f'{height}%',
                ha='center', va='bottom', fontsize=10, fontweight='normal')

axs[1].set_title('Customer Satisfaction Rates\nfor Coffee Brands (2023)', fontsize=14, fontweight='normal', pad=10)
axs[1].set_xlabel('Coffee Brands', fontsize=12)
axs[1].set_ylabel('Satisfaction Rate (%)', fontsize=12)
axs[1].yaxis.grid(True, linestyle='-.', linewidth=0.5, alpha=0.5)

plt.tight_layout()

axs[0].legend(wedges, coffee_brands, title="Coffee Brands", loc="upper right")

plt.show()
import matplotlib.pyplot as plt
import numpy as np

coffee_brands = ['BrewLove', 'JoltJava', 'CaféCraft', 'BeanBonanza', 'MugMagic']
market_shares = [40, 25, 20, 10, 5]
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700']
explode = [0.1, 0, 0, 0, 0]
customer_satisfaction = [85, 78, 88, 70, 65]

fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# Pie Chart for Market Shares
axs[0].pie(
    market_shares, 
    explode=explode, 
    labels=coffee_brands, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    wedgeprops={'edgecolor': 'none'},
    shadow=False
)

axs[0].set_title('Market Share of Coffee Brands\nin Fictional Country (2023)', fontsize=16, fontweight='bold', pad=20)

# Bar Chart for Customer Satisfaction Rates
axs[1].bar(coffee_brands, customer_satisfaction, color=colors, edgecolor='none')

for bar in axs[1].patches:
    height = bar.get_height()
    axs[1].text(bar.get_x() + bar.get_width() / 2, height - 5, f'{height}%', 
                ha='center', va='bottom', fontsize=12, fontweight='bold')

axs[1].set_title('Customer Satisfaction Rates\nfor Coffee Brands (2023)', fontsize=16, fontweight='bold', pad=20)
axs[1].set_xlabel('Coffee Brands', fontsize=14)
axs[1].set_ylabel('Satisfaction Rate (%)', fontsize=14)

# Adjust layout
plt.tight_layout()

plt.show()
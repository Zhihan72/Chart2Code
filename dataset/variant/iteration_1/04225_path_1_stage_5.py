import matplotlib.pyplot as plt

coffee_brands_varied = ['BrewLove', 'BeanBonanza', 'CaféCraft', 'MugMagic', 'JavaJolt', 'EspressoEmporium', 'CaffeineCrush']
market_shares = [5, 10, 20, 25, 30, 5, 5]
customer_satisfaction = [65, 70, 88, 78, 85, 72, 60]
colors = ['#FFD700', '#FFCC99', '#99FF99', '#66B2FF', '#FF9999', '#CCCCFF', '#FFB6C1']

fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# Swap the pie chart with the bar chart

# Updated bar chart now on the left
axs[0].bar(coffee_brands_varied, customer_satisfaction, color=colors, edgecolor='none')

for bar in axs[0].patches:
    height = bar.get_height()
    axs[0].text(bar.get_x() + bar.get_width() / 2, height - 5, f'{height}%', 
                ha='center', va='bottom', fontsize=12, fontweight='bold')

axs[0].set_title('Surveyed Happiness Metrics\nfor Coffee Producers (2023)', fontsize=16, fontweight='bold', pad=20)
axs[0].set_xlabel('Espresso Makers', fontsize=14)
axs[0].set_ylabel('Happiness Level (%)', fontsize=14)

# Updated pie chart now on the right
axs[1].pie(
    market_shares, 
    explode=[0, 0, 0, 0, 0.1, 0, 0], 
    labels=coffee_brands_varied, 
    autopct='%1.1f%%', 
    startangle=120, 
    colors=colors, 
    wedgeprops={'edgecolor': 'none'},
    shadow=False
)

axs[1].set_title('Fictional Market Division of Espresso Producers\nby 2023', fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()
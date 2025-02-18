import matplotlib.pyplot as plt
import numpy as np

# Backstory: The chart represents the breakdown of market shares held by popular coffee brands in a fictional country in 2023.
# Additionally, we delve into the customer satisfaction rates of these brands to provide more insight.

# Define coffee brands and their respective market shares in percentage
coffee_brands = ['BrewLove', 'JoltJava', 'CaféCraft', 'BeanBonanza', 'MugMagic']
market_shares = [40, 25, 20, 10, 5]

# Colors for the pie chart slices
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700']

# Explode the largest slice (BrewLove) for emphasis
explode = [0.1, 0, 0, 0, 0]

# Additional data for customer satisfaction rates of these coffee brands
customer_satisfaction = [85, 78, 88, 70, 65]

# Create a figure with 1 row and 2 columns of subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# Pie Chart for Market Shares
wedges, texts, autotexts = axs[0].pie(
    market_shares, 
    explode=explode, 
    labels=coffee_brands, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    wedgeprops={'edgecolor': 'black', 'linewidth': 1.5},
    shadow=True
)

# Adjust text size and color
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

axs[0].set_title('Market Share of Coffee Brands\nin Fictional Country (2023)', fontsize=16, fontweight='bold', pad=20)

# Bar Chart for Customer Satisfaction Rates
bars = axs[1].bar(coffee_brands, customer_satisfaction, color=colors, edgecolor='black')

# Adding value labels to bars
for bar in bars:
    height = bar.get_height()
    axs[1].text(bar.get_x() + bar.get_width() / 2, height - 5, f'{height}%', 
                ha='center', va='bottom', fontsize=12, fontweight='bold')

axs[1].set_title('Customer Satisfaction Rates\nfor Coffee Brands (2023)', fontsize=16, fontweight='bold', pad=20)
axs[1].set_xlabel('Coffee Brands', fontsize=14)
axs[1].set_ylabel('Satisfaction Rate (%)', fontsize=14)
axs[1].yaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to ensure no overlaps
plt.tight_layout()

# Add legends
axs[0].legend(wedges, coffee_brands, title="Coffee Brands", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Show the plot
plt.show()
import matplotlib.pyplot as plt
import squarify

sectors = ['Streaming', 'Gaming', 'Music', 'E-books', 'VR', 'Podcasts', 'AR']
market_share_2023 = [35, 30, 15, 10, 10, 5, 3]
growth_rates_2024 = [5, 8, 3, 2, 10, 6, 12]
new_colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c2f0c2']

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

# Horizontal bar chart for projected growth in 2024 (left)
axes[0].barh(sectors, growth_rates_2024, color=new_colors, alpha=0.8)
axes[0].set_title("Growth 2024", fontsize=16, fontweight='bold', pad=15)
axes[0].set_xlabel("Growth (%)", fontsize=12)
axes[0].set_xlim(0, max(growth_rates_2024) + 5)

# Annotate each bar
for i, v in enumerate(growth_rates_2024):
    axes[0].text(v + 0.5, i, f"{v}%", color='black', va='center', fontweight='bold')

# Treemap for market share 2023 (right)
axes[1].set_title("Market Share 2023", fontsize=16, fontweight='bold', pad=15)
squarify.plot(sizes=market_share_2023, label=[f"{sector}\n{share}%" for sector, share in zip(sectors, market_share_2023)], 
              color=new_colors, alpha=0.8, text_kwargs={'fontsize': 10, 'weight': 'bold', 'color': 'white'}, ax=axes[1])
axes[1].axis('off')

plt.tight_layout()
plt.show()
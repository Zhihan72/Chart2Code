import matplotlib.pyplot as plt
import squarify

# Market share data for digital entertainment sectors with altered content
sectors = ['Virtual Reality', 'Online Gaming', 'E-books', 'Streaming Services', 'Digital Music']
market_share_2023 = [30, 15, 10, 10, 35]

# Altered growth rates for 2024
growth_rates_2024 = [8, 10, 3, 2, 5]

# Altered color palette
new_colors = ['#20b2aa', '#ff6347', '#778899', '#4682b4', '#ffa07a']

# Sort data for bar chart based on growth rate
sorted_indices = sorted(range(len(growth_rates_2024)), key=lambda i: growth_rates_2024[i], reverse=True)
sorted_sectors = [sectors[i] for i in sorted_indices]
sorted_growth_rates_2024 = [growth_rates_2024[i] for i in sorted_indices]
sorted_colors = [new_colors[i] for i in sorted_indices]

# Create the figure and subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 8), gridspec_kw={'wspace': 0.5})

# Treemap for market share 2023
axes[0].set_title("Digital Sector Dominance in 2023", fontsize=16, fontweight='bold', pad=20)
squarify.plot(sizes=market_share_2023, label=[f"{sector}\n{share}%" for sector, share in zip(sectors, market_share_2023)], 
              color=new_colors, alpha=0.8, text_kwargs={'fontsize': 10, 'weight': 'bold', 'color': 'white'}, ax=axes[0])
axes[0].axis('off')
axes[0].spines['top'].set_visible(False)

# Sorted bar chart for projected growth in 2024
axes[1].barh(sorted_sectors, sorted_growth_rates_2024, color=sorted_colors, alpha=0.8, edgecolor='black', linestyle='--')
axes[1].set_title("Future Growth Trends: 2024", fontsize=16, fontweight='bold', pad=20)
axes[1].set_xlabel("Percentage Growth (%)", fontsize=12)
axes[1].set_xlim(0, max(growth_rates_2024) + 5)
for i, v in enumerate(sorted_growth_rates_2024):
    axes[1].text(v + 0.5, i, f"{v}%", color='black', va='center', fontweight='bold')

axes[1].grid(axis='x', linestyle='-.', color='gray', alpha=0.7)
axes[1].legend(['Growth Rate'], loc='lower right', frameon=False)

plt.tight_layout()
plt.show()
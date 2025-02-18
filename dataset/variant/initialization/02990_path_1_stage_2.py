import matplotlib.pyplot as plt
import squarify

# Market share data for digital entertainment sectors in 2023
sectors = ['Streaming Services', 'Online Gaming', 'Digital Music', 'E-books', 'Virtual Reality']
market_share_2023 = [35, 30, 15, 10, 10]

# Projected growth rates for 2024 (in percentage)
growth_rates_2024 = [5, 8, 3, 2, 10]

# New color palette for sectors
new_colors = ['#ffa07a', '#20b2aa', '#778899', '#ff6347', '#4682b4']

# Sort the data for the bar chart in descending order of growth rate
sorted_indices = sorted(range(len(growth_rates_2024)), key=lambda i: growth_rates_2024[i], reverse=True)
sorted_sectors = [sectors[i] for i in sorted_indices]
sorted_growth_rates_2024 = [growth_rates_2024[i] for i in sorted_indices]
sorted_colors = [new_colors[i] for i in sorted_indices]

# Create the figure and subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

# Treemap for market share 2023
axes[0].set_title("Market Share in 2023 by Sector", fontsize=16, fontweight='bold', pad=15)
squarify.plot(sizes=market_share_2023, label=[f"{sector}\n{share}%" for sector, share in zip(sectors, market_share_2023)], 
              color=new_colors, alpha=0.8, text_kwargs={'fontsize': 10, 'weight': 'bold', 'color': 'white'}, ax=axes[0])
axes[0].axis('off')

# Sorted bar chart for projected growth in 2024
axes[1].barh(sorted_sectors, sorted_growth_rates_2024, color=sorted_colors, alpha=0.8)
axes[1].set_title("Projected Growth Rate for 2024", fontsize=16, fontweight='bold', pad=15)
axes[1].set_xlabel("Growth Rate (%)", fontsize=12)
axes[1].set_xlim(0, max(growth_rates_2024) + 5)
for i, v in enumerate(sorted_growth_rates_2024):
    axes[1].text(v + 0.5, i, f"{v}%", color='black', va='center', fontweight='bold')

# General layout adjustments
plt.tight_layout()

# Display the plot
plt.show()
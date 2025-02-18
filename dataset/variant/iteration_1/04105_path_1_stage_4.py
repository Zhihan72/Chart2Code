import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2025, 2051)

num_space_tourists = [
    0, 1, 5, 12, 22, 36, 50, 65, 80, 100, 120, 140, 
    165, 190, 220, 250, 285, 320, 360, 400, 450, 
    500, 560, 620, 690, 770 
]

avg_ticket_price = [
    500, 450, 420, 390, 370, 350, 340, 330, 320, 315, 
    310, 305, 300, 295, 290, 285, 280, 275, 270, 
    265, 260, 255, 250, 245, 240, 235
]

num_companies = [
    2, 3, 5, 7, 10, 14, 18, 22, 26, 30, 35, 40, 
    45, 50, 55, 60, 65, 70, 75, 80, 85, 
    90, 95, 100, 105, 110 
]

fig, ax1 = plt.subplots(figsize=(12, 8))

# Altering color and marker styles
color_tourists = 'tab:red'
marker_tourists = 'x'
ax1.set_xlabel('Year', fontsize=12, color='purple')  # Random color change for axes label
ax1.set_ylabel('Tourists', color=color_tourists)
ax1.plot(years, num_space_tourists, color=color_tourists, linewidth=2.0, linestyle='-.', marker=marker_tourists)  # Changed linestyle
ax1.tick_params(axis='y', labelcolor=color_tourists)

# Changes in title font
ax1.set_title('Space Tourism (2025-2050)', fontsize=18, fontweight='normal', pad=15, color='darkgreen')  # Changed color and font weight
ax1.grid(color='lightblue', linestyle='-', linewidth=1.0, alpha=0.3)  # Changed grid style and color

milestones_tourists = {
    2030: 'Space Hotel Opens',
    2045: 'Interplanetary Tours'
}
for year, annotation in milestones_tourists.items():
    idx = years.tolist().index(year)
    tourists_val = num_space_tourists[idx]
    ax1.annotate(annotation, xy=(year, tourists_val), xytext=(year, tourists_val + 50),
                 arrowprops=dict(facecolor=color_tourists, arrowstyle='->'), fontsize=11, ha='right', color=color_tourists)

# Removed redundant plot line
# ax1.plot(years, num_space_tourists, linestyle='--', linewidth=1.5, alpha=0.7, color=color)

# Change line styles and colors for second y-axis
ax2 = ax1.twinx()
color_prices = 'tab:green'
marker_prices = '*'
ax2.set_ylabel('Price (M USD)', color=color_prices)
ax2.plot(years, avg_ticket_price, color=color_prices, linewidth=3.0, linestyle=':', marker=marker_prices)  # Changed linestyle and linewidth
ax2.tick_params(axis='y', labelcolor=color_prices)

milestones_prices = {
    2035: 'Tech Advances',
    2040: 'Mass Production'
}
for year, annotation in milestones_prices.items():
    idx = years.tolist().index(year)
    price_val = avg_ticket_price[idx]
    ax2.annotate(annotation, xy=(year, price_val), xytext=(year, price_val + 30),
                 arrowprops=dict(facecolor=color_prices, arrowstyle='->'), fontsize=12, ha='left', color=color_prices)

# Change line styles and colors for third y-axis
ax3 = ax1.twinx() 
ax3.spines['right'].set_position(('outward', 80))  # Altered position of the axis
color_companies = 'tab:orange'
marker_companies = 'v'
ax3.set_ylabel('Number of Companies', color=color_companies)
ax3.plot(years, num_companies, color=color_companies, linewidth=2.5, linestyle='-', marker=marker_companies)  # Changed marker
ax3.tick_params(axis='y', labelcolor=color_companies)

fig.tight_layout()
plt.show()
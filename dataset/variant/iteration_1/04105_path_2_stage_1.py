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

# Create a plot with y-axes
fig, ax1 = plt.subplots(figsize=(12, 8))

color1 = 'tab:blue'
ax1.set_xlabel('Yr')
ax1.set_ylabel('Tourists', color=color1)
ax1.plot(years, num_space_tourists, color=color1, linewidth=2.5, marker='o', label='Tourists')
ax1.tick_params(axis='y', labelcolor=color1)

# Shortened title and grid
ax1.set_title('Space Tourism (2025-2050)', fontsize=14, fontweight='bold', pad=10)
ax1.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

# Shortened annotations
milestones_tourists = {
    2030: 'First Hotel',
    2045: 'Interplanetary Tours'
}
for year, annotation in milestones_tourists.items():
    idx = years.tolist().index(year)
    tourists_val = num_space_tourists[idx]
    ax1.annotate(annotation, xy=(year, tourists_val), xytext=(year, tourists_val + 50),
                 arrowprops=dict(facecolor='tab:blue', arrowstyle='->'), fontsize=10, ha='center', color='tab:blue')

ax1.plot(years, num_space_tourists, linestyle='--', linewidth=1.5, alpha=0.7, color=color1)

ax2 = ax1.twinx()
color2 = 'tab:red'
ax2.set_ylabel('Price (Million USD)', color=color2)
ax2.plot(years, avg_ticket_price, color=color2, linewidth=2.5, linestyle='dashed', marker='s', label='Price')
ax2.tick_params(axis='y', labelcolor=color2)

milestones_prices = {
    2035: 'Tech Advances',
    2040: 'Mass Manuf.'
}
for year, annotation in milestones_prices.items():
    idx = years.tolist().index(year)
    price_val = avg_ticket_price[idx]
    ax2.annotate(annotation, xy=(year, price_val), xytext=(year, price_val + 30),
                 arrowprops=dict(facecolor='tab:red', arrowstyle='->'), fontsize=10, ha='center', color='tab:red')

fig.tight_layout()
plt.show()
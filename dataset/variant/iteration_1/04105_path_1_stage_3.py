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

color = 'tab:blue'
ax1.set_xlabel('Year')
ax1.set_ylabel('Tourists', color=color)
ax1.plot(years, num_space_tourists, color=color, linewidth=2.5, marker='o')
ax1.tick_params(axis='y', labelcolor=color)

ax1.set_title('Space Tourism (2025-2050)', fontsize=16, fontweight='bold', pad=20)
ax1.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

milestones_tourists = {
    2030: 'Space Hotel Opens',
    2045: 'Interplanetary Tours'
}
for year, annotation in milestones_tourists.items():
    idx = years.tolist().index(year)
    tourists_val = num_space_tourists[idx]
    ax1.annotate(annotation, xy=(year, tourists_val), xytext=(year, tourists_val + 50),
                 arrowprops=dict(facecolor=color, arrowstyle='->'), fontsize=10, ha='center', color=color)

ax1.plot(years, num_space_tourists, linestyle='--', linewidth=1.5, alpha=0.7, color=color)

ax2 = ax1.twinx()
ax2.set_ylabel('Price (M USD)', color=color)
ax2.plot(years, avg_ticket_price, color=color, linewidth=2.5, linestyle='dashed', marker='s')
ax2.tick_params(axis='y', labelcolor=color)

milestones_prices = {
    2035: 'Tech Advances',
    2040: 'Mass Production'
}
for year, annotation in milestones_prices.items():
    idx = years.tolist().index(year)
    price_val = avg_ticket_price[idx]
    ax2.annotate(annotation, xy=(year, price_val), xytext=(year, price_val + 30),
                 arrowprops=dict(facecolor=color, arrowstyle='->'), fontsize=10, ha='center', color=color)

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))  
ax3.set_ylabel('Number of Companies', color=color)
ax3.plot(years, num_companies, color=color, linewidth=2.5, linestyle='dotted', marker='^')
ax3.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Years for the data
years = np.arange(2010, 2026)

# Stock price data (in USD) for tech companies
company_a = np.array([100, 120, 150, 140, 130, 160, 190, 210, 230, 220, 250, 270, 290, 285, 300, 310])
company_b = np.array([50, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130])
company_c = np.array([80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380])
company_d = np.array([200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50])
company_e = np.array([300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450])

# Create the figure and axis for the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Line plots for each company's stock prices
ax.plot(years, company_a, marker='o', linestyle='-', color='#FF5733', label='Alpha Corp')
ax.plot(years, company_b, marker='v', linestyle='--', color='#33FF57', label='Beta Inc')
ax.plot(years, company_c, marker='s', linestyle='-.', color='#3357FF', label='Gamma LLC')
ax.plot(years, company_d, marker='D', linestyle=':', color='#FF33A8', label='Delta Group')
ax.plot(years, company_e, marker='^', linestyle='-', color='#FFC300', label='Epsilon Ltd')

# Titles, labels and legends
ax.set_title('Evolution of Tech Enterprises\nValue Fluctuations 2010-2025', fontsize=16, weight='bold')
ax.set_xlabel('Calendar Year', fontsize=14)
ax.set_ylabel('Valuation in USD', fontsize=14)
ax.legend(title='Corporations', fontsize=12, title_fontsize='13')
ax.grid(True)

# Annotating the highest and lowest points for each company
def annotate_extreme_points(years, prices, ax, color):
    max_idx = np.argmax(prices)
    min_idx = np.argmin(prices)
    ax.annotate(f'Peak: {prices[max_idx]} USD', xy=(years[max_idx], prices[max_idx]), xytext=(years[max_idx]+0.5, prices[max_idx]+5),
                arrowprops=dict(facecolor=color, edgecolor='white'), fontsize=9, color=color)
    ax.annotate(f'Dip: {prices[min_idx]} USD', xy=(years[min_idx], prices[min_idx]), xytext=(years[min_idx]+0.5, prices[min_idx]-10),
                arrowprops=dict(facecolor=color, edgecolor='white'), fontsize=9, color=color)

# Annotate extreme points for each company
annotate_extreme_points(years, company_a, ax, '#FF5733')
annotate_extreme_points(years, company_b, ax, '#33FF57')
annotate_extreme_points(years, company_c, ax, '#3357FF')
annotate_extreme_points(years, company_d, ax, '#FF33A8')
annotate_extreme_points(years, company_e, ax, '#FFC300')

# Adjust layout to prevent clipping
plt.tight_layout()

# Show the plot
plt.show()
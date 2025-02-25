import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

# Hypothetical data
gdp_growth = np.array([2.3, 2.6, 2.7, 2.9, 3.0, 3.2, 3.1, 2.8, 2.5, 2.0, 1.8])
unemployment_rate = np.array([7.8, 7.5, 7.2, 7.0, 6.8, 6.7, 6.6, 6.5, 6.3, 6.2, 6.1])
inflation_rate = np.array([1.5, 1.7, 1.8, 2.0, 2.2, 2.5, 2.4, 2.3, 2.1, 1.9, 1.8])
consumer_confidence = np.array([80, 82, 84, 83, 85, 87, 88, 89, 87, 86, 85])  # Consumer Confidence Index
trade_balance = np.array([-50, -48, -45, -44, -46, -43, -42, -40, -41, -39, -38])  # Trade Balance in billion USD

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(years, gdp_growth, label='GDP (%)', color='green', marker='o', linestyle='-', linewidth=2, markersize=6)
ax1.plot(years, unemployment_rate, label='Unemp. (%)', color='blue', marker='s', linestyle='-', linewidth=2, markersize=6)
ax1.plot(years, inflation_rate, label='Inflation (%)', color='red', marker='^', linestyle='-', linewidth=2, markersize=6)
ax1.plot(years, consumer_confidence, label='Cons. Conf.', color='purple', marker='d', linestyle='-', linewidth=2, markersize=6)

# Secondary y-axis for Trade Balance
ax2 = ax1.twinx()
ax2.plot(years, trade_balance, label='Trade Balance', color='orange', marker='x', linestyle='-', linewidth=2, markersize=6)
ax2.set_ylabel("Balance (Billion USD)", fontsize=12, color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

ax1.set_title("Imaginaryland Economy (2010-20)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Percentage (%)", fontsize=12)

key_events = {
    2012: ("Fiscal\nOverhaul", 8.1, 8.0),
    2015: ("Energy\nCrisis", 7.0, 1.5),
    2018: ("Tech\nBoom", 6.6, 2.4),
}

for year, (event, y_gdp, y_unemployment) in key_events.items():
    ax1.annotate(event, xy=(year, y_gdp),
                 xytext=(year, y_gdp + 0.5),
                 textcoords='data',
                 arrowprops=dict(arrowstyle='->', color='darkgrey'),
                 ha='center', fontsize=10, color='black')

ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax1.legend(loc='upper left', fontsize=12)
ax2.legend(loc='upper right', fontsize=12)

ax1.set_xticks(years)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
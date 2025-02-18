import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2023)

market_share_innovators = np.array([15, 17, 20, 17, 18, 22, 21, 22, 24, 26])
market_share_visionary = np.array([25, 27, 23, 25, 24, 20, 19, 18, 16, 14])
market_share_pioneer = np.array([10, 13, 15, 20, 18, 22, 23, 23, 24, 26])
market_share_techgiant = np.array([30, 29, 28, 30, 29, 28, 30, 31, 32, 33])
market_share_startups = np.array([5, 6, 8, 8, 11, 8, 7, 6, 4, 3])

forecast_years = np.array([2023, 2024])
forecast_innovators = np.array([27, 29])
forecast_visionary = np.array([13, 12])
forecast_pioneer = np.array([27, 29])
forecast_techgiant = np.array([34, 35])
forecast_startups = np.array([4, 5])

fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(years, market_share_innovators, marker='o', linestyle='-', color='tab:green', alpha=0.85)
ax.plot(years, market_share_visionary, marker='s', linestyle='-', color='tab:red', alpha=0.85)
ax.plot(years, market_share_pioneer, marker='^', linestyle='-', color='tab:blue', alpha=0.85)
ax.plot(years, market_share_techgiant, marker='x', linestyle='-', color='tab:orange', alpha=0.85)
ax.plot(years, market_share_startups, marker='d', linestyle='-', color='tab:purple', alpha=0.85)

ax.plot(forecast_years, forecast_innovators, marker='o', linestyle='--', color='tab:green', alpha=0.7)
ax.plot(forecast_years, forecast_visionary, marker='s', linestyle='--', color='tab:red', alpha=0.7)
ax.plot(forecast_years, forecast_pioneer, marker='^', linestyle='--', color='tab:blue', alpha=0.7)
ax.plot(forecast_years, forecast_techgiant, marker='x', linestyle='--', color='tab:orange', alpha=0.7)
ax.plot(forecast_years, forecast_startups, marker='d', linestyle='--', color='tab:purple', alpha=0.7)

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Market Share (%)', fontsize=12)
ax.set_title('Market Share Trends in Techlandia (2013-2024)', fontsize=14, fontweight='bold', loc='center', wrap=True)

plt.tight_layout()
plt.show()
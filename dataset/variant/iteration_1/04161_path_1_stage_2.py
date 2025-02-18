import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2013, 2023)

# Market share data for each company (in percentage)
market_share_innovators = np.array([15, 17, 20, 17, 18, 22, 21, 22, 24, 26])
market_share_visionary = np.array([25, 27, 23, 25, 24, 20, 19, 18, 16, 14])
market_share_pioneer = np.array([10, 13, 15, 20, 18, 22, 23, 23, 24, 26])
market_share_challengers = np.array([5, 6, 7, 8, 9, 13, 14, 16, 15, 17])

# Forecasting future market shares for each company
forecast_years = np.array([2023, 2024])
forecast_innovators = np.array([27, 29])
forecast_visionary = np.array([13, 12])
forecast_pioneer = np.array([27, 29])
forecast_challengers = np.array([18, 20])

fig, ax = plt.subplots(figsize=(14, 7))

# Plot actual market share data
ax.plot(years, market_share_innovators, marker='o', linestyle='-', color='tab:blue', alpha=0.85)
ax.plot(years, market_share_visionary, marker='s', linestyle='-', color='tab:green', alpha=0.85)
ax.plot(years, market_share_pioneer, marker='^', linestyle='-', color='tab:red', alpha=0.85)
ax.plot(years, market_share_challengers, marker='d', linestyle='-', color='tab:purple', alpha=0.85)

# Plot forecast market share data
ax.plot(forecast_years, forecast_innovators, marker='o', linestyle='--', color='tab:blue', alpha=0.7)
ax.plot(forecast_years, forecast_visionary, marker='s', linestyle='--', color='tab:green', alpha=0.7)
ax.plot(forecast_years, forecast_pioneer, marker='^', linestyle='--', color='tab:red', alpha=0.7)
ax.plot(forecast_years, forecast_challengers, marker='d', linestyle='--', color='tab:purple', alpha=0.7)

# Customize chart
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Market Share (%)', fontsize=12)
ax.set_title('Market Share Trends in Techlandia (2013-2024)\nFocus on Key Players in the Software Industry', fontsize=14, fontweight='bold', loc='center')

# Display the plot
plt.show()
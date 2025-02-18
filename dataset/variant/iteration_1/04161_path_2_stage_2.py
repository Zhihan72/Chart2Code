import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2013, 2023)

# Original market share data for each company (in percentage)
market_share_innovators = np.array([15, 17, 20, 17, 18, 22, 21, 22, 24, 26])
market_share_visionary = np.array([25, 27, 23, 25, 24, 20, 19, 18, 16, 14])
market_share_pioneer = np.array([10, 13, 15, 20, 18, 22, 23, 23, 24, 26])

# Adding new company data series
market_share_techgiant = np.array([30, 29, 28, 30, 29, 28, 30, 31, 32, 33])
market_share_startups = np.array([5, 6, 8, 8, 11, 8, 7, 6, 4, 3])

# Forecasting future market shares for each company
forecast_years = np.array([2023, 2024])
forecast_innovators = np.array([27, 29])
forecast_visionary = np.array([13, 12])
forecast_pioneer = np.array([27, 29])
forecast_techgiant = np.array([34, 35])
forecast_startups = np.array([4, 5])

# Combine real data with forecasting data
all_years = np.concatenate([years, forecast_years])
all_innovators = np.concatenate([market_share_innovators, forecast_innovators])
all_visionary = np.concatenate([market_share_visionary, forecast_visionary])
all_pioneer = np.concatenate([market_share_pioneer, forecast_pioneer])
all_techgiant = np.concatenate([market_share_techgiant, forecast_techgiant])
all_startups = np.concatenate([market_share_startups, forecast_startups])

# Plotting
fig, ax = plt.subplots(figsize=(14, 7))

# Plot actual market share data with shuffled colors
ax.plot(years, market_share_innovators, label='Innovators Inc.', marker='o', linestyle='-', color='tab:green', alpha=0.85)
ax.plot(years, market_share_visionary, label='Visionary Ventures', marker='s', linestyle='-', color='tab:red', alpha=0.85)
ax.plot(years, market_share_pioneer, label='Pioneer Platforms', marker='^', linestyle='-', color='tab:blue', alpha=0.85)
ax.plot(years, market_share_techgiant, label='Tech Giant Corp.', marker='x', linestyle='-', color='tab:orange', alpha=0.85)
ax.plot(years, market_share_startups, label='Emerging Startups', marker='d', linestyle='-', color='tab:purple', alpha=0.85)

# Plot forecast market share data with a dashed style
ax.plot(forecast_years, forecast_innovators, marker='o', linestyle='--', color='tab:green', alpha=0.7)
ax.plot(forecast_years, forecast_visionary, marker='s', linestyle='--', color='tab:red', alpha=0.7)
ax.plot(forecast_years, forecast_pioneer, marker='^', linestyle='--', color='tab:blue', alpha=0.7)
ax.plot(forecast_years, forecast_techgiant, marker='x', linestyle='--', color='tab:orange', alpha=0.7)
ax.plot(forecast_years, forecast_startups, marker='d', linestyle='--', color='tab:purple', alpha=0.7)

# Customize chart
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Market Share (%)', fontsize=12)
ax.set_title('Market Share Trends in Techlandia (2013-2024)', fontsize=14, fontweight='bold', loc='center', wrap=True)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(title='Companies', loc='upper left', fontsize=10)

# Highlight COVID-19 period (2020-2021) with a vertical shading
ax.axvspan(2020, 2021, color='gray', alpha=0.2, label='COVID-19 Impact Period')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()
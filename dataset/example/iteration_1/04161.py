import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# In the fictional realm of Techlandia, three rival tech companies - Innovators Inc., Visionary Ventures, and Pioneer Platforms - 
# have been competing in market share dominance in the software industry for the past decade. 
# Below is a line chart delineating each company's market share from 2013 to 2022, highlighting trends and movements over the years.

# Define the years
years = np.arange(2013, 2023)

# Market share data for each company (in percentage)
market_share_innovators = np.array([15, 17, 20, 17, 18, 22, 21, 22, 24, 26])
market_share_visionary = np.array([25, 27, 23, 25, 24, 20, 19, 18, 16, 14])
market_share_pioneer = np.array([10, 13, 15, 20, 18, 22, 23, 23, 24, 26])

# Forecasting future market shares for each company (next two years as an example)
forecast_years = np.array([2023, 2024])
forecast_innovators = np.array([27, 29])
forecast_visionary = np.array([13, 12])
forecast_pioneer = np.array([27, 29])

# Combine real data with forecasting data
all_years = np.concatenate([years, forecast_years])
all_innovators = np.concatenate([market_share_innovators, forecast_innovators])
all_visionary = np.concatenate([market_share_visionary, forecast_visionary])
all_pioneer = np.concatenate([market_share_pioneer, forecast_pioneer])

# Plotting
fig, ax = plt.subplots(figsize=(14, 7))

# Plot actual market share data
ax.plot(years, market_share_innovators, label='Innovators Inc.', marker='o', linestyle='-', color='tab:blue', alpha=0.85)
ax.plot(years, market_share_visionary, label='Visionary Ventures', marker='s', linestyle='-', color='tab:green', alpha=0.85)
ax.plot(years, market_share_pioneer, label='Pioneer Platforms', marker='^', linestyle='-', color='tab:red', alpha=0.85)

# Plot forecast market share data with a dashed style
ax.plot(forecast_years, forecast_innovators, marker='o', linestyle='--', color='tab:blue', alpha=0.7)
ax.plot(forecast_years, forecast_visionary, marker='s', linestyle='--', color='tab:green', alpha=0.7)
ax.plot(forecast_years, forecast_pioneer, marker='^', linestyle='--', color='tab:red', alpha=0.7)

# Customize chart
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Market Share (%)', fontsize=12)
ax.set_title('Market Share Trends in Techlandia (2013-2024)\nFocus on Key Players in the Software Industry', fontsize=14, fontweight='bold', loc='center', wrap=True)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(title='Companies', loc='upper left', fontsize=10)

# Highlight COVID-19 period (2020-2021) with a vertical shading
ax.axvspan(2020, 2021, color='gray', alpha=0.2, label='COVID-19 Impact Period')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()
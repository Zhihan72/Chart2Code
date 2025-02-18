import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking the growth of different tech stocks over a decade (2010-2020)
# Companies: TechCorp, InnovateInc, FutureSystems

# Define years for the timeline
years = np.arange(2010, 2021)

# Stock prices over the years for each company
techcorp_stocks = [120, 135, 150, 180, 210, 250, 300, 350, 400, 450, 500]
innovateinc_stocks = [80, 85, 100, 140, 180, 220, 280, 330, 420, 520, 650]
futuresystems_stocks = [60, 70, 90, 110, 140, 170, 210, 260, 320, 400, 490]

# Create the plot
plt.figure(figsize=(12, 8))

# Plot each company's stock data
plt.plot(years, techcorp_stocks, label='TechCorp', color='blue', marker='s', linewidth=2, linestyle='-')
plt.plot(years, innovateinc_stocks, label='InnovateInc', color='green', marker='d', linewidth=2, linestyle='--')
plt.plot(years, futuresystems_stocks, label='FutureSystems', color='red', marker='o', linewidth=2, linestyle='-.')

# Annotate some key points
for year, price in zip([2010, 2015, 2020], [120, 250, 500]):
    plt.annotate(f'{price}', (year, price), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=10, color='blue', backgroundcolor='white', alpha=0.8)
for year, price in zip([2010, 2015, 2020], [80, 220, 650]):
    plt.annotate(f'{price}', (year, price), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=10, color='green', backgroundcolor='white', alpha=0.8)
for year, price in zip([2010, 2015, 2020], [60, 170, 490]):
    plt.annotate(f'{price}', (year, price), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=10, color='red', backgroundcolor='white', alpha=0.8)

# Add a multi-line title and axis labels
plt.title('Tech Boom:\nStock Prices of Major Tech Companies (2010-2020)', fontsize=18, fontweight='bold', loc='center')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Stock Price (USD)', fontsize=14)

# Set y-axis range and add gridlines
plt.ylim(0, 700)
plt.grid(True, linestyle='--', alpha=0.6)

# Add a legend, positioned to avoid data occlusion
plt.legend(title='Companies', loc='upper left', fontsize=12)

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()
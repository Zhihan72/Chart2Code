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
ax.plot(years, company_a, marker='o', linestyle='-', color='#FF5733')
ax.plot(years, company_b, marker='v', linestyle='--', color='#33FF57')
ax.plot(years, company_c, marker='s', linestyle='-.', color='#3357FF')
ax.plot(years, company_d, marker='D', linestyle=':', color='#FF33A8')
ax.plot(years, company_e, marker='^', linestyle='-', color='#FFC300')

# Remove titles, labels, legends, and text annotations
ax.grid(True)

# Adjust layout to prevent clipping
plt.tight_layout()

# Show the plot
plt.show()
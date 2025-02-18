import matplotlib.pyplot as plt
import numpy as np

# **Backstory:**
# The chart shows the hypothetical change in market share among different types of ice cream flavors over the years 2015-2025.
# The data will represent the percentage of market share held by each flavor.

# Define the years
years = np.arange(2015, 2026)

# Market shares of different ice cream flavors over the years
vanilla = np.array([30, 30, 29, 28, 27, 25, 24, 23, 22, 20, 18])
chocolate = np.array([20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
strawberry = np.array([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10])
mint = np.array([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
cookie_dough = np.array([10, 10, 11, 12, 11, 12, 13, 14, 14, 16, 17])
others = np.array([10, 10, 10, 10, 12, 13, 13, 13, 14, 14, 15])

# Create the area plot
fig, ax = plt.subplots(figsize=(14, 7))

ax.stackplot(years, vanilla, chocolate, strawberry, mint, cookie_dough, others,
             labels=['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Cookie Dough', 'Others'],
             colors=['#f7d8ba', '#8b4513', '#ff6f61', '#98ff98', '#ddadaf', '#c2c2c2'], alpha=0.75)

# Customizing the plot
ax.set_title("Ice Cream Market Share Trends\n (2015 - 2025)", fontsize=16, fontweight='bold', family='serif')
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Market Share (%)", fontsize=14)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 101, 10))

# Add a legend
ax.legend(loc='upper left', title="Ice Cream Flavors", fontsize=12)

# Add gridlines
ax.grid(True, linestyle='--', alpha=0.6)

# Highlight the year 2020 with an annotation
ax.annotate('Marked shift in market share trend (2020)', xy=(2020, 50),
            xytext=(2022, 60), arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12,
            bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='white'))

# Ensure everything fits well within the plot
plt.tight_layout()

# Display the plot
plt.show()
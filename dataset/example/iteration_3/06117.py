import matplotlib.pyplot as plt
import numpy as np

# Backstory: Analyzing the Shift in Consumer Snack Preferences Over the Decade
# Data inspired by a hypothetical market research study on 5 most popular snack types each year over a span of 10 years.

# Years
years = np.array(['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'])

# Snack types and their annual popularity (percent of total consumption)
chip_popularity = np.array([25, 26, 28, 27, 26, 25, 24, 23, 22, 20])
cookie_popularity = np.array([20, 19, 18, 20, 21, 22, 23, 24, 25, 25])
fruit_popularity = np.array([15, 16, 17, 18, 19, 20, 21, 22, 23, 25])
nut_popularity = np.array([12, 13, 14, 14, 15, 16, 17, 17, 18, 19])
candy_popularity = np.array([28, 26, 23, 21, 19, 17, 15, 14, 12, 11])

# Create a bar chart for the latest year
fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.6
positions = np.arange(len(years))

# Plotting year-wise stacked bar chart for visual comparison
for i, year in enumerate(years):
    ax.bar(year, chip_popularity[i], width=bar_width, label='Chips' if i == 0 else "", color='#ff9999', edgecolor='grey')
    ax.bar(year, cookie_popularity[i], bottom=chip_popularity[i], width=bar_width, label='Cookies' if i == 0 else "", color='#66b3ff', edgecolor='grey')
    ax.bar(year, fruit_popularity[i], bottom=chip_popularity[i] + cookie_popularity[i], width=bar_width, label='Fruits' if i == 0 else "", color='#99ff99', edgecolor='grey')
    ax.bar(year, nut_popularity[i], bottom=chip_popularity[i] + cookie_popularity[i] + fruit_popularity[i], width=bar_width, label='Nuts' if i == 0 else "", color='#ffcc99', edgecolor='grey')
    ax.bar(year, candy_popularity[i], bottom=chip_popularity[i] + cookie_popularity[i] + fruit_popularity[i] + nut_popularity[i], width=bar_width, label='Candy' if i == 0 else "", color='#c2c2f0', edgecolor='grey')

# Adding annotations for the highest bar in each year
for i, year in enumerate(years):
    total = chip_popularity[i] + cookie_popularity[i] + fruit_popularity[i] + nut_popularity[i] + candy_popularity[i]
    ax.annotate(f'Total {total}%', xy=(i, total), xytext=(0, 3), textcoords="offset points", ha='center', fontsize=9, fontweight='bold', color='black')

# Customize the plot
ax.set_title('Shift in Consumer Snack Preferences Over the Decade\n(2013-2022)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Popularity (%)', fontsize=12)

# Add Custom Legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[:5], labels[:5], fontsize=10, loc='upper left')

# Habitat Grid
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
ax.set_axisbelow(True)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()
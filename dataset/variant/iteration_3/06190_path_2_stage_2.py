import matplotlib.pyplot as plt
import numpy as np

# Define the regions and years
years = np.arange(2012, 2023)

# Artificial data for renewable energy consumption (in terawatt-hours)
na_consumption = [500, 530, 560, 590, 620, 650, 680, 720, 750, 780, 820]
eu_consumption = [450, 470, 490, 520, 550, 580, 600, 630, 670, 700, 730]
asia_consumption = [700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200]
africa_consumption = [200, 210, 220, 230, 250, 270, 290, 310, 330, 350, 370]

# Create the line chart
fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, na_consumption, marker='o', linestyle='-', color='c', linewidth=2)
ax.plot(years, eu_consumption, marker='^', linestyle='-', color='orange', linewidth=2)
ax.plot(years, asia_consumption, marker='s', linestyle='-', color='purple', linewidth=2)
ax.plot(years, africa_consumption, marker='d', linestyle='-', color='brown', linewidth=2)

# Setting title and labels
ax.set_title("Decadal Growth Trend in Renewable Energy Consumption (2012-2022)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Consumption (Terawatt-hours)", fontsize=12)

# Highlighting a significant increase in consumption around 2018 for Asia
ax.annotate('Significant Increase',
            xy=(2018, 950), 
            xytext=(2016, 1100),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=10, fontweight='bold', color='darkred')

# Adding a vertical line to mark the year 2022 as the end of the observed period
ax.axvline(x=2022, color='gray', linestyle='--', linewidth=1.5, alpha=0.7)
ax.text(2022.1, 400, '2022 End of Period', rotation=90, verticalalignment='center', fontsize=10, color='gray')

# Display the plot
plt.show()
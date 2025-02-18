import matplotlib.pyplot as plt
import numpy as np

# Define the regions and years
years = np.arange(2012, 2023)

# Artificial data for renewable energy consumption (in terawatt-hours) including new groups
na_consumption = [500, 530, 560, 590, 620, 650, 680, 720, 750, 780, 820]
eu_consumption = [450, 470, 490, 520, 550, 580, 600, 630, 670, 700, 730]
asia_consumption = [700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200]
africa_consumption = [200, 210, 220, 230, 250, 270, 290, 310, 330, 350, 370]
oceania_consumption = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
sa_consumption = [300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 510]

# Create the line chart
fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, na_consumption, marker='o', linestyle='-', color='c', linewidth=2, label='North America')
ax.plot(years, eu_consumption, marker='^', linestyle='-', color='orange', linewidth=2, label='Europe')
ax.plot(years, asia_consumption, marker='s', linestyle='-', color='purple', linewidth=2, label='Asia')
ax.plot(years, africa_consumption, marker='d', linestyle='-', color='brown', linewidth=2, label='Africa')
ax.plot(years, oceania_consumption, marker='x', linestyle='-', color='green', linewidth=2, label='Oceania')
ax.plot(years, sa_consumption, marker='*', linestyle='-', color='blue', linewidth=2, label='South America')

# Adding a vertical line to mark the year 2022
ax.axvline(x=2022, color='gray', linestyle='--', linewidth=1.5, alpha=0.7)

# Display the legend
ax.legend()

# Display the plot
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart depicts the growth in space tourism ticket sales for different space agencies from 2020 to 2025.
# We will show a comparative bar chart for ticket sales over these years for four fictional space agencies.

years = ['2020', '2021', '2022', '2023', '2024', '2025']
agencies = ['StarVoyager', 'CosmoWay', 'GalacticExpeditions', 'AstroAdventures']
# Ticket sales in thousands
ticket_sales = [
    [30, 54, 75, 100, 120, 130],  # StarVoyager
    [20, 35, 50, 65, 90, 105],    # CosmoWay
    [15, 30, 45, 60, 70, 80],     # GalacticExpeditions
    [10, 25, 35, 50, 65, 75]      # AstroAdventures
]

fig, ax = plt.subplots(figsize=(14, 8))

# Generate bar positions for each year
bar_width = 0.15
x_pos = np.arange(len(years))

# Colors for each agency
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']

# Creating the bar chart
bars = []
for i, agency_sales in enumerate(ticket_sales):
    bars.append(ax.bar(x_pos + i * bar_width, agency_sales, width=bar_width, color=colors[i], label=agencies[i], edgecolor='black'))

# Titles and labels
ax.set_title('Space Tourism Ticket Sales Growth (2020-2025)\nA Comparative Insight by Agency', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12, fontweight='bold')
ax.set_ylabel('Ticket Sales (Thousands)', fontsize=12, fontweight='bold')
ax.set_xticks(x_pos + bar_width * 1.5)
ax.set_xticklabels(years)

# Adding data labels to each bar
for bar_group in bars:
    for bar in bar_group:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 1, f'{height}', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Adding a legend for better identification
ax.legend(title='Space Agencies', loc='upper left', frameon=True, fontsize=10, title_fontsize='12')

# Customizing grid and appearance
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Tight layout adjustment
plt.tight_layout()

# Displaying the plot
plt.show()
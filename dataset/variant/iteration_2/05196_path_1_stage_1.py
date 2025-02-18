import matplotlib.pyplot as plt
import numpy as np

# Data: Planet names and their corresponding allocation percentages
planets = ["Mars", "Moon", "Europa", "Titan", "Ganymede", "Callisto", "Venus", "Ceres"]
funding_percentages = [35, 25, 15, 10, 7, 3, 3, 2]  # Must sum up to 100

# Custom colors for the pie chart
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb366','#ff6666','#c2f0c2']

# Create the donut chart
fig, ax = plt.subplots(figsize=(12, 8))
wedges, texts, autotexts = ax.pie(funding_percentages, labels=planets, colors=colors,
                                  autopct='%1.1f%%', startangle=90, textprops=dict(color="black"),
                                  wedgeprops=dict(width=0.4))

plt.setp(autotexts, size=12, weight="bold")
plt.setp(texts, size=10)

# Title for the donut chart
ax.set_title('Solar System Colonization Initiatives\nPublic Funding Distribution in 2050', 
             fontsize=16, fontweight='bold', color='darkblue', pad=20)

# Add legend for more detail
ax.legend(wedges, [f"{planet}: {percentage}%" for planet, percentage in zip(planets, funding_percentages)],
          title="Celestial Bodies", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10, title_fontsize=12)

# Equal aspect ratio ensures that the chart is circular
ax.set_aspect('equal')

# Create a subplot for a bar chart to show comparative funding amounts
funding_amounts = [350, 250, 150, 100, 70, 30, 30, 20]  # Assume arbitrary funding amounts for each body, related to percentages
ax_bar = fig.add_subplot(212)
x_pos = np.arange(len(planets))
bars = ax_bar.bar(x_pos, funding_amounts, color=colors, edgecolor='black')

ax_bar.set_title('Comparative Funding Amounts\nFor Solar System Colonization (in Billion USD)', fontsize=14, weight='bold')
ax_bar.set_xlabel('Celestial Bodies', fontsize=12)
ax_bar.set_ylabel('Funding Amount (Billion USD)', fontsize=12)
ax_bar.set_xticks(x_pos)
ax_bar.set_xticklabels(planets, rotation=45, ha='right', fontsize=11)

# Annotate each bar with the corresponding funding amount
for bar in bars:
    height = bar.get_height()
    ax_bar.text(bar.get_x() + bar.get_width() / 2, height + 5, f"${height}B", ha='center', va='bottom', fontsize=10)

plt.tight_layout()

plt.show()
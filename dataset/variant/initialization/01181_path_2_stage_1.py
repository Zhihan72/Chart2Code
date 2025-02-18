import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
countries = ['Country A', 'Country B', 'Country C', 'Country D', 'Country E']
tea_consumption = [2.5, 4.2, 1.8, 3.6, 2.9]

# Creating horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 6))
y_pos = np.arange(len(countries))
colors = ['#B5651D', '#8B4513', '#A0522D', '#CD853F', '#D2691E']
bars = ax.barh(y_pos, tea_consumption, color=colors, alpha=0.8, height=0.5)

# Add data annotations
for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.1, bar.get_y() + bar.get_height() / 2.0,
            f'{width:.1f}', va='center', ha='left', fontsize=10)

# Set the title and labels
ax.set_title('Average Annual Tea Consumption\nPer Person by Country', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Country', fontsize=12)
ax.set_xlabel('Tea Consumption (kg/person/year)', fontsize=12)

# Set y-axis tick positions and labels
ax.set_yticks(y_pos)
ax.set_yticklabels(countries, fontsize=10)

# Adding grid only on x-axis for better readability
ax.xaxis.grid(True, linestyle='--', linewidth=0.6, alpha=0.7)

# Adjust layout
plt.tight_layout()

# Show the chart
plt.show()
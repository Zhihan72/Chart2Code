import numpy as np
import matplotlib.pyplot as plt

departments = ["Support", "HR", "Development", "Sales", "R&D", "Marketing"]
quarters = ["Fourth Quarter", "Third Quarter", "Second Quarter", "First Quarter"]

# Manually altered productivity data, changes within each department's data
development = [87, 89, 85, 88]
marketing = [75, 78, 70, 80]
sales = [88, 90, 92, 89]
hr = [68, 65, 72, 70]
customer_support = [87, 90, 88, 85]
rnd = [98, 95, 96, 97]

productivity_data = np.array([customer_support, hr, development, sales, rnd, marketing])

fig, ax = plt.subplots(figsize=(14, 8))

x = np.arange(len(quarters))

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

bottom = np.zeros(len(quarters))

for i, department in enumerate(departments):
    ax.bar(x, productivity_data[i], label=department, color=colors[i], bottom=bottom)
    bottom += productivity_data[i]

ax.set_title("2023 Productivity Analysis by Segment", fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Time Periods', fontsize=12)
ax.set_ylabel('Output Efficiency (%)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(quarters)
ax.set_ylim(0, sum(rnd))

ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title="Segments", fontsize=10)

ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
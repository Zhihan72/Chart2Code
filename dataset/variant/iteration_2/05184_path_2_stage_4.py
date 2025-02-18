import numpy as np
import matplotlib.pyplot as plt

companies = ['TechCorp', 'InnovateX', 'FutureSolutions', 'SkyNet', 'QuantumTech']
sectors = ['AI', 'IoT', 'Cloud Computing', 'Cybersecurity', 'Blockchain']

revenues = np.array([
    [15, 20, 25, 30, 22],
    [10, 15, 20, 18, 16],
    [25, 28, 30, 35, 40],
    [8, 10, 12, 15, 13],
    [5, 7, 9, 11, 6]
])

colors = ['#FF6347', '#32CD32', '#9370DB', '#4682B4', '#FFD700']

# Calculate total revenue for each sector
total_revenue_per_sector = revenues.sum(axis=1)

# Sort sectors by total revenue in descending order
sorted_indices = np.argsort(total_revenue_per_sector)[::-1]
sorted_revenues = revenues[sorted_indices]
sorted_sectors = [sectors[i] for i in sorted_indices]
sorted_colors = [colors[i] for i in sorted_indices]

x = np.arange(len(companies))

fig, ax = plt.subplots(figsize=(10, 6))

for i, (sector, color) in enumerate(zip(sorted_sectors, sorted_colors)):
    ax.bar(x + i * 0.15, sorted_revenues[i], 0.15, label=sector, color=color)

ax.yaxis.grid(True, linestyle='--', linewidth=0.7, color='gray')

ax.set_xlabel('Companies', fontsize=14)
ax.set_ylabel('Revenue (in Billion USD)', fontsize=14)
ax.set_title('Total Revenue by Sector in Ascending Order', fontsize=16, fontweight='bold')
ax.set_xticks(x + 0.30)
ax.set_xticklabels(companies)
ax.legend(title='Sectors', fontsize=12, frameon=False)

ax.spines['top'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import numpy as np

sectors = ["AI", "Blockchain", "Internet of Things", "Cyber Security"]
initial_funding = [10, 8, 7, 6]
year_end_revenue = [15, 12, 11, 10]

# Calculate growth percentage
growth_percentage = [(rev - init) / init * 100 for init, rev in zip(initial_funding, year_end_revenue)]

# Zip and sort data based on initial funding in descending order
sorted_data = sorted(zip(initial_funding, year_end_revenue, growth_percentage, sectors), reverse=True)

# Unzip data
initial_funding_sorted, year_end_revenue_sorted, growth_percentage_sorted, sectors_sorted = zip(*sorted_data)

fig, ax = plt.subplots(figsize=(14, 8))

bars_initial = ax.bar(np.arange(len(sectors_sorted)) - 0.2, initial_funding_sorted, width=0.4, color='#1f77b4')
bars_revenue = ax.bar(np.arange(len(sectors_sorted)) + 0.2, year_end_revenue_sorted, width=0.4, color='#1f77b4')

ax.set_title('TechVille Tech Innovation Challenge Results', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Technology Sectors', fontsize=12)
ax.set_ylabel('Amount (Million USD)', fontsize=12)
ax.set_xticks(np.arange(len(sectors_sorted)))
ax.set_xticklabels(sectors_sorted)

ax.bar_label(bars_initial, padding=3, fontsize=10)
ax.bar_label(bars_revenue, padding=3, fontsize=10)

ax2 = ax.twinx()
ax2.plot(np.arange(len(sectors_sorted)), growth_percentage_sorted, color='green', marker='o', linestyle='--', linewidth=2)
ax2.set_ylabel('Growth Percentage (%)', fontsize=12)
ax2.set_ylim(0, max(growth_percentage_sorted) + 10)

for i, gp in enumerate(growth_percentage_sorted):
    ax2.text(i, gp + 1, f'{gp:.1f}%', ha='center', va='bottom', color='green', fontsize=10, fontweight='bold')

ax.grid(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()
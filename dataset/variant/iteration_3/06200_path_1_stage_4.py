import matplotlib.pyplot as plt
import numpy as np

# Original data
years = np.arange(2015, 2026)
ev_sales = [100, 200, 450, 700, 1100, 1500, 2000, 2700, 3500, 4300, 5200]
co2_reduction = np.array(ev_sales) * 0.15
gov_incentives = [5, 10, 20, 30, 50, 70, 90, 120, 150, 180, 220]
charging_stations = [10, 15, 25, 35, 50, 70, 90, 115, 145, 180, 220]

# Sort data by EV sales in descending order
sorted_indices = np.argsort(ev_sales)[::-1]
sorted_years = years[sorted_indices]
sorted_ev_sales = np.array(ev_sales)[sorted_indices]
sorted_co2_reduction = co2_reduction[sorted_indices]
sorted_gov_incentives = np.array(gov_incentives)[sorted_indices]
sorted_charging_stations = np.array(charging_stations)[sorted_indices]

# Plot
fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.bar(sorted_years, sorted_ev_sales, color='#1F77B4')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of EVs Sold', fontsize=12)
ax1.set_title('Techville EV Adoption & Infrastructure (2015-2025)', fontsize=16, fontweight='bold')
ax1.set_xticks(sorted_years)
ax1.set_xticklabels(sorted_years, rotation=45, ha='right')

for bar, sales in zip(ax1.patches, sorted_ev_sales):
    ax1.text(bar.get_x() + bar.get_width() / 2, sales + 100, f'{sales}', ha='center', va='bottom', fontsize=10, fontweight='bold')

ax2 = ax1.twinx()
ax2.plot(sorted_years, sorted_co2_reduction, color='#FF7F0E', linestyle='--', marker='o', linewidth=2, markersize=8)
ax2.set_ylabel('CO2 Reduction (in tons)', fontsize=12, color='#FF7F0E')
ax2.tick_params(axis='y', labelcolor='#FF7F0E')

ax2.plot(sorted_years, sorted_gov_incentives, color='#2CA02C', linestyle='-', marker='s', linewidth=2, markersize=8)
ax2.plot(sorted_years, sorted_charging_stations, color='#D62728', linestyle='-.', marker='^', linewidth=2, markersize=8)

plt.tight_layout()
plt.show()
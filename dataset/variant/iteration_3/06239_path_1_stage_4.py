import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2026)
sedans_sales = np.array([0.2, 0.4, 0.6, 0.85, 1.2, 1.5, 2.0, 2.4, 2.8, 3.3, 3.8])
suvs_sales = np.array([0.1, 0.3, 0.5, 0.7, 0.9, 1.3, 1.7, 2.1, 2.5, 3.0, 3.5])
hatchbacks_sales = np.array([0.05, 0.1, 0.25, 0.35, 0.45, 0.65, 0.8, 0.9, 1.1, 1.3, 1.4])
trucks_sales = np.array([0.01, 0.05, 0.1, 0.25, 0.45, 0.7, 1.0, 1.4, 1.8, 2.2, 2.6])
buses_sales = np.array([0.02, 0.03, 0.06, 0.1, 0.15, 0.2, 0.3, 0.35, 0.42, 0.48, 0.55])
motorcycles_sales = np.array([0.03, 0.08, 0.12, 0.2, 0.25, 0.3, 0.38, 0.5, 0.6, 0.7, 0.75])

sales_data = np.vstack([sedans_sales, suvs_sales, hatchbacks_sales, trucks_sales, buses_sales, motorcycles_sales])

# Applying a single color for all data groups
single_color = '#ffadad'

fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, sales_data, colors=[single_color], alpha=0.85)

ax.set_title('Diverse E-Vehicle Sales Boom (2015-2025)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline', fontsize=12)
ax.set_ylabel('Volume Sold (millions)', fontsize=12)

ax.set_xticks(years)
ax.set_yticks(np.arange(0, 5.1, 0.5))
ax.set_xlim(2015, 2025)
ax.set_ylim(0, 5)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2005, 2021)

waste_reduction = [30, 5, 46, 65, 35, 9, 12, 59, 7, 40, 22, 26, 72, 15, 18, 52]
water_conservation = [33, 12, 28, 52, 45, 7, 4, 9, 5, 67, 39, 15, 19, 59, 3, 23]
green_energy = [95, 3, 19, 7, 40, 10, 2, 1, 32, 70, 25, 82, 49, 14, 59, 5]
community_awareness = [41, 3, 20, 35, 8, 24, 13, 56, 10, 48, 16, 65, 6, 29, 4, 2]
urban_greenery = [44, 19, 3, 30, 8, 37, 71, 94, 2, 15, 52, 61, 5, 24, 11, 82]

sustainability_efforts = np.vstack([
    waste_reduction, water_conservation, green_energy, community_awareness, urban_greenery
])

# Plot
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(years, sustainability_efforts,
             colors=['#FF6347', '#4682B4', '#9ACD32', '#8A2BE2', '#FFD700'], alpha=0.8)

# Updated textual elements
ax.set_title("GreenVille’s Environmental Impact (2005-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline', fontsize=14)
ax.set_ylabel('Change Metrics (Arbitrary)', fontsize=14)

ax.set_xticks(np.arange(2005, 2021, 1))
ax.set_yticks(np.arange(0, 301, 50))

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2005, 2021)

waste_reduction = [5, 7, 9, 12, 15, 18, 22, 26, 30, 35, 40, 46, 52, 59, 65, 72]
water_conservation = [3, 4, 5, 7, 9, 12, 15, 19, 23, 28, 33, 39, 45, 52, 59, 67]
green_energy = [1, 2, 3, 5, 7, 10, 14, 19, 25, 32, 40, 49, 59, 70, 82, 95]
community_awareness = [2, 3, 4, 6, 8, 10, 13, 16, 20, 24, 29, 35, 41, 48, 56, 65]
urban_greenery = [2, 3, 5, 8, 11, 15, 19, 24, 30, 37, 44, 52, 61, 71, 82, 94]

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
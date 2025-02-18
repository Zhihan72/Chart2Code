import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

# Randomly altered the data within the original dimensional structure
manufacturing = np.array([12, 13, 22, 26, 37, 43, 54, 67, 74, 84, 96, 119, 127, 142, 161, 172, 189, 208, 227, 249, 271])
healthcare = np.array([6, 8, 9, 14, 19, 21, 31, 36, 46, 54, 68, 74, 90, 101, 114, 129, 150, 158, 178, 192, 203])
retail = np.array([4, 6, 6, 11, 12, 18, 21, 29, 37, 44, 49, 61, 71, 79, 91, 99, 110, 129, 139, 154, 169])
agriculture = np.array([1, 4, 3, 7, 7, 11, 12, 16, 23, 24, 33, 36, 48, 55, 68, 79, 87, 105, 115, 134, 146])

plt.figure(figsize=(14, 8))
plt.stackplot(years, manufacturing, healthcare, retail, agriculture,
              labels=['Tech', 'Auto', 'Sales', 'Farming'],
              colors=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99'], alpha=0.7)

plt.title("Changing Trends of Tech Use\n2000-2020", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Timeline", fontsize=12)
plt.ylabel("Tech Deployment Units", fontsize=12)

plt.legend(loc='upper left', fontsize=10, title="Sectors")

plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
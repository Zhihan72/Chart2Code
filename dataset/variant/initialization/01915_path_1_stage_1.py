import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

manufacturing = np.array([10, 15, 20, 28, 35, 45, 55, 65, 75, 85, 100, 115, 130, 145, 160, 175, 190, 210, 230, 250, 270])
healthcare = np.array([5, 7, 10, 13, 18, 23, 30, 38, 45, 55, 65, 75, 88, 100, 115, 130, 145, 160, 175, 190, 205])
retail = np.array([3, 5, 7, 10, 13, 17, 22, 28, 35, 42, 50, 58, 67, 77, 88, 100, 113, 126, 140, 155, 170])
agriculture = np.array([2, 3, 4, 6, 8, 10, 13, 17, 21, 26, 32, 39, 47, 56, 66, 77, 89, 102, 116, 131, 147])

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
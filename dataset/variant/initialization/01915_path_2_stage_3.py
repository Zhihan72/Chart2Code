import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)
manufacturing = np.array([10, 20, 15, 28, 45, 35, 55, 75, 65, 85, 115, 100, 130, 145, 160, 190, 175, 230, 210, 270, 250])
healthcare = np.array([5, 10, 7, 18, 13, 23, 38, 30, 45, 65, 55, 75, 88, 115, 100, 145, 130, 175, 160, 205, 190])
retail = np.array([3, 7, 5, 13, 10, 17, 28, 22, 35, 50, 42, 58, 67, 77, 100, 88, 113, 140, 126, 170, 155])
agriculture = np.array([2, 4, 3, 8, 6, 10, 17, 13, 21, 32, 26, 39, 47, 66, 56, 89, 77, 116, 102, 147, 131])

plt.figure(figsize=(14, 8))
plt.stackplot(years, manufacturing, healthcare, retail, agriculture,
              colors=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99'], alpha=0.7)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
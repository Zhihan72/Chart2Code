import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

adoption_lights = [2, 4, 7, 10, 14, 20, 28, 38, 50, 65, 80]
adoption_thermostats = [1, 3, 5, 8, 12, 18, 25, 33, 44, 58, 73]
adoption_security = [1, 2, 4, 6, 9, 14, 21, 29, 38, 50, 65]

plt.figure(figsize=(12, 7))

plt.stackplot(years, adoption_lights, adoption_thermostats, adoption_security,
              colors=['#99FF99', '#FF9999', '#66B3FF'], alpha=0.8)

plt.title("Smart Tech Adoption (2010-20)", fontsize=16, fontweight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Adoption (%)", fontsize=12)
plt.xlim(years[0], years[-1])
plt.xticks(years, rotation=45)

plt.tight_layout()
plt.show()
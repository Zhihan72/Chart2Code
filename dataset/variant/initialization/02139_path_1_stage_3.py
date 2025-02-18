import matplotlib.pyplot as plt
import numpy as np

devices = ["Smart Thermostats", "Smart Appliances", "Smart Security", "Smart Lights"]
years = np.arange(2010, 2021)

# Manually shuffled versions of the original adoption lists
adoption_lights = [10, 28, 38, 4, 50, 20, 2, 80, 65, 7, 14]
adoption_thermostats = [5, 12, 44, 18, 1, 58, 3, 73, 33, 8, 25]
adoption_security = [14, 9, 4, 6, 65, 29, 1, 21, 50, 2, 38]
adoption_appliances = [2, 35, 7, 47, 4, 12, 18, 1, 26, 0, 60]

plt.figure(figsize=(12, 7))

plt.stackplot(years, adoption_lights, adoption_thermostats, adoption_security, adoption_appliances,
              labels=devices,
              colors=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99'], alpha=0.8,
              edgecolor=['#333333', '#444444', '#555555', '#666666'], linewidth=1.5)

plt.title("Adoption Growth of Smart Home Devices Over Time", fontsize=16, fontweight='bold')
plt.xlabel("Timeline", fontsize=12, fontstyle='italic')
plt.ylabel("Percentage Adoption", fontsize=12, color='darkred')
plt.xlim(years[0], years[-1])
plt.xticks(years, rotation=30)
plt.legend(loc='upper center', fontsize=10, title='Devices Categories', title_fontsize='12')

plt.grid(visible=True, linestyle=':', alpha=0.6)

plt.tight_layout()

plt.show()
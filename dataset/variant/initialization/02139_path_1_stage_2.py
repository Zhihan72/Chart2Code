import matplotlib.pyplot as plt
import numpy as np

devices = ["Smart Thermostats", "Smart Appliances", "Smart Security", "Smart Lights"]
years = np.arange(2010, 2021)

adoption_lights = [2, 4, 7, 10, 14, 20, 28, 38, 50, 65, 80]
adoption_thermostats = [1, 3, 5, 8, 12, 18, 25, 33, 44, 58, 73]
adoption_security = [1, 2, 4, 6, 9, 14, 21, 29, 38, 50, 65]
adoption_appliances = [0, 1, 2, 4, 7, 12, 18, 26, 35, 47, 60]

plt.figure(figsize=(12, 7))

plt.stackplot(years, adoption_lights, adoption_thermostats, adoption_security, adoption_appliances,
              labels=devices,
              colors=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99'], alpha=0.8,
              edgecolor=['#333333','#444444','#555555','#666666'], linewidth=1.5)

plt.title("Adoption Growth of Smart Home Devices Over Time", fontsize=16, fontweight='bold')
plt.xlabel("Timeline", fontsize=12, fontstyle='italic')
plt.ylabel("Percentage Adoption", fontsize=12, color='darkred')
plt.xlim(years[0], years[-1])
plt.xticks(years, rotation=30)
plt.legend(loc='upper center', fontsize=10, title='Devices Categories', title_fontsize='12')

plt.grid(visible=True, linestyle=':', alpha=0.6)

plt.tight_layout()

plt.show()
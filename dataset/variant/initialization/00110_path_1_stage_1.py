import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2024)
solar_energy = np.array([10, 15, 22, 33, 50, 65, 80, 100, 125, 150, 180])
wind_energy = np.array([20, 25, 35, 50, 70, 90, 120, 160, 200, 250, 310])
hydro_energy = np.array([50, 55, 60, 65, 70, 75, 78, 80, 82, 85, 88])

energy_data = np.vstack([solar_energy, wind_energy, hydro_energy])

plt.figure(figsize=(12, 8))
plt.stackplot(years, energy_data, labels=['Solar', 'Wind', 'Hydropower'], 
              colors=['#228B22', '#228B22', '#228B22'], alpha=0.8)

plt.title("The Rise of Green Energy:\nA Decade of Power Production Transformation in EcoLand", 
          fontsize=16, weight='bold')
plt.xlabel("Year", fontsize=14)
plt.ylabel("Energy Production (TWh)", fontsize=14)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 601, 50))
plt.legend(loc='upper left', fontsize=12, frameon=True)
plt.grid(alpha=0.3, linestyle='--')

plt.annotate("Significant Solar Expansion", xy=(2018, 80), xytext=(2015, 220),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='darkorange'), fontsize=12)

plt.annotate("Wind Energy Surpasses Hydropower", xy=(2021, 250), xytext=(2017, 400),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='blue'), fontsize=12)

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

natural_gas = [120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 210, 220, 230, 240]
nuclear = [50, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145]
solar = [5, 6, 7, 8, 10, 12, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]
wind = [10, 12, 15, 18, 22, 25, 30, 35, 40, 45, 50, 60, 70, 85, 100, 120, 140, 160, 180, 200, 220]

plt.figure(figsize=(12, 8))
plt.stackplot(years, natural_gas, nuclear, solar, wind, colors=['#eb8334', '#6e6ec2', '#f2e431', '#8cc13f'], alpha=0.8)

# Remove labels, title, legend, and annotations
plt.grid(linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
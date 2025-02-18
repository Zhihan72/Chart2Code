import matplotlib.pyplot as plt
import numpy as np

# Data setup
years = np.arange(2013, 2024)
epic_fantasy = np.array([70, 72, 74, 78, 75, 80, 85, 83, 88, 90, 87])
urban_fantasy = np.array([50, 55, 58, 62, 64, 68, 72, 70, 68, 65, 63])
dark_fantasy = np.array([30, 35, 37, 40, 45, 50, 55, 53, 57, 60, 58])
historical_fantasy = np.array([25, 30, 28, 32, 36, 38, 42, 45, 48, 50, 52])
romantic_fantasy = np.array([10, 12, 15, 20, 22, 25, 30, 35, 33, 30, 28])

average_popularity = (epic_fantasy + urban_fantasy + dark_fantasy + historical_fantasy + romantic_fantasy) / 5

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(years, epic_fantasy, urban_fantasy, dark_fantasy, historical_fantasy, romantic_fantasy,
             colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'],
             alpha=0.8)

ax.plot(years, average_popularity, color='black', linewidth=2.5, linestyle='--', marker='o')

plt.tight_layout()
plt.show()
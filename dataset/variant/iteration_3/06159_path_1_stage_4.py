import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
farm_a_productivity = np.array([35, 40, 42, 45, 50, 52, 55, 58, 60, 65, 70])

fig, ax = plt.subplots(figsize=(14, 8))

# Shuffle colors: changed from 'green' to 'blue'
ax.plot(years, farm_a_productivity, color='blue', linestyle='-', linewidth=2, marker='o')

plt.show()
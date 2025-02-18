import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
reading = np.array([50, 52, 53, 54, 55, 56, 57, 59, 60, 62, 65])
sports = np.array([30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50])
traveling = np.array([10, 12, 15, 18, 22, 26, 30, 35, 40, 45, 50])
cooking = np.array([15, 16, 18, 19, 20, 21, 23, 25, 27, 28, 30])

hobbies_data = np.vstack([reading, sports, traveling, cooking])
colors = ['#FF9999', '#66B3FF', '#FFCC99', '#C2C2F0']

plt.figure(figsize=(14, 8))
plt.stackplot(years, hobbies_data, colors=colors, alpha=0.8)

plt.tight_layout()
plt.show()
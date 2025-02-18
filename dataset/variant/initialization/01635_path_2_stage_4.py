import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2023)

ai_adoption = np.array([5, 10, 20, 30, 40, 50, 55, 60, 70, 75])
iot_adoption = np.array([10, 15, 25, 35, 45, 55, 53, 51, 50, 48])
ar_adoption = np.array([3, 7, 10, 15, 18, 20, 22, 20, 18, 17])

total_adoption = ai_adoption + iot_adoption + ar_adoption
ai_adoption_percentage = (ai_adoption / total_adoption) * 100
iot_adoption_percentage = (iot_adoption / total_adoption) * 100
ar_adoption_percentage = (ar_adoption / total_adoption) * 100
adoption_data = np.vstack([ai_adoption_percentage, iot_adoption_percentage, ar_adoption_percentage])

plt.figure(figsize=(12, 7))
# Shuffled colors
colors = ['#2ca02c', '#d62728', '#1f77b4']
plt.stackplot(years, adoption_data, colors=colors, alpha=0.8)

plt.xticks(years, rotation=45)
plt.tight_layout()
plt.show()
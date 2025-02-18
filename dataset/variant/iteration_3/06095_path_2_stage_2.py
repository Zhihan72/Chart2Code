import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

machine_learning = [10, 15, 25, 35, 45, 50, 60, 70, 80, 85, 90]
computer_vision = [5, 10, 20, 30, 40, 55, 65, 75, 80, 85, 87]
natural_language_processing = [7, 12, 22, 32, 40, 50, 60, 70, 80, 85, 88]

plt.figure(figsize=(12, 8))

plt.plot(years, machine_learning, marker='o', color='purple', linestyle='-', linewidth=2)
plt.plot(years, computer_vision, marker='s', color='orange', linestyle='-', linewidth=2)
plt.plot(years, natural_language_processing, marker='^', color='cyan', linestyle='-', linewidth=2)

plt.annotate('Breakthrough in ML algorithms', xy=(2016, machine_learning[6]), xytext=(2016, machine_learning[6] + 10),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, ha='right')
plt.annotate('Improvements in CV accuracy', xy=(2018, computer_vision[8]), xytext=(2018, computer_vision[8] + 10),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, ha='right')
plt.annotate('Advancements in NLP models', xy=(2020, natural_language_processing[10]), xytext=(2020, natural_language_processing[10] + 10),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, ha='right')

plt.title('Decade of AI Progress (2010-2020)', fontsize=18, fontweight='bold')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Progress (%)', fontsize=14)
plt.xticks(years)
plt.yticks(range(0, 101, 10))

plt.show()
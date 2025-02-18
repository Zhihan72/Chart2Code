import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2010, 2021)

teenagers = np.array([0.5, 0.6, 0.7, 0.8, 0.8, 0.9, 1.0, 1.0, 1.1, 1.2, 1.3])
adults = np.array([2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5])
seniors = np.array([1.0, 1.0, 1.1, 1.1, 1.2, 1.3, 1.2, 1.1, 1.1, 1.1, 1.2])

students = np.array([1.0, 1.1, 1.2, 1.2, 1.3, 1.3, 1.4, 1.5, 1.5, 1.6, 1.7])
retirees = np.array([1.3, 1.3, 1.4, 1.4, 1.5, 1.6, 1.6, 1.5, 1.5, 1.6, 1.7])

plt.figure(figsize=(14, 8))

plt.plot(years, teenagers, color='green', marker='o', linestyle='-', linewidth=2)
plt.plot(years, adults, color='purple', marker='s', linestyle='-', linewidth=2)
plt.plot(years, seniors, color='orange', marker='^', linestyle='-', linewidth=2)

plt.plot(years, students, color='blue', marker='d', linestyle='-', linewidth=2)
plt.plot(years, retirees, color='red', marker='x', linestyle='-', linewidth=2)

plt.xticks(years, rotation=45)

plt.axvline(x=2015, linestyle='--', color='purple', linewidth=1.5)

for year, cups in zip(years, teenagers):
    if year in [2010, 2015, 2020]:
        plt.annotate(f'{cups} c', xy=(year, cups), textcoords='offset points', xytext=(-30, 10), ha='center', fontsize=9, color='green')

plt.xlim(2010, 2020)
plt.ylim(0, 4)

plt.tight_layout()
plt.show()
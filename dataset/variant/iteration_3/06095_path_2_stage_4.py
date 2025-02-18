import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

machine_learning = [10, 15, 25, 35, 45, 50, 60, 70, 80, 85, 90]
computer_vision = [5, 10, 20, 30, 40, 55, 65, 75, 80, 85, 87]
natural_language_processing = [7, 12, 22, 32, 40, 50, 60, 70, 80, 85, 88]
reinforcement_learning = [2, 5, 10, 15, 25, 30, 40, 50, 65, 75, 80]

plt.figure(figsize=(12, 8))

plt.plot(years, machine_learning, marker='o', color='purple', linestyle='-', linewidth=2)
plt.plot(years, computer_vision, marker='s', color='orange', linestyle='-', linewidth=2)
plt.plot(years, natural_language_processing, marker='^', color='cyan', linestyle='-', linewidth=2)
plt.plot(years, reinforcement_learning, marker='d', color='green', linestyle='-', linewidth=2)

plt.xticks(years)
plt.yticks(range(0, 101, 10))

plt.show()
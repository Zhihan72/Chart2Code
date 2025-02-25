import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2015, 2026)
ev_us = np.array([0.5, 1.1, 0.8, 3.5, 2.0, 12.0, 6.5, 35.0, 18.0, 45.0, 26.0])
ev_europe = np.array([0.4, 1.2, 0.7, 4.0, 2.5, 13.0, 7.0, 48.0, 20.0, 38.0, 28.0])
ev_china = np.array([1.0, 4.0, 2.0, 10.0, 7.0, 30.0, 18.0, 90.0, 42.0, 70.0, 55.0])
ev_japan = np.array([0.3, 0.9, 0.5, 2.8, 1.5, 9.0, 5.0, 40.0, 14.0, 30.0, 21.0])
ev_india = np.array([0.1, 0.4, 0.2, 1.5, 0.8, 6.0, 3.0, 30.0, 10.0, 22.0, 15.0])

plt.figure(figsize=(12, 8))

plt.plot(years, ev_us, color='blue', marker='o', linestyle='-', linewidth=2, markersize=5)
plt.plot(years, ev_europe, color='green', marker='s', linestyle='-', linewidth=2, markersize=5)
plt.plot(years, ev_china, color='red', marker='d', linestyle='-', linewidth=2, markersize=5)
plt.plot(years, ev_japan, color='orange', marker='p', linestyle='-', linewidth=2, markersize=5)
plt.plot(years, ev_india, color='purple', marker='*', linestyle='-', linewidth=2, markersize=5)

plt.title('Electric Vehicle Adoption Rates (2015-2025)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('EV Adoption Rate (in millions)', fontsize=14)

plt.tight_layout()
plt.show()
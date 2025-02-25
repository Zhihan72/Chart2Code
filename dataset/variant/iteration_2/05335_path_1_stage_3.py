import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2015, 2026)
ev_us = np.array([0.5, 0.8, 1.1, 2.0, 3.5, 6.5, 12.0, 18.0, 26.0, 35.0, 45.0])
ev_europe = np.array([0.4, 0.7, 1.2, 2.5, 4.0, 7.0, 13.0, 20.0, 28.0, 38.0, 48.0])
ev_china = np.array([1.0, 2.0, 4.0, 7.0, 10.0, 18.0, 30.0, 42.0, 55.0, 70.0, 90.0])
ev_japan = np.array([0.3, 0.5, 0.9, 1.5, 2.8, 5.0, 9.0, 14.0, 21.0, 30.0, 40.0])
ev_india = np.array([0.1, 0.2, 0.4, 0.8, 1.5, 3.0, 6.0, 10.0, 15.0, 22.0, 30.0])
ev_korea = np.array([0.2, 0.4, 0.7, 1.1, 2.0, 3.5, 6.0, 9.0, 14.0, 19.0, 25.0])
ev_australia = np.array([0.1, 0.3, 0.5, 0.9, 1.6, 2.5, 4.5, 7.0, 10.0, 15.0, 21.0])

plt.figure(figsize=(12, 8))

plt.plot(years, ev_us, color='blue', marker='v', linestyle='--', linewidth=3, markersize=7, label='USA')
plt.plot(years, ev_europe, color='orange', marker='x', linestyle='-', linewidth=2, markersize=6, label='Europe')
plt.plot(years, ev_china, color='red', marker='o', linestyle=':', linewidth=2, markersize=8, label='China')
plt.plot(years, ev_japan, color='green', marker='s', linestyle='-', linewidth=2, markersize=5, label='Japan')
plt.plot(years, ev_india, color='magenta', marker='^', linestyle='-.', linewidth=2, markersize=6, label='India')
plt.plot(years, ev_korea, color='purple', marker='p', linestyle='--', linewidth=2, markersize=5, label='South Korea')
plt.plot(years, ev_australia, color='cyan', marker='d', linestyle='-', linewidth=2, markersize=4, label='Australia')

plt.title('Electric Vehicle Adoption Rates (2015-2025)\nHypothetical Data Analysis Across Major Regions', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('EV Adoption Rate (in millions)', fontsize=14)

plt.grid(linestyle='-', alpha=0.7)
plt.legend(title='Regions', fontsize=10, loc='lower right', frameon=False)

annotations = [
    ('Rapid Growth in China', 2020, 10.0),
    ('Kickstart in India', 2020, 3.0),
    ('Accelerated Growth in USA', 2021, 6.5)
]

for text, x, y in annotations:
    plt.annotate(text, xy=(x, y), xytext=(-30, 20), textcoords='offset points', arrowprops=dict(arrowstyle='->', color='black'), fontsize=11, color='grey')

plt.tight_layout()
plt.show()
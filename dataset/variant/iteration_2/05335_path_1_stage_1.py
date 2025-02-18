import numpy as np
import matplotlib.pyplot as plt

# Define the years and adoption rates for each region
years = np.arange(2015, 2026)
ev_us = np.array([0.5, 0.8, 1.1, 2.0, 3.5, 6.5, 12.0, 18.0, 26.0, 35.0, 45.0])
ev_europe = np.array([0.4, 0.7, 1.2, 2.5, 4.0, 7.0, 13.0, 20.0, 28.0, 38.0, 48.0])
ev_china = np.array([1.0, 2.0, 4.0, 7.0, 10.0, 18.0, 30.0, 42.0, 55.0, 70.0, 90.0])
ev_japan = np.array([0.3, 0.5, 0.9, 1.5, 2.8, 5.0, 9.0, 14.0, 21.0, 30.0, 40.0])
ev_india = np.array([0.1, 0.2, 0.4, 0.8, 1.5, 3.0, 6.0, 10.0, 15.0, 22.0, 30.0])
ev_korea = np.array([0.2, 0.4, 0.7, 1.1, 2.0, 3.5, 6.0, 9.0, 14.0, 19.0, 25.0])
ev_australia = np.array([0.1, 0.3, 0.5, 0.9, 1.6, 2.5, 4.5, 7.0, 10.0, 15.0, 21.0])

# Set up the figure and axis
plt.figure(figsize=(12, 8))

# Plot each region's data
plt.plot(years, ev_us, color='blue', marker='o', linestyle='-', linewidth=2, markersize=5, label='USA')
plt.plot(years, ev_europe, color='green', marker='s', linestyle='-', linewidth=2, markersize=5, label='Europe')
plt.plot(years, ev_china, color='red', marker='d', linestyle='-', linewidth=2, markersize=5, label='China')
plt.plot(years, ev_japan, color='orange', marker='p', linestyle='-', linewidth=2, markersize=5, label='Japan')
plt.plot(years, ev_india, color='purple', marker='*', linestyle='-', linewidth=2, markersize=5, label='India')
plt.plot(years, ev_korea, color='cyan', marker='x', linestyle='-', linewidth=2, markersize=5, label='South Korea')
plt.plot(years, ev_australia, color='magenta', marker='^', linestyle='-', linewidth=2, markersize=5, label='Australia')

# Title and labels
plt.title('Electric Vehicle Adoption Rates (2015-2025)\nHypothetical Data Analysis Across Major Regions', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('EV Adoption Rate (in millions)', fontsize=14)

# Add grid, legend, and annotate significant data points
plt.grid(linestyle='--', alpha=0.6)
plt.legend(title='Regions', fontsize=12, loc='upper left')

# Annotations
annotations = [
    ('Rapid Growth in China', 2020, 10.0),
    ('Kickstart in India', 2020, 3.0),
    ('Accelerated Growth in USA', 2021, 6.5)
]

for text, x, y in annotations:
    plt.annotate(text, xy=(x, y), xytext=(-30, 20), textcoords='offset points', arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='black')

plt.tight_layout()
plt.show()
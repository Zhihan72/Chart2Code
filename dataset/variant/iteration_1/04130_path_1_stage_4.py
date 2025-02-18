import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

# Existing data
country_a_adoption = np.array([2, 3, 4, 7, 10, 12, 15, 19, 22, 25, 30, 35, 41, 48, 55, 63, 70, 78, 86, 93, 100])
country_b_adoption = np.array([1, 1.5, 2.5, 4, 6, 8, 12, 15, 18, 22, 27, 33, 40, 48, 57, 67, 78, 90, 95, 98, 100])
country_c_adoption = np.array([0.5, 1, 1.5, 2.5, 4, 6, 9, 13, 17, 23, 30, 38, 47, 57, 68, 80, 85, 90, 94, 97, 100])

# New hypothetical data
country_d_adoption = np.array([0, 1, 2, 3, 5, 7, 11, 16, 21, 27, 34, 42, 51, 61, 72, 84, 87, 91, 95, 99, 100])
country_e_adoption = np.array([2, 4, 6, 9, 13, 18, 24, 31, 39, 48, 58, 69, 81, 84, 86, 88, 91, 94, 97, 100, 100])

plt.figure(figsize=(12, 8))

# Plot existing data
plt.plot(years, country_a_adoption, color='red', marker='o', linewidth=2, markersize=6, label='Country A')
plt.plot(years, country_b_adoption, color='blue', marker='s', linewidth=2, markersize=6, label='Country B')
plt.plot(years, country_c_adoption, color='green', marker='^', linewidth=2, markersize=6, label='Country C')

# Plot new hypothetical data
plt.plot(years, country_d_adoption, color='purple', marker='d', linewidth=2, markersize=6, label='Country D')
plt.plot(years, country_e_adoption, color='orange', marker='x', linewidth=2, markersize=6, label='Country E')

plt.title("Growth of Clean Energy Usage\nIn Different Areas (2000-2020)", fontsize=16, fontweight='bold', ha='center')
plt.xlabel('Timeline', fontsize=14)
plt.ylabel('Renewable Share (%)', fontsize=14)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 101, 10))
plt.ylim(0, 110)

plt.legend(loc='upper left')

plt.annotate('Innovation Boost',
             xy=(2015, 63), xytext=(2012, 80),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, color='red', fontweight='bold')

plt.annotate('Subsidy Increase',
             xy=(2010, 27), xytext=(2007, 45),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, color='blue', fontweight='bold')

plt.annotate('Breakthrough Discovery',
             xy=(2015, 68), xytext=(2012, 85),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, color='green', fontweight='bold')

plt.tight_layout()
plt.show()
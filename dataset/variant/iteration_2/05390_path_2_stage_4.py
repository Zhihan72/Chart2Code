import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2024)

# Data for services
service_a = np.array([5, 10, 15, 20, 30, 45, 60, 80, 100, 130, 165])
service_b = np.array([8, 13, 22, 30, 35, 50, 70, 90, 110, 140, 170])
service_c = np.array([2, 3, 5, 8, 15, 25, 35, 50, 75, 105, 140])
service_d = np.array([1, 2, 4, 8, 15, 28, 42, 60, 85, 115, 150])
service_e = np.array([3, 5, 10, 18, 25, 35, 50, 70, 95, 130, 160])
service_f = np.array([6, 12, 18, 25, 33, 47, 65, 85, 105, 135, 175])

fig, ax = plt.subplots(figsize=(12, 8))

line_styles = ['-', '--', '-.', ':', '-', '--']
services = [service_a, service_b, service_c, service_d, service_e, service_f]

single_color = '#1f77b4'  # Blue color

for service, linestyle in zip(services, line_styles):
    ax.plot(years, service, linestyle=linestyle, color=single_color, linewidth=2, marker='o', markersize=6)

# Remove text elements
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 181, 20))

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()
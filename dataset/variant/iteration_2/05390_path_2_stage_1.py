import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2024)

service_a = np.array([5, 10, 15, 20, 30, 45, 60, 80, 100, 130, 165])
service_b = np.array([8, 13, 22, 30, 35, 50, 70, 90, 110, 140, 170])
service_c = np.array([2, 3, 5, 8, 15, 25, 35, 50, 75, 105, 140])
service_d = np.array([1, 2, 4, 8, 15, 28, 42, 60, 85, 115, 150])

fig, ax = plt.subplots(figsize=(12, 8))

line_styles = ['-', '--', '-.', ':']
services = [service_a, service_b, service_c, service_d]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

for service, linestyle, color in zip(services, line_styles, colors):
    ax.plot(years, service, linestyle=linestyle, color=color, linewidth=2, marker='o', markersize=6)

ax.set_title('Growth of Streaming Service Subscriptions (2013-2023)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Subscriptions (Millions)', fontsize=14)
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 181, 20))

# Remove borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()
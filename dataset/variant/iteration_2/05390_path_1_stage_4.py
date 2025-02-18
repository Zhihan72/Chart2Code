import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2024)

service_a = np.array([45, 80, 20, 15, 165, 5, 30, 100, 130, 60, 10])
service_b = np.array([50, 13, 35, 140, 8, 90, 110, 70, 170, 22, 30])
service_c = np.array([25, 2, 35, 140, 5, 3, 50, 8, 15, 75, 105])
service_d = np.array([8, 115, 42, 150, 15, 85, 1, 4, 28, 2, 60])

fig, ax = plt.subplots(figsize=(12, 8))

line_styles = ['-', '--', '-.', ':']
services = [service_a, service_b, service_c, service_d]

uniform_color = '#1f77b4'

for service, linestyle in zip(services, line_styles):
    ax.plot(years, service, linestyle=linestyle, color=uniform_color, linewidth=2, marker='o', markersize=6)

ax.set_title('Subscription Growth (2013-2023)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Subscriptions (M)', fontsize=14)
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 181, 20))

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

for service in services:
    peak_year = 2013 + np.argmax(service)
    peak_value = max(service)
    ax.annotate(f'{peak_value}M', xy=(peak_year, peak_value), xytext=(-10, 10),
                textcoords='offset points', fontsize=10,
                arrowprops=dict(facecolor=uniform_color, arrowstyle='->'),
                bbox=dict(facecolor='white', edgecolor=uniform_color, boxstyle='round,pad=0.3'))

plt.tight_layout()

plt.show()
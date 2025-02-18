import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking the Growth of Streaming Service Subscriptions
# Over the past decade (2013-2023), several streaming services have seen exponential growth in their user base.
# This analysis compares the growth trajectories of four prominent streaming services.

# Define the topic and data for the line chart
years = np.arange(2013, 2024)

# Subscription numbers (millions) for different services
service_a = np.array([5, 10, 15, 20, 30, 45, 60, 80, 100, 130, 165])
service_b = np.array([8, 13, 22, 30, 35, 50, 70, 90, 110, 140, 170])
service_c = np.array([2, 3, 5, 8, 15, 25, 35, 50, 75, 105, 140])
service_d = np.array([1, 2, 4, 8, 15, 28, 42, 60, 85, 115, 150])

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the data
line_styles = ['-', '--', '-.', ':']
services = [service_a, service_b, service_c, service_d]
labels = ['Service A', 'Service B', 'Service C', 'Service D']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

for service, label, linestyle, color in zip(services, labels, line_styles, colors):
    ax.plot(years, service, label=label, linestyle=linestyle, color=color, linewidth=2, marker='o', markersize=6)

# Customize the plot
ax.set_title('Growth of Streaming Service Subscriptions (2013-2023)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Subscriptions (Millions)', fontsize=14)
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 181, 20))
ax.grid(True, linestyle='--', alpha=0.5)

# Add annotations for the peak year
for service, label, color in zip(services, labels, colors):
    peak_year = 2013 + np.argmax(service)
    peak_value = max(service)
    ax.annotate(f'{peak_value}M', xy=(peak_year, peak_value), xytext=(-10, 10),
                textcoords='offset points', fontsize=10,
                arrowprops=dict(facecolor=color, arrowstyle='->'),
                bbox=dict(facecolor='white', edgecolor=color, boxstyle='round,pad=0.3'))

# Set up the legend
ax.legend(loc='upper left', fontsize=12, title='Streaming Services')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()
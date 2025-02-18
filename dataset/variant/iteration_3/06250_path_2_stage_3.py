import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

spring_wind_speeds = np.array([3.2, 2.8, 3.5, 4.0, 3.1, 2.7, 3.8, 3.0, 4.2])
summer_wind_speeds = np.array([2.0, 1.8, 2.2, 2.5, 2.5, 1.9, 2.3, 2.4, 2.1])
autumn_wind_speeds = np.array([4.5, 4.3, 4.6, 5.0, 4.8, 4.7, 4.4, 4.9, 5.1])
winter_wind_speeds = np.array([5.5, 5.2, 5.8, 6.0, 5.6, 5.4, 5.7, 5.3, 6.2])

fig, ax = plt.subplots(2, 2, figsize=(14, 10), sharex=True, sharey=True)
wind_speed_data = [spring_wind_speeds, summer_wind_speeds, autumn_wind_speeds, winter_wind_speeds]
colors = ['green', 'orange', 'brown', 'blue']

for i, (ax_, data, color) in enumerate(zip(ax.flatten(), wind_speed_data, colors)):
    density = gaussian_kde(data)
    y_vals = np.linspace(0, 7, 200)
    x_vals = density(y_vals)

    ax_.plot(x_vals, y_vals, color=color)
    ax_.fill_betweenx(y_vals, 0, x_vals, color=color, alpha=0.3)

plt.tight_layout()
plt.show()
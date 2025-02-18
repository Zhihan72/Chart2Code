import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

coffee_consumption = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
productivity = np.array([5, 11, 6, 10, 8, 3, 12, 9, 11])

coffee_spline = make_interp_spline(coffee_consumption, productivity)
coffee_new = np.linspace(0, 8, 300)
productivity_smooth = coffee_spline(coffee_new)

plt.figure(figsize=(12, 7))
plt.scatter(coffee_consumption, productivity, color='blue', s=100, edgecolor='black')
plt.plot(coffee_new, productivity_smooth, color='orange', linestyle='-', linewidth=2, alpha=0.7)

plt.title('Tech Productivity vs Daily Coffee Intake', fontsize=16, fontweight='bold')
plt.xlabel('Cups of Coffee (Daily)', fontsize=12)
plt.ylabel('Tasks Done per Day', fontsize=12)

plt.xticks(np.arange(0, 9, step=1))
plt.yticks(np.arange(2, 14, step=2))
plt.tight_layout()
plt.show()
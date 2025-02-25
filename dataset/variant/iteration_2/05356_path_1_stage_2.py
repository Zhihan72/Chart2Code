import matplotlib.pyplot as plt
import numpy as np

# Decades and contributors
decades = ['90s', '00s', '10s', '20s', '30s', '40s']
contributors = ['Res PV', 'Com PV', 'Util PV', 'CSP']

# Solar adoption data
solar_adoption = np.array([
    [20, 40, 30, 10],
    [30, 25, 35, 10],
    [30, 30, 10, 30],
    [10, 35, 25, 30],
    [40, 25, 20, 15],
    [15, 50, 20, 15]
])

# Create a stacked area chart
plt.figure(figsize=(14, 8))
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
plt.stackplot(decades, solar_adoption.T, labels=contributors, colors=colors, alpha=0.85)

# Chart details
plt.title("Solar Tech Adoption (90s-40s)", fontsize=16, fontweight='bold')
plt.xlabel('Decades', fontsize=12)
plt.ylabel('Solar Contribution (%)', fontsize=12)
plt.xticks(rotation=45)
plt.legend(loc='upper left', title='Contributors', bbox_to_anchor=(1.05, 1), borderaxespad=0)
plt.grid(True, linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Display plot
plt.show()
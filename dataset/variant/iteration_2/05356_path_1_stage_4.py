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

plt.figure(figsize=(14, 8))
colors = ['#ffcc99','#99ff99','#66b3ff','#ff9999']

# Stacked area chart without stylistic elements
plt.stackplot(decades, solar_adoption.T, colors=colors, alpha=0.85)

# Chart details
plt.title("Solar Tech Adoption (90s-40s)", fontsize=16, fontweight='bold')
plt.xlabel('Decades', fontsize=12)
plt.ylabel('Solar Contribution (%)', fontsize=12)
plt.xticks(rotation=45)

# Display plot
plt.show()
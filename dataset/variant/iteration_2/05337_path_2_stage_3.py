import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Manually altered specific data points to randomize content while keeping structure
alice_running = [55, 52, 60, 58, 62, 50, 68, 72, 75, 80, 65, 85]
bob_running = [40, 47, 45, 52, 55, 57, 50, 65, 70, 75, 60, 80]
charlie_running = [35, 30, 40, 50, 55, 45, 60, 65, 72, 70, 80, 75]

alice_gym = [10, 8, 12, 14, 15, 16, 18, 22, 20, 27, 25, 23]
bob_gym = [7, 5, 11, 13, 9, 15, 18, 16, 24, 22, 20, 26]
charlie_gym = [6, 4, 10, 8, 13, 11, 15, 17, 22, 18, 20, 19]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

ax1.plot(months, alice_running, marker='o', linestyle='-', color='blue')
ax1.plot(months, bob_running, marker='s', linestyle='--', color='green')
ax1.plot(months, charlie_running, marker='^', linestyle='-.', color='red')

ax2.plot(months, alice_gym, marker='o', linestyle='-', color='blue')
ax2.plot(months, bob_gym, marker='s', linestyle='--', color='green')
ax2.plot(months, charlie_gym, marker='^', linestyle='-.', color='red')

plt.tight_layout()
plt.show()
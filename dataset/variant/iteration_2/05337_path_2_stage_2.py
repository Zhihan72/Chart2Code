import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

alice_running = [50, 52, 55, 60, 58, 62, 65, 68, 72, 75, 80, 85]
bob_running = [40, 45, 47, 50, 52, 55, 57, 60, 65, 70, 75, 80]
charlie_running = [30, 35, 40, 45, 50, 55, 60, 65, 70, 72, 75, 80]

alice_gym = [8, 10, 12, 15, 14, 16, 18, 20, 22, 23, 25, 27]
bob_gym = [5, 7, 9, 11, 13, 15, 16, 18, 20, 22, 24, 26]
charlie_gym = [4, 6, 8, 10, 11, 13, 15, 17, 18, 19, 20, 22]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

ax1.plot(months, alice_running, marker='o', linestyle='-', color='blue')
ax1.plot(months, bob_running, marker='s', linestyle='--', color='green')
ax1.plot(months, charlie_running, marker='^', linestyle='-.', color='red')

ax2.plot(months, alice_gym, marker='o', linestyle='-', color='blue')
ax2.plot(months, bob_gym, marker='s', linestyle='--', color='green')
ax2.plot(months, charlie_gym, marker='^', linestyle='-.', color='red')

plt.tight_layout()
plt.show()
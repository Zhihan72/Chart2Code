import matplotlib.pyplot as plt
import numpy as np

days = np.array(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
probe_A = np.array([250, 245, 243, 240, 242, 244, 248])
probe_B = np.array([252, 247, 245, 243, 244, 247, 251])
probe_C = np.array([249, 245, 244, 241, 243, 246, 250])
probe_D = np.array([253, 248, 246, 244, 245, 248, 252])
probe_E = np.array([251, 246, 244, 242, 243, 245, 249])

fig, ax1 = plt.subplots(figsize=(14, 8))

# Define unique colors for each line
colors = ['royalblue', 'forestgreen', 'orangered', 'purple', 'darkorange']

# Plot each probe with unique markers and colors
ax1.plot(days, probe_A, '-o', color=colors[0], markersize=6, linewidth=2, markerfacecolor=colors[0])
ax1.plot(days, probe_B, '-s', color=colors[1], markersize=6, linewidth=2, markerfacecolor=colors[1])
ax1.plot(days, probe_C, '-^', color=colors[2], markersize=6, linewidth=2, markerfacecolor=colors[2])
ax1.plot(days, probe_D, '-d', color=colors[3], markersize=6, linewidth=2, markerfacecolor=colors[3])
ax1.plot(days, probe_E, '-p', color=colors[4], markersize=6, linewidth=2, markerfacecolor=colors[4])

ax1.set_xticks(np.arange(len(days)))
ax1.set_xticklabels(days)

plt.show()
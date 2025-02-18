import matplotlib.pyplot as plt

daceds = ['2030s', '2020s', '2000s', '2010s', '2040s']  # Changed order
findings = [15, 45, 80, 60, 30]  # Shuffled discoveries
trips = [75, 10, 35, 55, 20]  # Shuffled missions
inquiries = [40, 5, 70, 50, 25]  # Shuffled research

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(daceds, findings, marker='o', linestyle='-', color='b', linewidth=2, markersize=8, label='Findings')
ax.plot(daceds, trips, marker='s', linestyle='--', color='g', linewidth=2, markersize=8, label='Trips')
ax.plot(daceds, inquiries, marker='^', linestyle=':', color='r', linewidth=2, markersize=8, label='Inquiries')

ax.set_xlabel('Era', fontsize=12, labelpad=10)  # Changed from 'Decade'
ax.set_ylabel('Numbers', fontsize=12, labelpad=10)  # Shortened label
ax.set_title('Cosmic Exploration:\nFindings, Trips, and Inquiries Through Time', fontsize=16, pad=20)

ax.legend()

plt.tight_layout()
plt.show()
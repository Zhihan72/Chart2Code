import matplotlib.pyplot as plt
import numpy as np

quarters = np.arange(2010, 2020.75, 0.25)

lingualeap_users = np.array([3.5, 0.7, 18.5, 1.0, 15.5, 18.0, 1.4, 12.5, 9.0, 1.5, 1.2, 20.0, 3.0, 0.5, 12.0, 13.0, 8.5, 6.5, 13.0, 12.0, 2.5, 15.0, 9.5, 6.0, 14.0, 21.5, 3.5, 3.0, 11.0, 6.5, 4.0, 5.5, 7.5, 16.0, 16.5, 10.0, 5.0, 21.0, 10.0, 2.0, 22.0, 19.5, 19.0])
polyglotpro_users = np.array([1.8, 0.6, 26.0, 8.0, 28.0, 3.0, 2.5, 27.0, 1.2, 11.0, 2.0, 1.0, 10.0, 7.0, 6.5, 14.0, 4.0, 9.0, 17.0, 2.0, 30.0, 30.0, 13.5, 13.5, 11.0, 0.3, 16.0, 5.5, 15.0, 19.5, 12.0, 18.5, 18.5, 14.0, 29.5, 0.4, 21.0, 6.0, 0.2, 24.0, 1.4, 7.5, 2.5])
verboventures_users = np.array([2.5, 0.2, 3.0, 1.5, 13.5, 2.0, 1.5, 9.0, 5.5, 4.5, 8.5, 2.5, 11.5, 9.0, 21.5, 10.5, 3.0, 13.5, 10.5, 15.0, 7.5, 0.4, 18.5, 0.5, 13.0, 21.5, 9.0, 18.0, 1.0, 15.0, 11.0, 7.0, 8.0, 1.5, 12.0, 4.5, 8.0, 5.5, 13.0, 14.0, 17.0, 3.5, 16.0])

fig, ax = plt.subplots(1, 2, figsize=(14, 10), sharex=True)

color = '#ff5733'

ax[0].plot(quarters, lingualeap_users, marker='x', linestyle=':', color=color, linewidth=2, label='LinguaLeap')
ax[0].plot(quarters, polyglotpro_users, marker='d', linestyle='-', color=color, linewidth=3, label='PolyglotPro')
ax[0].plot(quarters, verboventures_users, marker='v', linestyle='--', color=color, linewidth=1, label='VerboVentures')

lingualeap_rate = np.gradient(lingualeap_users)
polyglotpro_rate = np.gradient(polyglotpro_users)
verboventures_rate = np.gradient(verboventures_users)

ax[1].plot(quarters, lingualeap_rate, marker='x', linestyle=':', color=color, linewidth=1, label='LinguaLeap Growth')
ax[1].plot(quarters, polyglotpro_rate, marker='d', linestyle='-', color=color, linewidth=2, label='PolyglotPro Growth')
ax[1].plot(quarters, verboventures_rate, marker='v', linestyle='--', color=color, linewidth=1.5, label='VerboVentures Growth')

ax[0].set_title('App Users\n(2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax[0].set_ylabel('Users (M)', fontsize=12)
ax[1].set_title('Growth Rate (Millions)', fontsize=14, fontweight='bold', pad=20)
ax[1].set_xlabel('Year', fontsize=12)
ax[1].set_ylabel('Rate (M/Q)', fontsize=12)

ax[1].set_xticks(quarters[::4])
ax[1].set_xticklabels(range(2010, 2021), rotation=45)

ax[0].legend(title='Apps', loc='upper right', fontsize=11)
ax[1].legend(title='Growth', loc='lower left', fontsize=11)

annotations_users = {
    2015: ("Launch", lingualeap_users[20]),
    2018: ("Partnerships", polyglotpro_users[32]),
    2020: ("Growth", verboventures_users[42]),
}

for year, (text, y_value) in annotations_users.items():
    ax[0].annotate(text, xy=(year, y_value), xytext=(year, y_value + 2),
                   arrowprops=dict(facecolor='gray', shrink=0.05, width=1.5, headwidth=6),
                   fontsize=9, color='blue', ha='center')

ax[0].grid(True, linestyle=':', alpha=0.8)
ax[1].grid(True, linestyle='-.', alpha=0.5)

plt.tight_layout()
plt.show()
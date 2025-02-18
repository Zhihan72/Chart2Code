import matplotlib.pyplot as plt

# Shuffled colors for each transport mode
transport_modes = ['Airplanes', 'Cycling', 'Buses', 'Feet', 'Automobiles', 'Miscellaneous', 'EVs']
mode_shares = [30, 15, 20, 10, 10, 5, 10]
shuffled_colors = ['#808080', '#1E90FF', '#4B0082', '#FF6347', '#FFD700', '#228B22', '#8B0000']
explode = (0, 0.1, 0, 0, 0, 0, 0.1)

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(mode_shares, labels=transport_modes, colors=shuffled_colors, explode=explode,
                                  autopct='%1.1f%%', startangle=140, wedgeprops=dict(width=0.3))

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')
    autotext.set_fontsize(10)

ax.set_title("Transportation Trends:\n Shadows of 2023 Mobility", fontsize=16, fontweight='bold')

plt.show()
import matplotlib.pyplot as plt

transport_modes = ['Airplanes', 'Cycling', 'Buses', 'Feet', 'Automobiles', 'Miscellaneous', 'EVs']
mode_shares = [30, 15, 20, 10, 10, 5, 10]
colors = ['#8B0000', '#228B22', '#1E90FF', '#FFD700', '#FF6347', '#808080', '#4B0082']
explode = (0, 0.1, 0, 0, 0, 0, 0.1)

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(mode_shares, labels=transport_modes, colors=colors, explode=explode,
                                  autopct='%1.1f%%', startangle=140, wedgeprops=dict(width=0.3))

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')
    autotext.set_fontsize(10)

ax.set_title("Transportation Trends:\n Shadows of 2023 Mobility", fontsize=16, fontweight='bold')

plt.show()
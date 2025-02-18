import matplotlib.pyplot as plt

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
chrome_usage = [130, 115, 120, 180, 125, 140, 160]
firefox_usage = [70, 65, 50, 60, 55, 85, 90]
edge_usage = [10, 25, 20, 35, 30, 15, 20]

fig, ax = plt.subplots(figsize=(14, 10))

colors = ['#FF5733', '#FFC300', '#C70039']

ax.bar(days, chrome_usage, color=colors[0])
ax.bar(days, firefox_usage, bottom=chrome_usage, color=colors[1])
ax.bar(days, edge_usage, bottom=[c+f for c, f in zip(chrome_usage, firefox_usage)], color=colors[2])

ax.set_xticks([])
ax.set_yticks([])
ax.legend().set_visible(False)

plt.show()
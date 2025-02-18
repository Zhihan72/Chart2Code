import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
python = np.array([10, 15, 20, 25, 30, 40, 50, 55, 60, 65, 70])
javascript = np.array([30, 35, 40, 50, 55, 60, 60, 62, 65, 68, 70])
java = np.array([50, 45, 40, 35, 30, 25, 20, 20, 18, 17, 15])
csharp = np.array([5, 5, 5, 6, 7, 8, 8, 10, 12, 13, 15])
ruby = np.array([5, 5, 5, 5, 5, 7, 9, 8, 5, 4, 3])

bar_width = 0.15
r1 = np.arange(len(years))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]
r5 = [x + bar_width for x in r4]

fig, ax = plt.subplots(figsize=(12, 8))

ax.bar(r1, python, color='#306998', width=bar_width, label='Python', alpha=0.8)
ax.bar(r2, javascript, color='#F7DF1E', width=bar_width, label='JavaScript', alpha=0.8)
ax.bar(r3, java, color='#b07219', width=bar_width, label='Java', alpha=0.8)
ax.bar(r4, csharp, color='#178600', width=bar_width, label='C#', alpha=0.8)
ax.bar(r5, ruby, color='#701516', width=bar_width, label='Ruby', alpha=0.8)

ax.set_title("Popular Programming Languages Over Years")
ax.set_xlabel("Years")
ax.set_ylabel("Usage Popularity")
ax.set_xticks([r + 2 * bar_width for r in range(len(years))])
ax.set_xticklabels(years, rotation=45, ha="right")
ax.legend()

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
python = np.array([10, 15, 20, 25, 30, 40, 50, 55, 60, 65, 70])
javascript = np.array([30, 35, 40, 50, 55, 60, 60, 62, 65, 68, 70])
java = np.array([50, 45, 40, 35, 30, 25, 20, 20, 18, 17, 15])
csharp = np.array([5, 5, 5, 6, 7, 8, 8, 10, 12, 13, 15])
ruby = np.array([5, 5, 5, 5, 5, 7, 9, 8, 5, 4, 3])

bottom_js = python
bottom_java = bottom_js + javascript
bottom_csharp = bottom_java + java
bottom_ruby = bottom_csharp + csharp

fig, ax = plt.subplots(figsize=(12, 8))

ax.bar(years, python, color='#306998', width=0.6, alpha=0.8)
ax.bar(years, javascript, bottom=bottom_js, color='#F7DF1E', width=0.6, alpha=0.8)
ax.bar(years, java, bottom=bottom_java, color='#b07219', width=0.6, alpha=0.8)
ax.bar(years, csharp, bottom=bottom_csharp, color='#178600', width=0.6, alpha=0.8)
ax.bar(years, ruby, bottom=bottom_ruby, color='#701516', width=0.6, alpha=0.8)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha="right")

plt.tight_layout()
plt.show()
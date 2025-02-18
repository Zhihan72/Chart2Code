import matplotlib.pyplot as plt

# Data series
percentages = [25, 35, 15, 10, 15, 8, 12]
colors = ['#e377c2', '#8c564b', '#d62728', '#2ca02c', '#ff7f0e', '#9467bd', '#1f77b4']
markers = 'o^s*Dxv'
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

fig, ax = plt.subplots(figsize=(8, 8))

# Create pie chart with altered styles
wedges, texts, autotexts = ax.pie(percentages, labels=labels, startangle=90, colors=colors, autopct='%1.1f%%',
       wedgeprops={'linestyle': '-', 'linewidth': 2}, pctdistance=0.85)

# Style autotexts
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)

# Style texts
for text, marker in zip(texts, markers):
    text.set_color('black')
    text.set_fontsize(10)
    text.set_fontweight('bold')

ax.legend(loc='upper right', fontsize=10, shadow=True, title="Legend", title_fontsize=12)
ax.set_facecolor('#f9f9f9')
ax.grid(linestyle='--', alpha=0.5)

plt.show()
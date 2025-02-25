import matplotlib.pyplot as plt
import numpy as np

flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Cookie Dough', 'Rocky Road', 'Pistachio']
percentages = [30, 25, 15, 10, 10, 5, 5]
colors = ['#f3e5ab', '#7b3f00', '#ff69b4', '#98fb98', '#d2b48c', '#bc8f8f', '#93c572']
explode = (0.1, 0, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    percentages,
    labels=flavors,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    shadow=True
)

for text in texts:
    text.set_fontsize(12)
for autotext in autotexts:
    autotext.set_fontsize(11)
    autotext.set_color('black')

ax.axis('equal')
plt.show()
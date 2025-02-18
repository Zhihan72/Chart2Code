import matplotlib.pyplot as plt

user_percentages = [22, 18, 25, 15, 10, 10]

# New set of colors
colors = ['#FF5733', '#33FFBD', '#335BFF', '#F5FF33', '#9333FF', '#FF3380']

plt.figure(figsize=(10, 7))
wedges, _, autotexts = plt.pie(
    user_percentages, 
    colors=colors, 
    startangle=140, 
    wedgeprops=dict(width=0.3, edgecolor='w'),
    autopct='%1.1f%%', 
    pctdistance=0.85
)

center_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(center_circle)

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontweight('bold')

plt.axis('equal')
plt.tight_layout()
plt.show()
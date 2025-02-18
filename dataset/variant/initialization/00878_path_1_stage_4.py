import matplotlib.pyplot as plt

modes = ['Transit', 'Ride', 'Bike', 'Scooter', 'Loop', 'Fly Taxi', 'Walk', 'Self-Drive', 'Drone']
percentages = [20, 15, 10, 5, 10, 5, 5, 20, 10]

colors = ['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF33A6', '#A633FF', '#FF3333', '#33FFF5', '#F5A623']

explode = (0, 0, 0, 0, 0.1, 0, 0, 0, 0)

plt.figure(figsize=(10, 7))
wedges, texts, autotexts = plt.pie(
    percentages, labels=modes, colors=colors, explode=explode,
    autopct='%1.1f%%', startangle=140
)

for text in texts:
    text.set_fontsize(11)
    text.set_fontweight('bold')

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

plt.axis('equal')
plt.title('Urban Transport: 2035 Mode', fontsize=14, fontweight='bold', ha='center')
plt.legend(wedges, modes, title="Modes", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.tight_layout()
plt.show()
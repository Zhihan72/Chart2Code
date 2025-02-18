import matplotlib.pyplot as plt

objectives = ['Pollution', 'Resource', 'Biodiversity', 'Climate', 'Research']
proportions = [10, 25, 20, 15, 30]
single_color = '#66B3FF'

fig, ax = plt.subplots(figsize=(9, 9))
wedges, texts, autotexts = ax.pie(
    proportions,
    labels=objectives,
    autopct='%1.1f%%',
    startangle=100,
    colors=[single_color]*len(proportions),
    explode=(0.1, 0, 0.1, 0.1, 0),
    shadow=False,
    textprops=dict(color="black"),
    wedgeprops=dict(edgecolor='grey', linewidth=1, width=0.3)  # Setting the width to create a donut chart
)

plt.title("Ocean Mission", fontsize=14, fontweight='medium', pad=10)
plt.setp(autotexts, size=9, fontweight="light")

ax.legend(wedges, objectives, title="Goals", loc="upper left", bbox_to_anchor=(0.9, 0.9))

plt.show()
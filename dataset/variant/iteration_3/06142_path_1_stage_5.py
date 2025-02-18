import matplotlib.pyplot as plt

transport_modes = ["Bikes", "Cars", "Walk", "M-cycles", 
                   "Transit", "Oth.", "Scoot.", "Skatebd."]
percentages = [20, 18, 25, 8, 12, 5, 7, 5]
colors = ['#66b3ff', '#ff9999', '#99ff99', '#ffcc99', 
          '#c2c2f0', '#ffb3e6', '#c0c0c0', '#ffbf00']

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(percentages, labels=transport_modes, autopct='%1.1f%%', startangle=90, colors=colors)

for text in texts:
    text.set_size(10)

for autotext in autotexts:
    autotext.set_size(10)
    autotext.set_color('darkgrey')

plt.show()
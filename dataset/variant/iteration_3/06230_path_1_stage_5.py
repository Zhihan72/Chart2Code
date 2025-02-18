import matplotlib.pyplot as plt

flavors = ['Cherry', 'Blueberry', 'Watermelon', 'Kiwi', 'Mango', 'Peach', 'Strawberry', 'Pineapple']
preferences = [300, 200, 150, 100, 150, 100, 180, 120]

# Applying a single consistent color for all data groups
single_color = ['#FF9999']

fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

explode = [0.1 if i == max(preferences) else 0 for i in preferences]

wedges, texts, autotexts = ax.pie(
    preferences, explode=explode, colors=single_color * len(preferences), autopct='%1.1f%%',
    startangle=140, textprops={'fontsize': 9, 'color': 'black'}
)

plt.show()
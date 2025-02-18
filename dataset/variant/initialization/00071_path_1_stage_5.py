import matplotlib.pyplot as plt

# Shortened genre names
genres = ['Fic', 'Non-Fic', 'Mys', 'Sci-Fi', 'Rom', 'Fant']
overall_preference = [35, 25, 20, 10, 10, 15]

single_color = '#4682B4'

fig, ax = plt.subplots(figsize=(10, 8))

# Using shorter genre labels
wedges, texts, autotexts = ax.pie(overall_preference, labels=genres, colors=[single_color]*len(genres),
                                  startangle=60, autopct='%1.1f%%')

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_weight('bold')

# Shortened chart title
plt.title("Genre Preferences", fontsize=16, weight='bold')
plt.tight_layout()
plt.show()
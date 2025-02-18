import matplotlib.pyplot as plt

genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Science Fiction', 'Romance', 'Fantasy']
overall_preference = [35, 25, 20, 10, 10, 15]

single_color = '#4682B4'

fig, ax = plt.subplots(figsize=(10, 8))

wedges, texts, autotexts = ax.pie(overall_preference, labels=genres, colors=[single_color]*len(genres),
                                  startangle=60, autopct='%1.1f%%')

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_weight('bold')

plt.title("Literary Preferences by Genre", fontsize=16, weight='bold')
plt.tight_layout()
plt.show()
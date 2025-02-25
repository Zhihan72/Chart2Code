import matplotlib.pyplot as plt

genres = ['Fantasy', 'Non-fiction', 'Historical', 'Science Fiction', 'Mystery', 'Fiction']
genre_distribution = [25, 20, 15, 15, 10, 15]

age_groups = ['30-39', '10-19', '0-9', '50-59', '60+', '40-49', '20-29']
books_read = [8, 5, 2, 11, 13, 9, 7]
variability = [0.5, 1, 1.5, 1.2, 1.3, 1.6, 2]

single_color = '#4CAF50'

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))

bars = ax1.barh(age_groups, books_read, color=single_color, edgecolor='black', 
                height=0.6, xerr=variability, capsize=5)
ax1.set_title('Which Books Did They Read in 2023?\nExploring Literary Taste by Generations', 
              fontsize=14, fontweight='bold', pad=20)
ax1.set_xlabel('Books Consumed Per Year', fontsize=12)

for bar in bars:
    width = bar.get_width()
    ax1.text(width + 0.3, bar.get_y() + bar.get_height() / 2, f'{width} reads', 
             va='center', ha='left', fontsize=10, color='darkblue')

ax1.tick_params(axis='y', labelsize=12)
ax1.xaxis.grid(True, linestyle='--', alpha=0.6)

wedges, texts, autotexts = ax2.pie(genre_distribution, labels=genres, autopct='%1.1f%%', startangle=90, 
                                   colors=[single_color] * len(genres), wedgeprops={'edgecolor': 'black'})
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

ax2.set_title('Beloved Genres: A Peek at Preferences from Seasoned Readers', fontsize=14, fontweight='bold')
ax2.axis('equal') 

plt.tight_layout()
plt.subplots_adjust(wspace=0.4)
plt.show()
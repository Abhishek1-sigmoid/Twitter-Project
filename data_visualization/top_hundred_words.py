from matplotlib import pyplot as plt
from wordcloud import WordCloud
import sys
sys.path.append("../")
from queries.top_hundred_words import top_hundred_words


def show_words():
    word_count = top_hundred_words()
    words_list = word_count['top_hundred_words']
    words_str = ''
    for word in words_list:
        words_str = word['word']+" "+words_str
    plt.figure(figsize=(8, 8))
    wc = WordCloud(max_words=100, width=800, height=800,background_color ='black').generate(words_str)
    plt.imshow(wc)
    plt.savefig('Top_100_words.png')
    plt.show()


if __name__ == '__main__':
    show_words()

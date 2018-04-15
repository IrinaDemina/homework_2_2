# -*- coding: utf-8 -*-
import chardet


def get_top_ten_words(text):
    words_dict = {}
    for element in text.split():
        word = element.lower()
        if len(word) > 6:
            if word not in words_dict:
                words_dict[word] = 1
            else:
                words_dict[word] += 1

    sorted_words = sorted(words_dict.items(), key=lambda x: -x[1])
    i = 1
    for word_item in sorted_words:
        if i <= 10:
            print(word_item[0], "-", word_item[1])
            i += 1
        else:
            break


def create_news_list():
    news_list = ["newsafr.txt", "newscy.txt", "newsfr.txt", "newsit.txt"]
    for news_file in news_list:
        with open(news_file, "rb") as f:
            data = f.read()
            result = chardet.detect(data)
            text = data.decode(result["encoding"])
            print(news_file, "топ 10 слов:")
            get_top_ten_words(text)


create_news_list()

import xml.etree.ElementTree as fun
from collections import Counter

def main():
    news = []
    f = fun.parse('123.xml')
    root = f.getroot()
    descriptions = root.findall('channel/item/description')
    for text in descriptions:
        news.append(text.text)
    output = Counter(support(news))
    print(output.most_common(1))

def support(list):
    news_str = ''
    for news in list:
        news_str += news
    news_strs = news_str.split()
    news_strs.sort(key=len, reverse=True)
    output_list = []
    for word in news_strs:
        if len(word) >= 6:
            output_list.append(word)
    return output_list

main()
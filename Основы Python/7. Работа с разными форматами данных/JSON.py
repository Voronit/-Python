import json
from collections import Counter

def main():
    f = open("json.json")
    news = json.load(f)
    output = Counter(support(news))
    print(output.most_common(1))


def support(_json):
    news_str = ''
    for news in _json['rss']['channel']['items']:
        news_str += news['description']
    news_strs = news_str.split()
    news_strs.sort(key=len, reverse=True)
    output_list = []
    for word in news_strs:
        if len(word) >= 6:
            output_list.append(word)
    return output_list

main()
#!/usr/bin/python
# coding=utf-8
# 采用TextRank方法提取文本关键词
import pandas as pd
from textrank4zh import TextRank4Keyword, TextRank4Sentence


# 处理标题和摘要，提取关键词
def getKeywords_textrank4zh(data,topK):
    idList,titleList,summaryList = data['id'],data['title'],data['summary']
    ids, titles, keys = [], [], []
    for index in range(len(idList)):
        text = '%s。%s' % (titleList[index], summaryList[index]) # 拼接标题和摘要
        print("\"",titleList[index],"\"" , " 10 Keywords - TextRank :")
        tr4w = TextRank4Keyword()
        tr4w.analyze(text, lower=True)
        print('关键词为：')
        for item in tr4w.get_keywords(num=topK, word_min_len=1):
            print(item.word, item.weight)
        print('\n')
        print('关键短语为：')
        for phrase in tr4w.get_keyphrases(keywords_num=topK, min_occur_num=2):
            print(phrase)
        print('\n')
        tr4s = TextRank4Sentence()
        tr4s.analyze(text=text, lower=True, source='all_filters')
        print('关键句为：')
        for item in tr4s.get_key_sentences(num=3):
            print(item.index, item.weight, item.sentence)
        print('\n')
    return 0


def main():
    dataFile = 'data/qyd_out.csv'
    data = pd.read_csv(dataFile,encoding='gbk')
    result = getKeywords_textrank4zh(data,10)

if __name__ == '__main__':
    main()

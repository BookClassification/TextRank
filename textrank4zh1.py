#!/usr/bin/python
# coding=utf-8
# 采用TextRank方法提取文本关键词
import pandas as pd
from textrank4zh import TextRank4Keyword


# 处理标题和摘要，提取关键词
def getKeywords_textrank4zh(data,topK):
    idList,titleList,summaryList = data['id'],data['title'],data['summary']
    ids, titles, keys = [], [], []
    for index in range(len(idList)):
        text = '%s。%s' % (titleList[index], summaryList[index]) # 拼接标题和摘要
        print("\"",titleList[index],"\"" , " 10 Keywords - TextRank :")
        tr4w = TextRank4Keyword()
        tr4w.analyze(text, lower=True)
        keylist = []
        key_words = tr4w.get_keywords(num=topK, word_min_len=1)
        print('关键词为：')
        for item in key_words:
            print(item.word, item.weight)
            keylist.append(item.word)
            word_split = " ".join(keylist)
        keys.append(word_split)
        ids.append(idList[index])
        titles.append(titleList[index])

    result = pd.DataFrame({"id": ids, "title": titles, "key": keys}, columns=['id', 'title', 'key'])
    return result


def main():
    dataFile = 'data/qyd_out.csv'
    data = pd.read_csv(dataFile,encoding='gbk')
    result = getKeywords_textrank4zh(data,10)
    result.to_csv("result/TextRank4ZH_out.csv",index=False)

if __name__ == '__main__':
    main()

import requests
import pickle
from Crypto.Hash import MD5
import bs4


def toHash(msg):
    return MD5.new(msg.encode("utf-8")).hexdigest()

f=open("Hash_CV.ser","wb")
list=[]
res = requests.get(
    'https://timesofindia.indiatimes.com/india/coronavirus-live-news-updates-total-number-of-confirmed-coronavirus-cases-in-india-20-march-2020/liveblog/74721127.cms')
html = bs4.BeautifulSoup(res.text, "html.parser")
news = html.select('._1KydD')
for n in range(5):
    list.append(news[n].select_one('p').text.lower())

list=list[::-1]
print(list)
pickle.dump(list,f)
f.close()



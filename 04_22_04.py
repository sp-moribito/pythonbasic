import requests
from bs4 import BeautifulSoup

#url="https://upbit.com/exchange?code=CRIX.UPBIT.KRW-ETC"
url="https://www.bithumb.com/"
html=requests.get(url).text

soup=BeautifulSoup(html,"html5lib")
#tags=soup.select("#UpbitLayout>div:nth-child(4)>div>sector")
tag=soup.select("#assetRealBTC_KRW")[0]
print(tag.text)
tag=soup.select("#assetRealETH_KRW")[0]
print(tag.text)

# for tag in tags:
#     print(tag.text)
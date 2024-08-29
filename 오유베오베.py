# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(1,10):
        try:
                #오유 념글 주소 
                data = 'https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
                print(data)
                #웹브라우져 헤더 추가 
                req = urllib.request.Request(data, headers = hdr)
                data = urllib.request.urlopen(req).read()
                #한글이 깨지면 디코딩
                page = data.decode('utf-8', 'ignore')
                soup = BeautifulSoup(page, 'html.parser')
                list = soup.find_all('td', attrs={'class':'subject'})

# <a href="/board/view.php?table=bestofbest&amp;no=476685&amp;s_no=476685&amp;page=1" target="_top">긍정적인 삶 vs 부정적인 삶 vs 내 삶.jpg</a>

                for item in list:
                        try:
                                title = item.find("a").text.strip()
                                href = item.find("a")["href"]
                                # print(title)
                                if (re.search('한국', title)):
                                        print(title)
                                        print(href)
                        except:
                                pass
        except:
                pass 

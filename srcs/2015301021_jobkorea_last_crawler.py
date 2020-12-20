import urllib.request ## url 
import re ## html 태그 제거 
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from wordcloud import WordCloud
import matplotlib.pyplot as plt 
import nltk 
from nltk.corpus import stopwords
from collections import Counter
import matplotlib 
from IPython.display import set_matplotlib_formats

matplotlib.rc('font',family = 'Malgun Gothic') 
set_matplotlib_formats('retina') 
matplotlib.rc('axes',unicode_minus = False)

stop_words = ['개인','이력서','회원','관리','입사','이력서',
            '열람','기업','스마트','매치','스크랩','기업','회원',
            '서비스','안내','서치','펌','신규','등록','공채','실시간',
            '신입','큐','레이','션','콘텐츠','최근','실', '이', '에', 
            '홈','채용','공고','지원','인재','검색','현황','일반','면접',
            '전체','것','임원','토론','인성','전','엠','단','탈','자','소서',
            '지원동','대해','편','안','수','말','적','때','낼','폴리오',
            '점','즐','알','중','더','리','내','명','사','찬',
            '후','꼬','관','졸','어보','시오','건가','워','밸',
            '번','비','터','땐','입','체','을','몇','등','는','의',
            '곳','에','개','공','직','각','외','업','윷',
            '방','차','면','안나','법쪽','무','못','쪽',
            '철','합','는가','무었',
            '을', '가', '도', '와', '1', '저', '다', '를', '들', '은', '과', '그'] 

## url 설정
noun_list = []
cnt = 0
# 잡코리아 봇 수집 방지 정책으로 인해 70개 이상 한번에 수집이 어려웠습니다.
# 500개정도까지 수작업으로 결과물을 비교해보니 큰 차이가 없어서 표본 갯수를 70개로 선택하였습니다.
for num in range(1,70):
    url='https://www.jobkorea.co.kr/Starter/Review/view?C_Idx=%s&Half_Year_Type_Code=0&Ctgr_Code=4&FavorCo_Stat=0&G_ID=0&Page=1' % str(num)
    webpage=urllib.request.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(webpage, 'html.parser') #분석 용이하게 파싱
    blog_list = []
    cnt += 1
    print(cnt)
    for n in soup.find_all('ul', attrs={'class':'lists'}):
        blog_list.append(n.get_text())
    for n in blog_list :
        n = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"\\n\\r]','',n)
        okt = Okt()
        n = okt.nouns(n)
        #n = okt.morphs(n)
        k = [each_word for each_word in n if each_word not in stop_words]
        if k:
            for p in k:
                noun_list.append(p)
            
                  
count = Counter(noun_list)
words = dict(count.most_common())
wordcloud = WordCloud(font_path = 'C:/Windows/Fonts/malgun.ttf', background_color='white',colormap = "Accent_r", width=1500, height=1000).generate_from_frequencies(words) 
plt.imshow(wordcloud) 
plt.axis('off') 
plt.show()

#1~4012
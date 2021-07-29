from django.shortcuts import render
from .models import *
import requests
from bs4 import BeautifulSoup
import re



def index(request):
    titles = {}
    links = {}
    texts = {}
    infos = {}
    url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%BD%94%EB%A1%9C%EB%82%9819'
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml" )

    # info추출 
    contents = soup.find_all("a",attrs={"class":"info press"})
    for i , t in enumerate(contents):
        ele=  t.get_text()
        
        if '언론사 선정' in ele:
            ln = len(ele)
            ele = ele[0:ln-6]
        infos[i] = ele


    # title 추출 
    contents = soup.find_all("a",attrs={"class":"news_tit"})
    for i , t in enumerate(contents):
        titles[i] = t.get_text()

    # text 추출 
    contents = soup.find_all("a",attrs={"class":"api_txt_lines dsc_txt_wrap"})
    for i , t in enumerate(contents):
        texts[i] = t.get_text()

    # links 추출 
    contents = soup.find_all("div",attrs={"class":"dsc_wrap"})
    for i , t in enumerate(contents):
        link = t.a["href"]
        links[i] = link
    
    content = {'title':titles , 'link':links , 'text':texts , 'info': infos}
    status =  {'status_t':'deactive' ,'status_c':'active', 'status_g':'deactive'}
    dic = {'first':status, 'second':content}
   
    return render(request,'app/index.html', dic)

def clean_text(text):
    nospace = re.sub('&nbsp;| |\t|\n', ' ', text)
    nospace = re.sub('  ', '', nospace)
    return nospace
    
def Trend(request):
    titles = {}
    links = {}
    texts = {}
    infos = {}
    url = 'https://www.itworld.co.kr/news' 
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml" )

    # title추출 
    contents = soup.find_all("h4",attrs={"class":"news_list_full_size news_list_title default_font font_bold font_limit title_h3"})
    for i , t in enumerate(contents):
        ele = t.get_text()
        ele = clean_text(ele)
        titles[i] = ele    
    print(titles)

    # text 추출 
    contents = soup.find_all("div",attrs={"class":"news_body_summary font_14 cl"})
    for i , t in enumerate(contents):
        ele = t.get_text()
        texts[i] = clean_text(ele)


    # info 추출 
    contents = soup.find_all("div",attrs={"class":"of-h cb"})   
    for i , t in enumerate(contents):
        ele = t.get_text()
        infos[i] = clean_text(ele)

    # links 추출 
    contents = soup.find_all("h4",attrs={"class":"news_list_full_size news_list_title default_font font_bold font_limit title_h3"})
    for i , t in enumerate(contents): 
        link = t.a["href"]
        links[i] = 'https://www.itworld.co.kr' + link
    
    content = {'title':titles , 'link':links , 'text':texts , 'info': infos}
    status =  {'status_t':'active' ,'status_c':'deactive', 'status_g':'deactive'}
    dic = {'first':status, 'second':content}
   
    return render(request, 'app/index.html', dic)
    
def Corona(request):
    titles = {}
    links = {}
    texts = {}
    infos = {}
    url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%BD%94%EB%A1%9C%EB%82%9819'
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml" )

    # info추출 
    contents = soup.find_all("a",attrs={"class":"info press"})
    for i , t in enumerate(contents):
        ele=  t.get_text()
        
        if '언론사 선정' in ele:
            ln = len(ele)
            ele = ele[0:ln-6]
        infos[i] = ele


    # title 추출 
    contents = soup.find_all("a",attrs={"class":"news_tit"})
    for i , t in enumerate(contents):
        titles[i] = t.get_text()

    # text 추출 
    contents = soup.find_all("a",attrs={"class":"api_txt_lines dsc_txt_wrap"})
    for i , t in enumerate(contents):
        texts[i] = t.get_text()

    # links 추출 
    contents = soup.find_all("div",attrs={"class":"dsc_wrap"})
    for i , t in enumerate(contents):
        link = t.a["href"]
        links[i] = link
    
    content = {'title':titles , 'link':links , 'text':texts , 'info': infos}
    status =  {'status_t':'deactive' ,'status_c':'active', 'status_g':'deactive'}
    dic = {'first':status, 'second':content}
   
    return render(request,'app/index.html', dic)


def Game(request):

    #inven 기준 한 주제당 4요소(제목, 이미지, 내용, 기자)
    titles = {}
    links = {}
    texts = {}
    infos = {}
    url = 'https://www.inven.co.kr/webzine/news/?iskin=vr'
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml" )

    # enumerate -> i는 0부터
    #각각 19개의 데이터
    # title 추출 (0~19)
    contents = soup.find_all("span",attrs={"class":"cols title"})   
    for i , t in enumerate(contents):
        titles[i] = t.get_text()       


    # link 추출 //뭔가 잡것이 들어옴 -> 0은 더미 . 1번부터 시작임 (1~20)
    contents = soup.find_all("div",attrs={"class":"content"})   
    for i , t in enumerate(contents):      
        link = t.a["href"]
        if i != 0:  
            links[i-1] = link
        

    # text 추출 (0~19)
    contents = soup.find_all("span",attrs={"class":"cols summary"})   
    for i , t in enumerate(contents):
        texts[i] = t.get_text()   

    # info 추출 (0~19)
    contents = soup.find_all("span",attrs={"class":"info"})   
    for i , t in enumerate(contents):
        infos[i] = t.get_text()   
    
    content = {'title':titles , 'link':links , 'text':texts , 'info': infos}
    status =  {'status_t':'deactive' ,'status_c':'deactive', 'status_g':'active'}
    dic = {'first':status, 'second':content}
    
    return render(request,'app/index.html', dic)
   

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

# selenium chromedriver.exe 다운로드 필요


# 구글 이미지 검색으로 이미지를 검색
# searchName : 검색할 이미지명
# down_imgCount : 다운로드할 이미지수
# alldata : 페이지 전체 스크롤 여부
def googleImageSearch(searchName , down_imgCount , alldata ):
    global Gdriver
    Gdriver = webdriver.Chrome()
    # 구글 이미지 검색 주소
    Gdriver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
    elem = Gdriver.find_element_by_name("q")
    # 검색어 입력
    elem.send_keys(searchName)
    # 엔터키
    elem.send_keys(Keys.RETURN)
    time.sleep(0.5)

    # 전체 데이터 스크롤 여부 확인
    if (alldata):
        allimage()

    imgDownload(searchName , down_imgCount)

# 이미지 반복 다운로드
# searchName : 다운받을 이미지명
# down_imgCount : 다운로드할 이미지수
def imgDownload(searchName , down_imgCount):
    images = Gdriver.find_elements_by_css_selector(".rg_i.Q4LuWd")
    img_count = 1

    for image in images :
        if(img_count == down_imgCount+1):
            break
        try:
            image.click()
            time.sleep(0.5)

            imgUrl = Gdriver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
            # 폴더 생성하기

            os.makedirs('../imgs/tourapi_img/' + searchName + '/', exist_ok=True)
            # 다운로드
            urllib.request.urlretrieve(imgUrl,'../imgs/tourapi_img/'+searchName+'/'+ searchName +str(img_count)+".jpg")
            img_count = img_count + 1
        except BaseException as e:
            print(e)


    Gdriver.close()




# 검색한 페이지에 모든 정보를 보기 위해서 스크롤을 내려가지 않을때 까지 내림
def allimage():
    # 스크롤
    # 자바스크립트로 스크롤 크기를 찾아서 저장
    last_height = Gdriver.execute_script("return document.body.scrollHeight")

    while True:
        # 브라우저 끝까지 스크롤 내림
        Gdriver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

        time.sleep(1)

        new_height = Gdriver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                #driver.find_element_by_css_selector(".r0zKGf").click()
                Gdriver.find_element_by_css_selector(".mye4qd").click()
            except BaseException as e:
                print(e)

        last_height = new_height

# if __name__ == '__main__':
#     # 셀레니움 열기
#     # 검색어명 , 다룬로드 사진수 , 전체 데이터 스크롤 여부
#     googleImageSearch("공주 금성동 유적" , 10 , False)
#     googleImageSearch("공주 송산리 고분군", 10, False)
#
#     driver.close()
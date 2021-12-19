from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
from PreProcessing.resource_data.keys import Instagram_Id ,Instagram_Pw


def instagramGetImg(searchKeyword,selectElement, getImgCount):
    # 셀레니움 열기
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/")
    time.sleep(0.5)
    # 로그인 페이지
    elem = driver.find_element_by_name("username")
    elem.send_keys(Instagram_Id)
    elem = driver.find_element_by_name("password")
    elem.send_keys(Instagram_Pw)
    elem.send_keys(Keys.RETURN)
    time.sleep(3)
    # 로그인 정보 저장
    driver.find_element_by_css_selector(".sqdOP.yWX7d.y3zKF").click()
    time.sleep(3)
    # 알람설정 나중에
    driver.find_element_by_css_selector(".aOOlW.HoLwm").click()
    time.sleep(1)

    # 키워드 검색
    searchName = searchKeyword
    search_keyword = driver.find_element_by_css_selector(".XTCLo.x3qfX")
    search_keyword.send_keys(searchName)
    time.sleep(2)
    search_element = driver.find_elements_by_css_selector(".-qQT3")

    # 검색 키워드 중에 원하는 번째 키워드를 선택
    elementCout =0

    for i , clickElement in enumerate(search_element):

        if(elementCout == i):
            clickElement.click()
            break

    time.sleep(7)

    down_imgCount = getImgCount
    img_count = 1

    instDatas = driver.find_elements_by_css_selector(".v1Nh3.kIKUG._bz0w")

    for instData in instDatas:
        try:
            if (img_count == down_imgCount + 1):
                break
            imgUrl = instData.find_element_by_css_selector(".FFVAD").get_attribute("src")
            urllib.request.urlretrieve(imgUrl, '../imgs/tourapi_img/' + searchName + '/' + searchName + str(
                img_count) + "_instr.jpg")
            img_count = img_count + 1
        except BaseException as e:
            print(e)


    driver.close()


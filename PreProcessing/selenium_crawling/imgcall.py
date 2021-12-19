
from PreProcessing.selenium_crawling.google_crawling import googleImageSearch
from PreProcessing.selenium_crawling.instagram_crawling import instagramGetImg
import threading

def getGI_Imgs(keyword ,selectElement ,  count):
    instagramGetImg(keyword,  selectElement , count)

if __name__ == '__main__':
    Gyeonggi =['감악산 출렁다리' , '남한산성' , '두물머리' , '서오릉' , '수섬' , '팜랜드']
    Gangwon =['용아장성' , '장호항' , '봉정암' , '상고대' , '정동진']
    Chungcheongnam = ['명재고택' , '궁남지' , '부소산성' , '대둔산도립공원' , '고란사']
    Chungcheongbuk = ['보발재' , '문의문화재단지' , '솔밭공원' , '도담삼봉' , '구담봉']
    Gyeongsangbuk = ['월지' , '청량사탑' , '반월성' , '대왕암' , '양동마을' ]
    Gyeongsangnam = ['소매물도 등대' , '보리암' , '황매산' , '장사도해상공원' ,'대암산']
    Jeollabuk = ['전주한옥마을' , '덕유산' , '내장산' , '광한루' , '금산사']
    Jeollanam = ['불갑사' , '순천만' , '월출산' , '백학봉' , '대한다원']

    count = 20

    SearchLocation = Jeollanam
    for i in range(len(SearchLocation)) :
        keword =SearchLocation[i]
        t1 = threading.Thread(target=googleImageSearch, args=(keword, count, False))
        t1.start()
        getGI_Imgs(keword,  0 , count)


    # instar
    #getGI_Imgs('용아장성',  0 , count)


# 경기도 Gyeonggi
# 감악산 출렁다리 , 남한산성 , 두물머리 , 서오릉 , 수섬 , 팜랜드

# 강원도 Gangwon
# 용아장성 , 장호항 , 봉정암 , 상고대 , 정동진

# 충청남도 Chungcheongnam
# '명재고택' , '궁남지' , '부소산성' , '대둔산도립공원' , '고란사'

# 충청북도 Chungcheongbuk
# '보발재' , '문의문화재단지' , '솔밭공원' , '도담삼봉' , '구담봉'

# 경상북도 Gyeongsangbuk
# '월지' , '청량사탑' , '반월성' , '대왕암' , '양동마을'

# 경상남도 Gyeongsangnam
# '소매물도 등대' , '보리암' , '황매산' , '장사도해상공원' ,'대암산'

# 전라북도 Jeollabuk
# '전주한옥마을' , '덕유산' , '내장산' , '광한루' , '금산사'

# 전라남도 Jeollanam
# '불갑사' , '순천만' , '월출산' , '백학봉' , '대한다원'
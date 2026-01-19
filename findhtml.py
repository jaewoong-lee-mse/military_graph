from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 크롬 드라이버 실행
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 사이트 접속
driver.get("https://www.mma.go.kr/board/boardList.do")

# 현재 페이지 HTML 가져오기
html = driver.page_source

# 파일로 저장
with open("page1.html", "w", encoding="utf-8") as f:
    f.write(html)

print("page1.html 저장 완료")

# 브라우저 종료

